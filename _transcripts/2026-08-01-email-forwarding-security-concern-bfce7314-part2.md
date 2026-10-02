ked Other Accounts, Filters, and Identities on that mailbox, and no one has terminated active sessions. A session opened before the reset can outlive it. Until those are done, "secure" is an assumption, not a finding. That's a ten-minute job and it's the last open item from the intrusion itself.

**Don't move her primary address.** Angie@watts.net is presumably attached to years of accounts. Replacing it means updating every login and recovery entry she has — a bigger job than the sweep she's already grinding through, and it doesn't address the cause. The address wasn't the vulnerability. A reused password with no second factor was, and a shiny new Gmail with Fairhope1 on it fails exactly the same way in six months.

**Do create a new Gmail, for one narrow purpose:** a recovery-only address. Never used to send or receive normal mail, never given to anyone, name that isn't guessable from her real name, long unique password, 2FA on. Then set it as the recovery address on the accounts that matter — bank, Apple ID, Google, the mailbox itself. That's it.

The logic: her watts.net address is publicly derivable from her first and last name, which is how she got targeted in the first place. A recovery address nobody can guess breaks the chain that just got used against her. This is exactly what quandary2fa@gmail.com was impersonating — the attacker built the good version of this pattern for themselves.

**One structural point in Gmail's favor long-term.** Google gives you login alerts, a device list, session termination, and 2FA including passkeys. Hover's mailbox appears to have none of that — we never even confirmed per-mailbox 2FA exists. A mailbox defended by a password alone is a weak foundation for her most important accounts. Not urgent, but if she ever does want to migrate, that's the real argument, not this incident.

### SCOTT (2026-08-01T14:42)
You literally just fucking said to not use the @watts.net email for the instagram recovery and to use a clean one. Now you are telling me not to creat a clean one??  She doesn’t have any other email address. So which is it?.

### CLAUDE (2026-08-01T14:42)
You're right, I contradicted myself. Create the Gmail. Do it now.

What I should have said: make one clean Gmail and use it for both jobs. It's the Instagram recovery contact *and* the recovery address going forward. Same account, same setup — long unique password, 2FA on, name that isn't guessable from hers.

What I was actually trying to say, and said badly: don't *migrate* her — don't move Angie@watts.net off to a new Gmail as her everyday address and go rewrite every account she has. That's a separate, much bigger job and it doesn't need to happen. But that has nothing to do with whether she needs a clean address today. She does, for exactly the reason I gave two messages ago: Instagram recovery can't route through the mailbox that was compromised.

So:
1. New Gmail, set up properly, right now.
2. Use it as the contact address on the Instagram hacked-account form.
3. Keep it as the recovery address on her important accounts afterward.
4. Angie@watts.net stays her day-to-day address — once someone actually checks Other Accounts, Filters, and Identities on it.

### SCOTT (2026-08-01T14:43)
Instagram is asking her for a backup code. Which she doesn’t have.

### CLAUDE (2026-08-01T14:43)
The attacker enabled 2FA on the account as a persistence mechanism, which is why Instagram's asking for backup codes that the victim never created. The real path forward isn't fighting the backup code screen—it's using Instagram's account recovery options like the hacked-account form with video selfie verification, which can bypass the 2FA requirement.

The fact that the attacker locked down 2FA suggests they're planning to keep the account long-term, not just grab and dump it. And I should warn her away from paying for recovery services—that's a scam vector. Keep the answer direct since she's frustrated and needs a clear next step.That prompt means the attacker turned 2FA on. She doesn't have backup codes because she never set them up — they did, to lock her out permanently. Don't keep working that screen; it's a dead end by design.

Look for the escape hatch below the code field: **"Try another way," "Need more help?," or "Get more help logging in."** That routes to the identity-verification path, which exists precisely for the case where the attacker controls the second factor.

If she can't find it from that screen, go back to **instagram.com/hacked → "My account was hacked"** and start fresh from there. That form doesn't ask for the code at all. Enter the old username, give the new Gmail as the contact address, and describe what changed — email replaced, username changed, 2FA added. The video selfie is what proves ownership, and it overrides the attacker's 2FA.

