# Blank screen in the WattsWay iPhone app when navigating

**Status:** On his iPhone, Scott often gets a blank screen when going from the dashboard to Settings or back, and has to force-close and reopen the app. He suggested adding a "refresh" button to every page, since it's basically a web app. Claude recommended a global error boundary with a Reload button instead of per-page refresh buttons, and supplied an agent task. It's unknown whether Scott adopted or ran it.

**Open questions:** Refresh buttons versus an error boundary. The root cause of the crash.

**Blocked on:** Running the fix and capturing the error message on the next crash.

**Last activity:** July 2026

**Source:** Importing Garmin data with FitnessSyncer, 2026-07-10
