# Random 20-character password generator
Date: 2026-08-01
Conversation: 9644963f-c569-4c6a-b91f-9473e5ddfdb3
Domain: skip

## Summary
**Conversation Overview**

The person made a brief, practical request: generate a random 20-character string containing uppercase letters, lowercase letters, and special characters. Claude used a Python script with the `secrets` module to produce a cryptographically random result meeting all three character-type requirements. The output delivered was `kI#Shxa{QddoX[<Ubl{n`. Claude noted that digits were intentionally excluded since they were not requested, and offered to regenerate with digits included or with specific special characters removed if the target system has character restrictions.

### SCOTT (2026-08-01T13:59)
give me a 20 character randonm.  upper lower and special chars

### CLAUDE (2026-08-01T13:59)
I need to generate a random 20-character password with uppercase, lowercase, and special characters. The user didn't explicitly mention digits, but I should probably include them anyway since that's standard for a strong password. I'll use bash to ensure genuine randomness rather than relying on pattern-matching.

`kI#Shxa{QddoX[<Ubl{n`

20 chars, mixed case + specials, no digits (you didn't ask for them — say the word if you want digits added or specific characters excluded for a system that chokes on them).