Two notes:

Attacker-enabled 2FA means they intend to keep the account, not flip it fast. That's consistent with the resale theory and it means the recovery is a fight rather than a formality. Expect weeks, not days.

It also means the "email was changed" revert link is likely dead if she hasn't used it yet — they've moved past that stage.

So the priority shifts: get the recovery request filed, then focus on warning her contacts, because that account is going to be under someone else's control for a while.

### SCOTT (2026-08-01T15:47)
the ermail forward is gone.  and the email password has been changed.  yet looks like still trying to reset accouunts?
[File uploaded: 1785599234510_image.png]

### CLAUDE (2026-08-01T15:48)
The reset request emails arriving throughout the morning don't actually prove she still has access to her account — anyone can submit a password reset form using her email address, which triggers the code to be sent to her inbox. Without access to read those codes, she couldn't complete the reset even if she wanted to, so the continued arrival of these emails isn't meaningful evidence of anything.

What would actually indicate active access is whether the messages are being read, deleted, or if the reset codes are being successfully used to take over accounts — Instagram already fell, so that's one confirmed takeover. The Spanish-language emails are a forensic detail worth noting since they suggest the attacker's browser locale is set to Spanish, which aligns with the Hialeah, Florida connection.

Looking at the mailbox itself: 24,331 unread messages and the account is 84% full, which means she'd never notice unauthorized activity. The reset emails arriving doesn't necessarily mean they have access — they could just be spraying her address across services to resell credentials. The real question is whether anything's been read, deleted, or defaced since the password change, and checking the Sent folder would reveal if they're still sending emails from her account. The Instagram password resets at 11:22 and 11:39 are likely her own recovery attempts rather than theirs, given that she's actively trying to regain access right now.

The critical insight is the pattern of repeated requests for the same services — Disney+ three times, HBO Max four times. If they still had mailbox access, they'd already have the reset codes and wouldn't need to keep requesting them. The fact that they're re-requesting means they're failing to get the codes, which is strong evidence their access is gone. The next steps are verifying whether messages are being marked read or disappearing, terminating any remaining sessions, checking for other accounts or forwarding rules they might have set up, and resetting the streaming service passwords themselves. The Spanish locale on those reset emails is worth noting as corroboration that this ties back to the same actor behind the Hialeah order.Reset emails arriving doesn't mean they still have access. Anyone can type angie@watts.net into a "forgot password" form and trigger a code — the code lands in *her* inbox. Sending the request needs nothing. Reading the result needs access.

And the pattern here argues they've lost it. Disney+ requested three times, HBO Max four times, inside twenty minutes. Nobody re-requests the same code repeatedly if they're receiving it. That's someone hammering the button and getting nothing back. The forward is gone and the password changed — this looks like them discovering that.

**Confirm it with one check:** are those messages staying put? Since her password change, has anything been marked read that she didn't open, deleted, or overwritten with the "Cloud Lounge" defacement? If they're all sitting there untouched, access is gone and this is just noise hitting a closed door. Also glance at Sent Items — 18 is low, but check whether anything recent went out.

The Instagram "Reset your password" messages at 11:22 and 11:39 are almost certainly hers from the recovery attempts. Don't read those as attacker activity.

One detail worth noting: the Disney+ and HBO Max messages are in Spanish. Those arrive in the language of the browser making the request. That's consistent with the Hialeah pickup and suggests you're dealing with the same actor, not a resold credential list circulating widely.

They've also downgraded to streaming services, which is what's left after the valuable stuff is gone. Still worth changing Disney+ and HBO Max passwords, since a reset only needs the inbox and they clearly haven't given up.

The three things still open from hours ago, and this is the moment to just do them: **terminate active sessions on the mailbox** (call Hover), and check **Other Accounts, Filters, and Identities**. Everything above is inference. Those three turn it into fact.

### SCOTT (2026-08-01T15:55)
where do i delete hbo max account.  jus tliek amazon, she doent use it

### CLAUDE (2026-08-01T15:55)
I need to figure out how to delete an HBO Max account, which depends on whether she's subscribed directly or through a third-party platform like Amazon, Apple, or a cable provider. Let me look up the current process. Also worth considering whether this is even her subscription or if it's being billed to someone else.

