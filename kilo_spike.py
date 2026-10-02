"""
Kilo spike: Managed Agents + a memory store over a slice of the notes corpus.

Purpose: one-hour test of whether Managed Agents can carry Kilo's runtime,
before re-sequencing the build around it.

Scope is deliberately limited to non-employer, non-health folders
(farms, concrete, pool, WattsWay app). Business Ops / Manila (employer data
boundary, harvest-playbook 5.1), fitness (health), and job-search stay out
until the data-location decision is made.

Usage (Command Prompt, from C:\\Users\\scott\\Dev\\notes):
    python kilo_spike.py setup      # create store, seed notes, create agent + env
    python kilo_spike.py add --folders X Y   # load more folders into the same store
    python kilo_spike.py chat       # ask questions; type 'quit' to stop
    python kilo_spike.py cleanup    # delete everything the spike created
Options:
    --notes PATH   notes repo root (default: current directory)
    --limit N      number of notes to seed (default 20)
    --folders A B  note folders to seed (default: farms, concrete, pool, app)
"""

import argparse
import itertools
import json
import sys
from pathlib import Path

from anthropic import Anthropic

SPIKE_FOLDERS = ["watts-way-farms", "farm-concrete", "home-pool", "wattsway-app"]
IDS_FILE = Path(__file__).with_name("spike_ids.json")
MAX_BYTES = 100_000  # memory store per-memory cap is ~100 kB
MODEL = "claude-opus-5-5"

SYSTEM = """You are Kilo, a private single-user assistant for Scott.

Your knowledge of Scott's world is the notes memory store mounted in your sandbox.
Rules:
- Before answering, search the mounted notes (grep/glob/read). Do not answer from general knowledge when the notes could hold the answer.
- Do not use web search or web fetch.
- Cite the note file path for every claim drawn from the notes.
- Distinguish what Scott decided from what was only proposed or suggested. If a note marks something [UNCERTAIN] or PENDING, say so.
- Check for rejected alternatives before recommending an approach, and surface them if they match.
- If the notes don't answer the question, say that plainly instead of guessing.
- Direct, analytical register. Lead with the answer. No preamble, no restating the question.
- This is a read-only test: do not write to or modify the notes store."""

STORE_INSTRUCTIONS = (
    "Scott's harvested notes, one topic per file, folders by domain. "
    "Search this before answering any question about Scott's projects, decisions, or history."
)

SUGGESTED_QUESTIONS = [
    "Across the farm, concrete, and pool work, what have I decided about contractors or equipment, and what did I rule out?",
    "What's still open or pending across all of these notes?",
    "(exact-string test) Search for a specific vendor, product, or place name you know is in one of the notes.",
    "(cross-domain) Is there anything in the WattsWay app notes that affects or depends on the farm?",
]


def load_ids():
    if not IDS_FILE.exists():
        sys.exit("No spike_ids.json found. Run 'python kilo_spike.py setup' first.")
    return json.loads(IDS_FILE.read_text())


def pick_files(root: Path, limit: int, folders):
    """Round-robin across folders so the seed spans several domains."""
    groups = []
    for folder in folders:
        d = root / folder
        if not d.is_dir():
            print(f"  (skipping missing folder: {folder})")
            continue
        files = sorted(p for p in d.rglob("*.md") if p.stat().st_size <= MAX_BYTES)
        if files:
            groups.append(files)
    picked = []
    for row in itertools.zip_longest(*groups):
        for p in row:
            if p is not None and len(picked) < limit:
                picked.append(p)
    return picked


def setup(client: Anthropic, root: Path, limit: int, folders):
    if IDS_FILE.exists():
        sys.exit("spike_ids.json already exists. Run cleanup first, or use 'add' to load more.")

    store = client.beta.memory_stores.create(
        name="kilo-spike-notes",
        description="Scott's harvested notes, verbatim chat transcripts, project docs and Claude memory export.",
    )
    agent = client.beta.agents.create(
        name="Kilo spike",
        model=MODEL,
        system=SYSTEM,
        tools=[{"type": "agent_toolset_20260401"}],
    )
    env = client.beta.environments.create(
        name="kilo-spike-env",
        config={"type": "cloud", "networking": {"type": "unrestricted"}},
    )
    # Save IDs before loading anything, so a crash or Ctrl+C can be resumed with 'add'.
    IDS_FILE.write_text(json.dumps(
        {"store": store.id, "agent": agent.id, "env": env.id, "sessions": []}, indent=2
    ))
    print(f"Memory store: {store.id}\nAgent: {agent.id}\nEnvironment: {env.id}")
    add(client, root, limit, folders)


