# [UNCERTAIN] Per-user Drive folder ID stored in user_integrations

**Decided:** The Cursor agent built each user's Drive folder ID into user_integrations (provider 'garmin'), entered on the Settings card, and used two secrets: GOOGLE_SERVICE_ACCOUNT_EMAIL and GOOGLE_SERVICE_ACCOUNT_PRIVATE_KEY. Claude first tried to revert this and then accepted it. Scott went along and deployed it.

**Why:** It supports the multi-user family model, with each member's folder mapped separately. (Claude's reasoning.)

**Rejected alternatives:** A single DRIVE_TCX_FOLDER_ID secret plus a single GOOGLE_SERVICE_ACCOUNT_KEY JSON secret. This was Claude's original spec.

**Would revisit if:** unknown

**Approx date:** July 2026

**Source:** Importing Garmin data with FitnessSyncer, 2026-07-10