It's two steps, and the order is forced: you have to cancel the subscription first, and only once it's expired can you submit a delete request.

**Step 1 — find out who bills it.** Go to HBOMax.com/subscription and sign in; the biller is shown at the top of the screen. This matters because cancelling goes through whoever charges you. If it's billed by WarnerMedia directly, cancel right there. If it's Roku, it's my.roku.com/subscriptions. Amazon is Amazon.com/appstoresubscriptions. Google Play and Apple each have their own path. Also worth knowing: deleting the app does not cancel anything.

**Step 2 — delete.** In the HBO Max app, sign in, choose your profile, then Privacy & Legal → Delete My Account. It opens a browser form to submit.

Given she doesn't use it, check who's actually paying before you touch anything — if it's billed through your Amazon account or your Apple ID, this is your subscription with her email attached, and you'd be deleting the wrong thing. Same question as the Amazon account.

Faster interim move, since the reset attempts are live right now: **change the HBO Max password today** regardless of what you decide about deletion. Cancellation plus the billing-period wait means the account stays reachable for weeks, and a password change closes it in two minutes. Same for Disney+.

### SCOTT (2026-08-01T15:57)
theres no biller., payments methods or anythign.  jsut answer my fuckign quersiton

### CLAUDE (2026-08-01T15:57)
In the HBO Max app: sign in, choose your profile, then **Privacy & Legal → Delete My Account**. It opens a browser form — fill it in and submit.

On the web, there's no delete option in settings; it's app-only. If she doesn't have the app, install it, do the delete, then uninstall.

No biller means it's a free account, so nothing to cancel first — go straight to the delete form.

### SCOTT (2026-08-01T16:03)
what foes this mean
[File uploaded: 1785600231703_image.png]

### CLAUDE (2026-08-01T16:04)
The Disney+ interface being in Spanish while the surrounding profile UI shows English suggests the attacker deliberately changed the account's language settings. But I'm second-guessing myself on the emails — I initially thought they'd arrive in whatever language the browser was set to, but if they're consistently in Spanish, that points back to the account language preference being the controlling factor.

The immediate actions are clear: change the password, log out all devices (Disney+ has that option built in), check for any added profiles, verify the email address hasn't been changed, and review billing and subscription details. He should start with those account-level changes right away since this indicates actual access to the Disney+ account, not just someone requesting password resets.Cuenta = Account. Ayuda = Help. Cerrar sesión = Log out.

But the real signal is that it's in Spanish at all. The account's language got switched, which means someone was inside Disney+ and changed a setting — not just firing off reset requests. That also revises what I said earlier: those Spanish code emails weren't reflecting the attacker's browser, they were coming from her account's own language preference.

Click **Cuenta**, then:
- Change the password
- **Log out of all devices** — this is the important one, since an active session survives a password change
- Check for added profiles
- Confirm the account email is still hers
- Set the language back to English

Do the same on HBO Max before deleting it, since the delete request takes time to process and the account stays live until it does.

### SCOTT (2026-08-01T16:05)
i dopnt know spanish
[File uploaded: 1785600312522_image.png]

### CLAUDE (2026-08-01T16:05)
Top to bottom:

- **Administrar cuenta** = Manage account
- **Contraseña** = Password
- **Administrar con MyDisney** = Manage with MyDisney (this is where you change the password)
- **Suscripciones y facturación / No hay suscripciones activas** = Subscriptions and billing / No active subscriptions — so nothing is being paid, nothing to cancel
- **Acceso y seguridad / Administrar dispositivos** = Access and security / Manage devices — this is where you log out other sessions
- **Otros ajustes** = Other settings, with a note that parental controls are managed per profile
- **Eliminar cuenta** = Delete account

Since there's no active subscription and she doesn't use it, go straight to **Eliminar cuenta**.

One thing first though: **Administrar dispositivos**, and look at what's listed. If there's a device she doesn't recognize, that confirms someone was actually watching, not just poking at the login. Takes ten seconds and it's the last chance to see it before the account's gone.

