# Encrypted file sharing options for large videos
Date: 2026-07-19
Conversation: fcceb19e-a167-4b34-af3b-a95d9455ca92
Domain: skip

## Summary
**Conversation Overview**

The person needed help sharing large personal video files with their partner securely and privately. The core requirements were end-to-end encryption and the ability to handle files of 900MB or larger, as WhatsApp was insufficient for the file sizes involved.

Claude walked through several encrypted file-sharing options including Signal (ruled out due to the ~100MB file size limit), Tresorit Send, Proton Drive, and the approach of using AES-256 encrypted archives via 7-Zip uploaded to any cloud service. When the person asked specifically about Mega, Claude provided a balanced assessment covering its generous free tier, zero-knowledge encryption architecture, and the 2022 cryptographic vulnerability findings and subsequent patches. The person then confirmed they already have a paid 3TB Mega account, making the choice straightforward.

Claude provided specific guidance on using Mega securely: uploading to a dedicated folder, separating the decryption key from the share link and sending each through different channels, and deleting the folder and link once the recipient confirms download. An additional tip was offered — if the partner also has a Mega account, sharing directly to her account eliminates the need for a public link entirely. The person demonstrated a preference for concise, practical guidance and responded to the conversation by providing their existing setup details to narrow down recommendations.

### SCOTT (2026-07-19T00:31)
I have a few intimate videos I need to share with my girlfriend. They are too big to send via WhatsApp. What other options do I have. Need them them to be encrypted.

### CLAUDE (2026-07-19T00:31)
I'm thinking through the best ways to securely share large video files between two people, keeping the answer straightforward and mobile-friendly with a concise list format.A few solid options for large files with encryption:

- **Signal** – End-to-end encrypted by default, handles files up to ~100MB per video. Best combo of privacy and simplicity if you both install it.
- **Proton Drive** – E2E encrypted cloud storage. Upload, then share a link you can password-protect and set to expire.
- **Tresorit Send** – Free, E2E encrypted file transfer up to 5GB, links expire automatically.
- **iCloud/Google Drive with an encrypted container** – If you want to use mainstream cloud, zip the files with AES-256 encryption first (7-Zip or Keka) and share the password separately via a different channel.

Avoid standard WeTransfer or plain Drive/Dropbox links — those aren't end-to-end encrypted and links can leak.

Signal is the easiest if file sizes cooperate; Proton Drive or Tresorit if they're multi-GB. Whatever you use, send the password or link through a different app than the files themselves.

### SCOTT (2026-07-19T00:32)
Some are 900 mb or more

### CLAUDE (2026-07-19T00:32)
Signal's hitting around 100MB, so I should recommend the larger-file options to handle that capacity.That rules out Signal. Best options for 900MB+ files:

- **Tresorit Send** – Free, up to 5GB, end-to-end encrypted, no account needed for the recipient. Probably your easiest path.
- **Proton Drive** – Free tier gives 5GB storage, E2E encrypted, password-protected share links with expiration.
- **Encrypted 7z archive + any cloud** – Compress with 7-Zip using AES-256 and a strong password, upload anywhere (Drive, Dropbox), and text her the password on a different app. The encryption travels with the file, so the cloud provider can't see the contents.

Tresorit Send is the least friction: upload, get a link, send it, done. Just set the expiration short and delete after she's downloaded them.

### SCOTT (2026-07-19T02:30)
What about Mega?

### CLAUDE (2026-07-19T02:30)
Mega is a solid option with 20GB of free storage and end-to-end encryption, though I should mention its past security audit issues and the complexity around its ownership history to give a complete picture.Mega works, and it's actually a reasonable fit here:

**Pros:** 20GB free (way more than Proton or Tresorit's free tiers), zero-knowledge E2E encryption by default, and you can share a link with the decryption key separated from the URL — send the link in one app and the key in another. Password-protected links and expiry dates are available too (expiry may require a paid tier).

**Caveats worth knowing:** Security researchers found cryptographic flaws in Mega's design in 2022 — theoretically allowing Mega itself to decrypt files if it acted maliciously. They patched the specific attacks, but the architecture got criticized. Practically speaking, this matters against a determined adversary, not for keeping files private from casual snooping or a leaked link.

**Verdict:** For your use case it's fine, and the 20GB free tier makes it the practical winner if your videos total more than 5GB. If you want the strongest cryptographic pedigree, Proton or Tresorit; if you want free space and good-enough encryption, Mega.

One tip regardless of platform: send the link and the key/password through two different channels, and delete the files from the cloud once she's downloaded them.

### SCOTT (2026-07-19T02:31)
I already have a 3TB mega account.

### CLAUDE (2026-07-19T02:31)
Mega seems like the straightforward choice here.Then use Mega — no reason to add another service.

Quickest way to do it securely:

1. Upload the videos to a dedicated folder (not mixed with other files).
2. Share the folder link, but use the option to **send the decryption key separately** — Mega lets you copy the link without the key embedded.
3. Send the link via one app and the key via another (e.g., link on WhatsApp, key via text or in person).
4. Once she confirms she's downloaded them, delete the folder and the link.

If she has a Mega account too, an even cleaner option is sharing the folder directly to her account instead of using a public link — no link floating around at all, and access stays tied to her login.