def add(client: Anthropic, root: Path, limit: int, folders):
    """Load more folders into the existing store. Skips notes already there."""
    ids = load_ids()
    files = pick_files(root, limit, folders)
    if not files:
        sys.exit(f"No .md files found under {root} in {folders}.")
    print("Checking what's already loaded...")
    have = set()
    for item in client.beta.memory_stores.memories.list(ids["store"], path_prefix="/"):
        have.add(item.path)
    files = [p for p in files if "/" + p.relative_to(root).as_posix() not in have]
    print(f"{len(have)} already loaded, {len(files)} to add.")
    added = skipped = 0
    for p in files:
        rel = "/" + p.relative_to(root).as_posix()
        try:
            client.beta.memory_stores.memories.create(
                ids["store"], path=rel,
                content=p.read_text(encoding="utf-8", errors="replace"),
            )
            added += 1
            if added % 100 == 0:
                print(f"  {added} added...")
        except Exception as e:
            skipped += 1
            msg = str(e)[:200]
            print(f"  SKIPPED {rel}: {msg}")
            with open(IDS_FILE.with_name("spike_skipped.txt"), "a", encoding="utf-8") as log:
                log.write(f"{rel}\t{msg}\n")
    print(f"\nAdded {added}, skipped {skipped}. Skipped files are listed in spike_skipped.txt.")
    print("If interrupted, run the same 'add' command again - it picks up where it left off.")


def orphans(client: Anthropic):
    """Delete memory stores named kilo-spike-notes that the current spike isn't using."""
    keep = load_ids()["store"] if IDS_FILE.exists() else None
    for st in client.beta.memory_stores.list():
        if st.name == "kilo-spike-notes" and st.id != keep:
            client.beta.memory_stores.delete(st.id)
            print(f"  deleted leftover store {st.id}")
    print("Done.")


def describe_tool(event) -> str:
    inp = getattr(event, "input", None)
    if isinstance(inp, dict):
        for key in ("path", "file_path", "pattern", "command", "query"):
            if inp.get(key):
                return str(inp[key])[:120]
    return ""


def chat(client: Anthropic):
    ids = load_ids()
    session = client.beta.sessions.create(
        agent=ids["agent"],
        environment_id=ids["env"],
        title="Kilo spike",
        resources=[{
            "type": "memory_store",
            "memory_store_id": ids["store"],
            "access": "read_only",
            "instructions": STORE_INSTRUCTIONS,
        }],
    )
    ids["sessions"].append(session.id)
    IDS_FILE.write_text(json.dumps(ids, indent=2))

    print(f"Session {session.id}. Tool lines show which notes it opened.")
    print("Suggested questions:")
    for q in SUGGESTED_QUESTIONS:
        print(f"  - {q}")

    while True:
        try:
            q = input("\nyou> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not q:
            continue
        if q.lower() in ("quit", "exit"):
            break

        with client.beta.sessions.events.stream(session.id) as stream:
            client.beta.sessions.events.send(
                session.id,
                events=[{"type": "user.message", "content": [{"type": "text", "text": q}]}],
            )
            print("kilo> ", end="", flush=True)
            for event in stream:
                if event.type == "agent.message":
                    for block in event.content:
                        if block.type == "text":
                            print(block.text, end="", flush=True)
                elif event.type == "agent.tool_use":
                    print(f"\n   [{event.name}] {describe_tool(event)}", flush=True)
                elif event.type == "session.status_idle":
                    print()
                    break

    print("\nDone. Check token cost for this session in the Console usage page.")


def cleanup(client: Anthropic):
    ids = load_ids()
    steps = [(f"session {s}", lambda s=s: client.beta.sessions.delete(s)) for s in ids["sessions"]]
    steps += [
        (f"memory store {ids['store']}", lambda: client.beta.memory_stores.delete(ids["store"])),
        (f"agent {ids['agent']}", lambda: client.beta.agents.archive(ids["agent"])),
        (f"environment {ids['env']}", lambda: client.beta.environments.delete(ids["env"])),
    ]
    for label, fn in steps:
        try:
            fn()
            print(f"  removed {label}")
        except Exception as e:  # keep going; report what didn't clear
            print(f"  could not remove {label}: {e}")
    IDS_FILE.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("command", choices=["setup", "add", "chat", "cleanup", "orphans"])
    ap.add_argument("--notes", default=".", help="notes repo root")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--folders", nargs="+", default=SPIKE_FOLDERS, help="note folders to seed")
    args = ap.parse_args()

    client = Anthropic()  # reads ANTHROPIC_API_KEY from the environment
    if args.command == "setup":
        setup(client, Path(args.notes).resolve(), args.limit, args.folders)
    elif args.command == "add":
        add(client, Path(args.notes).resolve(), args.limit, args.folders)
    elif args.command == "orphans":
        orphans(client)
    elif args.command == "chat":
        chat(client)
    else:
        cleanup(client)


if __name__ == "__main__":
    main()