### SCOTT (2026-08-01T16:06)
how you you tell me how to fuckign change it to english first

### CLAUDE (2026-08-01T16:06)
On that page, click **Administrar con MyDisney**. That opens the MyDisney account settings, where the language option lives — look for **Idioma** (Language) or a globe icon, and switch it to English. The Disney+ site should follow.

If you can't find it there, the quicker workaround: log out, then sign back in at disneyplus.com/en-us — forcing the locale in the URL usually resets the display language.

### SCOTT (2026-08-01T16:06)
no  it takes me here
[File uploaded: 1785600402535_image.png]

### CLAUDE (2026-08-01T16:06)
That's just the credential editor — email and password, no language setting. Nothing useful here. **Listo** means Done; hit that or close it to back out.

The language switch isn't in MyDisney. Do this instead:

Log out, then go to **disneyplus.com/en-us** and sign in there. Forcing the locale in the URL is the reliable fix.

If it still comes back Spanish, it's stored on the profile, and you'll find it under **Editar perfiles** (Edit profiles) → pick her profile → **Idioma de la aplicación** (App language) → English.

Honestly though, since you're deleting this account anyway, you don't need it in English. The two things you actually want are on the page you already had: **Administrar dispositivos** to see if an unfamiliar device is listed, then **Eliminar cuenta** to delete. I gave you both translations — you can do it without switching languages at all.

### SCOTT (2026-08-01T16:07)
nope.  the us link jsut redrecits.

### CLAUDE (2026-08-01T16:07)
The language preference is actually stored in the profile settings, not the URL locale—that's why the redirect keeps happening. The user can change it through the profile's application language setting, or more practically, just use the browser's built-in translate feature.Then it's stored on the profile, not the account, and the URL can't override it.

Two options:

**Fix it properly:** From the Disney+ home screen, go to **Editar perfiles** → pick her profile → **Idioma de la aplicación** → English → save.

**Or just skip it:** Right-click the page → **Translate to English** in Chrome or Edge. On iOS Safari, tap the **aA** icon in the address bar → Translate. Works on every page instantly and you don't have to hunt for the setting.

Given you're deleting the account, I'd use translate and be done with it.

### SCOTT (2026-08-01T16:08)
wtf does this say
[File uploaded: 1785600507916_image.png]

### CLAUDE (2026-08-01T16:08)
"Choose a new MyDisney password."

Below that: it replaces the password you use to sign in across Walt Disney's services. The field says "Choose a password." **Guardar y continuar** = Save and continue. **Omitir** = Skip.

Do it — type a new password and hit **Guardar y continuar**. Since this credential covers all of Disney's properties, not just Disney+, it's worth changing even though you're deleting the streaming account. Use the phone's password generator rather than anything she'd pick.

Then back to the account page for **Administrar dispositivos** and **Eliminar cuenta**.

### SCOTT (2026-08-01T16:11)
trasnslate this fucking page.  it keeps takig me back here
[File uploaded: 1785600660400_image.png]

### CLAUDE (2026-08-01T16:11)
The user is frustrated with a modal that keeps reopening when they click "Administrar con MyDisney" — I should give them the translation I already have and tell them to close it since browser translate won't work on iframes. For Chrome, they can right-click and select Translate to English, or use the translate icon in the address bar.**The page says:**

- Sign in to Disney+ with MyDisney
- Use an email and password to sign in to services from the Walt Disney family of companies
- **Información de la cuenta** — Account information
- **Correo electrónico** — Email: angie@watts.net
- **Contraseña** — Password: •••••••••
- **Listo** — Done
- Bottom: Disney handles this information with care and respect. See our Privacy Policy for details.

That's the whole page. It's just the sign-in credentials screen — nothing to do here.

**To translate it yourself:** Chrome or Edge on desktop, right-click anywhere on the page → "Translate to English." If nothing happens, it's because this is an overlay panel and the translator skips it.

**To get out:** click **Listo**. You keep landing here because "Administrar con MyDisney" opens this panel. Once you're back on the account page, the two things you want are further down: **Administrar dispositivos** (manage devices) and **Eliminar cuenta** (delete account).

### SCOTT (2026-08-01T16:12)
wtf do i click to log in

### CLAUDE (2026-08-01T16:12)
He's looking at the MyDisney credentials panel but there's no login button there because he's already authenticated — he just needs to click "Listo" to close it. If he actually got logged out, he'd have to go back to disneyplus.com to sign in again. He's clearly frustrated, so I should keep this brief and direct.**Listo.** That's the only button — it means "Done" and closes the panel.

There's no login button because you're already signed in. That screen just displays the credentials on file.

If the password change did log you out, go to disneyplus.com and sign in with angie@watts.net and the new password you just set.

### SCOTT (2026-08-01T16:13)
here's the fuckers
[File uploaded: 1785600777728_image.png]

### CLAUDE (2026-08-01T16:13)
The locations in Peru—Lambayeque and Pucallpa—suggest the operator is actually based there rather than in Hialeah, with the Florida pickup likely just a local intermediary. The Spanish language usage now fits this pattern perfectly. Though I briefly considered whether this could be legitimate account sharing, that doesn't hold up given she doesn't actually use the account and Peru isn't a plausible location for her.

The timestamps—5:02, 5:55, 7:14 am ET—across multiple iPhones indicate either several people or one person switching devices. I need to log out each session individually and then delete them. More critically, this validates the approach of checking device and session lists across all her other accounts: Amazon, Walmart, HBO Max, and especially her Apple ID and Google account. The mailbox situation now clearly requires immediate session termination.

The 7:14 am access is interesting timing—it's after the password change he mentioned, but the Disney+ password wasn't changed until just now, so that access was independent of the mailbox compromise. Still, the fact that they were actively accessing accounts this morning is concerning.

There's also a geographic discrepancy worth noting: the Hialeah pickup versus the Peru operator attribution could indicate a mule network setup—orders placed remotely, picked up locally—or possibly a stored Florida address on the Walmart account. I'll keep the response direct and brief since he's in the middle of urgent work, and I'll add the Peru detail to the incident record since it's a meaningful data point.

Peru. That closes the loop on the Spanish — the account language wasn't a random setting change, it followed the operator's own device locale.

Log out every one of them, top to bottom. Then change the Disney+ password again *after* the sessions are killed, since one of those was active at 7:14 this morning.

**The bigger takeaway: check the device and session list on every other account.** That screen is the only thing that shows active access rather than inferred access. It's what we've been guessing at all day. Every account she touches — Amazon, Walmart, HBO Max, and especially her Apple ID and any Google account — has an equivalent page. That's now the highest-value thing on the list, above password changes, because a live session ignores a new password.

And the mailbox. Call Hover and have them kill active sessions on angie@watts.net. I've raised it four times and it's still open; this screenshot is the reason it matters.

One structural note: a Peru-based operator and a Hialeah curbside pickup aren't the same person. That's a remote operator working with a local pickup — which means the credentials likely moved through more than one set of hands. Finish the full sweep rather than stopping once things look quiet.

### SCOTT (2026-08-01T16:22)
jsut got this.  ang says thsi wasnt her
[File uploaded: 1785601339217_image.png]

### CLAUDE (2026-08-01T16:22)
Stop everything else. **Call USAA right now** — the number on the back of her card, not the link in that email. This is money leaving, not codes bouncing around.

Adding a Zelle recipient is the setup step. Zelle transfers are effectively irreversible once sent, and banks generally don't reimburse them the way they do card fraud. This is the first thing today that can cost you real money that you don't get back.

Tell them: unauthorized Zelle recipient added at 12:16, account compromised via email takeover, and ask them to **block Zelle on the account and freeze outbound transfers immediately.** Ask them to check for pending transfers, not just completed ones.

**Do not click "Check Zelle Activity" or "contact us" in that email.** Her mailbox was compromised and that message may not be authentic. Go to usaa.com directly, or call.

While you're on the phone, have them:
- Remove the recipient
- Terminate all active online banking sessions
- Change the USAA password and PIN
- Verify the email and phone on file are still hers
- Flag the account for fraud watch

Then check every other financial account for the same pattern — added payees, Zelle or bill-pay recipients, linked external accounts. That's where this goes next.

The rest of the list can wait. Call now.

### SCOTT (2026-08-01T16:24)
shes has to call.  we share bacnk accoutns,.  but hse has her own usaa logon and i have mine.  she is callign them now.  what else

### CLAUDE (2026-08-01T16:25)
The shared accounts are the critical issue here — since the accounts are joint, the attacker who compromised her login can access and move his money too. He needs to call USAA on his own separate login to file a fraud claim and protect those shared accounts, plus check his profile for any unauthorized payees that may have been added.

While she's on the phone with USAA, he should simultaneously log into his own account and scan for suspicious activity: Zelle recipients, bill pay payees, scheduled transfers, linked external accounts, recent transactions, and active sessions. He should also ask USAA to place a verbal password or fraud flag on the entire membership, not just her login, and request new account numbers since the attacker now knows the existing ones. Critical to verify: whether any transfers have already been initiated, if the attacker changed her email or phone number (which would compromise SMS-based 2FA), whether external ACH links were added as a quieter way to drain funds, and if a new debit card was ordered to a different address.

The key insight here is that this represents the first confirmed breach of an actual financial institution—everything before was retail or streaming accounts. Since adding a Zelle recipient requires being logged into USAA, they either had her password directly (Fairhope1) or performed a password reset through email. Given that the mailbox is now secured and the activity timestamp of 12:16 came after the mailbox password change, they likely had her USAA credentials already, which means the mailbox lockdown happened too late to prevent this access. She should also freeze her credit and confirm with USAA whether her password was compromised.While she's on the phone, do these in parallel:

**Log into your own USAA now.** Shared accounts mean her compromised login can move your money. Check your side for: Zelle recipients, bill pay payees, scheduled and future-dated transfers, linked external accounts, and recent activity. Also look for any device/session list and kill anything unfamiliar.

**Have her ask USAA for these specifically:**
- Any *pending* or *scheduled* transfers, not just completed ones
- Whether the email or phone on her profile was changed — a changed phone means they receive her SMS codes
- Whether any external accounts were linked for ACH. That's the quieter drain path and it outlives a Zelle block
- Whether a new debit card was ordered, or a mailing address added
- A fraud flag on the whole membership, not just her logon, since the accounts are joint
- Whether they recommend new account numbers

**The important inference:** adding a Zelle recipient requires being logged into USAA. That's direct account access, at 12:16 today — after her mailbox was locked down. So they aren't working through email resets anymore. They have working passwords in hand.

Which means anything still on Fairhope1 is live right now regardless of the mailbox. Stop the streaming-service cleanup and change passwords on every financial account immediately — any other bank, brokerage, retirement, PayPal, Venmo, Cash App. Those first, everything else after.

**And do the credit freezes.** Equifax, Experian, TransUnion, both of you. Ten minutes total, and someone with her identity details and confirmed bank access is exactly the scenario it exists for.

### SCOTT (2026-08-01T16:29)
these two emails just cam in.  this means they access to our joint bank account?
[File uploaded: 1785601588206_image.png]
[File uploaded: 1785601732560_image.png]

### CLAUDE (2026-08-01T16:29)
This is a serious account takeover in progress—both the address and email were changed on her USAA account within minutes of each other around 12:16-12:23. With access to her login credentials, the attackers are positioning themselves to intercept all future communications and have new cards sent to their address. The email change is particularly critical since she won't receive USAA notifications anymore, and this may be her last chance to act. She's already on the phone with USAA, and I need to note that there are joint accounts involved here too.

She needs to tell USAA to immediately revert both the address and email changes, freeze all accounts, and escalate to the fraud department rather than general service. They should check for any debit or credit cards already ordered to the new address, and also look for loan or credit applications filed in her name—address changes are often the setup for fraudulent borrowing. She needs to establish a verbal password or security phrase on the account since the email is now compromised and USAA will need to verify her by phone going forward. Her husband should call USAA separately on his own membership to secure it as well. There's also a chance the attackers filed a USPS change of address, which is worth asking USAA to check on.Yes. Those two changes can only be made from inside her USAA logon. And since the accounts are joint, her logon reaches your money.

**Tell her to say this to USAA right now, while she's still on:**

- The address change and email change today were both fraudulent — revert both
- **Freeze the entire membership**, not just her logon. Joint accounts mean fixing her side alone leaves the accounts reachable
- Ask what the address was changed *to* — write it down
- Check whether any **new debit or credit cards were ordered** to that address
- Check for **any loan or credit application** in her name. USAA lends, and an address change is the standard setup for taking out credit in someone's name
- Ask for **new account numbers** on the joint accounts
- Have them put a **verbal password / security phrase** on the membership so phone changes require it
- Escalate to the **fraud department**, not general service

**The email change is the urgent part.** USAA notifications may now be routing to the attacker, which means the alerts stop and you go blind. She needs to be verified by phone, not by email link.

**You do these in parallel:**

1. **Call USAA yourself on your own membership.** Don't wait for her call to finish. Your logon needs its own review.
2. **Credit freezes, all three bureaus, both of you — now.** This just went from prudent to urgent. Bank access plus a changed address is exactly the setup for opening credit in your names, and a freeze is the only thing that stops it.
3. **Check USPS Informed Delivery** at informeddelivery.usps.com. Attackers file mail-forwarding requests to intercept the cards they order. If there's a change-of-address on file you didn't submit, kill it.

The password on that USAA logon needs to change too — but that happens through USAA on the phone, after they've verified her, not through a reset link to a mailbox that may no longer be hers on file.

### SCOTT (2026-08-01T16:30)
give me the websites for the credit freezes

### CLAUDE (2026-08-01T16:30)
**Equifax:** equifax.com/personal/credit-report-services/credit-freeze
**Experian:** experian.com/freeze
**TransUnion:** transunion.com/credit-freeze

All three are free and each has to be done separately — freezing one doesn't touch the others. You'll create an account or verify by knowledge questions, and you'll get a PIN. Save it somewhere you can find later; you'll need it to lift the freeze if either of you applies for credit.

Do both of you.

Two more worth adding, both free and quick:

**Innovis** — innovis.com/personal/securityFreeze. The fourth bureau, often skipped, and some lenders pull from it.

**ChexSystems** — chexsystems.com. Blocks new *bank accounts* from being opened in your names. Given they're already inside a USAA membership, this one is more relevant than usual.

### SCOTT (2026-08-01T19:49)
Any idea where this is from?
[File uploaded: Screenshot 2026-08-01 at 3.46.02 PM]

### CLAUDE (2026-08-01T19:49)
The domain points to athenahealth's identity platform, which is used by medical practices for patient portals. This is a healthcare provider login for scott@watts.net, and the "Compromised Password" flag indicates the password was found in a known data breach.

I should clarify what this flag actually means — it doesn't mean the account was hacked today, just that this password exists in breach databases. Since he mentioned his passwords are mostly in LastPass with strong encryption, this one saved in Apple Passwords stands out as potentially reused or weaker. The practical next step is to change it and check Apple's Security Recommendations in Settings → Passwords to see if there are other flagged accounts he should address.

That's athenahealth — the shared login page for medical practice patient portals. Many providers use it, and the same email and password get you into your provider's athenahealth Patient Portal and the athenaPatient app. Whichever practice you saw is the one that runs on their platform. The "M" icon is just Apple's generic placeholder.

Note whose it is, though: **scott@watts.net**, not hers. This is your login, not Angie's.

On the red flag — Apple's "Compromised Password" means that password turned up in a known breach corpus, not that this account was accessed today. Different claim, and it long predates this morning. But it's real: that password is in circulation.

More useful than fixing this one entry: **Settings → Passwords → Security Recommendations** on your phone. Apple lists every saved credential that's breached, reused, or weak, in one screen. Given you found this by accident, there are probably others.

Which raises the thing worth sitting with — you told me your passwords are 60 random characters in LastPass. This one is in Apple Passwords, flagged, unchanged since January 2025. Some portion of your accounts isn't living up to the standard you described. Worth knowing which, especially today.

Change this one, and check that Security Recommendations list before you go back to her cleanup.
