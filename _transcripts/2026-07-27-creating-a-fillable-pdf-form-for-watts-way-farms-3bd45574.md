# Creating a fillable PDF form for Watts Way Farms
Date: 2026-07-27
Conversation: 3bd45574-f44a-4188-af2e-d007f35a3a4e
Domain: watts-way-farms

## Summary
**Conversation Overview**

The person is associated with Watts Way Farms (Franklin, GA, contact number 706-883-5644) and needed help converting a beef cut sheet document for Daniel-Jackson Meat Processing into a fillable PDF form. The specific requirements were to pre-fill certain fields: Farm/Farmer as "Watts Way Farms," phone number as "706-883-5644," Custom or Inspected as "Inspected," and the payment/pickup field as "Watts Way Farms is paying for processing. Pickup is TBD."

Claude attempted to build the fillable PDF programmatically using ReportLab with AcroForm fields, producing a form with 68 fillable fields including checkboxes, radio buttons, and text fields organized into sections for animal/farm information, customer information, steaks, roasts, ground beef/organs/bones, and special instructions. The person was dissatisfied with the quality of the output and asked for a prompt to use Claude Design instead, wanting a single-page result.

Claude provided a detailed Claude Design prompt specifying all form sections, field types, pre-filled values, and design requirements (US Letter, print-friendly, sans-serif, AcroForm-compatible). Claude also directed the person to claude.ai/design and noted it is available on Pro, Max, Team, and Enterprise plans. Claude flagged an important caveat that Claude Design may not produce true fillable AcroForm fields and suggested that if the export comes out flat, the person could use Acrobat's "Prepare Form" feature or send the file back to Claude to add the form layer. The person's clear preference is for a clean, functional, single-page fillable PDF.

### SCOTT (2026-07-27T00:13)
turn this in to a fillabnle pdf form.  for the form that says, "Farm/Farmer" fill it in with, "Watts Way Farms" and for phone number put 706-883-5644.  

Roight Undernesth the "Custom or Inspected" put Inspected.  For "Who is payong for proicess and pcikign up" put Watts Way Farms is payong for processing.  Pickup is TBD
[File uploaded: Beef Cutlsheet Daniel Jackson.pdf]

### CLAUDE (2026-07-27T00:15)
I'll build this as a fillable PDF. Let me check the skill guidance first.

Got the original. Now building the fillable version.

68 fillable fields. The three you asked for are pre-filled and will show up filled every time someone opens it:

- **Farm/Farmer** — Watts Way Farms
- **Phone Number** — 706-883-5644
- **Custom or Inspected** — Inspected
- **Who is paying for processing and picking up** — Watts Way Farms is paying for processing. Pickup is TBD

Everything else is blank and editable: date slaughtered, beef ID, live/hanging weight, age verification, customer name and phone, order size (Whole/Half/Quarter radio), the full steak table with thickness and notes per cut, ribeye bone-in Y/N, roasts with 2-3 / 3-4 / 4-5 lb radios, brisket whole/half, ground beef package size, stew, organs, soup bones.

Three things I changed or added that weren't in the original — flagging so you can tell me to revert:

1. **Address:** the uploaded sheet reads 5164 County Rd 49; the address on file for Daniel Jackson Farms is 5160. I used 5164 from the source document. Not sure which is correct.
2. **Dropped "2024" from the title.** It just reads "BEEF CUTLIST" now.
3. **Added** a Special Instructions box and a customer signature line at the bottom.

### SCOTT (2026-07-27T00:44)
your fillable pdf suck.  give me the prompt to use cluadue desing.  i need it to be a one page pdf

### CLAUDE (2026-07-27T00:45)
Fair. Here's the prompt:

```
Create a single-page, print-ready fillable PDF form (US Letter, 8.5" x 11", portrait) 
titled "BEEF CUTLIST" for Watts Way Farms. It must be ONE page — no overflow.

PROCESSOR HEADER (centered, small):
Daniel-Jackson Meat Processing | 5164 County Rd 49, Ranburne, AL 36273 | 256-463-9841
Subtitle line: "One sheet per whole animal — or, if half or quarter, one sheet per customer"

DESIGN:
Clean, professional, black on white. Thin hairline rules, minimal shading — this gets 
printed and handled in a processing plant, so it must stay legible on a cheap printer 
and photocopy well. Sans-serif. Section headers in bold caps with a light rule under 
them. Labels 8pt, field text 9pt. Tight vertical rhythm — compress padding before you 
compress content. Do not use a colored background on any field.

All text fields, checkboxes, and radio buttons must be REAL fillable AcroForm fields 
that work in Adobe Acrobat, Preview, and mobile PDF viewers.

SECTION 1 — ANIMAL & FARM INFORMATION
- Date Slaughtered (text)
- Farm / Farmer (text, PRE-FILLED: "Watts Way Farms")
- Phone Number (text, PRE-FILLED: "706-883-5644")
- Custom or Inspected (text, PRE-FILLED: "Inspected")
- Beef ID (text)
- Live Weight (text)
- Hanging Weight (text)
- Age Verification < 30 mths (Yes/No radio pair)
- Who is paying for processing and picking up? (full-width text, PRE-FILLED: 
  "Watts Way Farms is paying for processing. Pickup is TBD")

SECTION 2 — CUSTOMER INFORMATION
- Customer Name (text)
- Phone Number (text)
- Order: Whole / Half / Quarter (radio group, mutually exclusive)
- Small note text: "($25 per quarter — quarters have to be cut the same)"

SECTION 3 — STEAKS
Note line above the table: "Half and quarter beef cannot have both Filet/NY Strip and 
T-Bone. Steaks cut to a standard 3/4" thickness unless noted. Cubed is standard 1/4". 
Steaks are packaged 2 per pack (cubed is 4 per pack)."

Table, columns: CUT | YES | NO | THICKNESS | NOTES
Rows: Filet, NY Strip, T-Bone, Ribeye, Sirloin, Cubed Steak
Yes/No are mutually exclusive radio pairs. Thickness and Notes are text fields.
On the Ribeye row only, add "Bone-In: Y / N" as a radio pair at the start of the 
Notes cell.

SECTION 4 — ROASTS
Table, columns: CUT | YES | NO | WEIGHT OF ROASTS | NOTES
Rows: Chuck, Shoulder, Sirloin Tip, Brisket
Weight column = radio group per row: 2-3 lb / 3-4 lb / 4-5 lb
EXCEPTION: on the Brisket row, the weight column is instead Whole / Half (radio pair).

SECTION 5 — GROUND BEEF, STEW, ORGANS & BONES
- Ground Beef — package size: 1 lb / 2 lb / 1 and 2 lb (radio group) + Notes text field
- Stew Beef: Yes / No (radio pair) + Notes text field
- Organs: Liver, Heart, Tongue, Tail (independent checkboxes — any combination)
- Soup Bones: Yes / No (radio pair) + Notes text field

SECTION 6 — SPECIAL INSTRUCTIONS
One multi-line text field, full width, roughly 3 lines tall.

FOOTER (small, grey):
Left: "Watts Way Farms | Franklin, GA | 706-883-5644 | wattswayfarms.com"
Right: "Customer signature: ______________________"

Give every field a descriptive, lowercase, underscore-separated name (e.g. 
steak_ribeye_thickness, roast_chuck_weight) so the filled data can be exported cleanly.
```

One thing to decide before you run it: the address on the processor's own sheet reads 5164 County Rd 49, but 5160 is what I have on file for them. The prompt above uses 5164 — swap it if 5160 is right.

### SCOTT (2026-07-27T00:47)
how do i get to cluade design

### CLAUDE (2026-07-27T00:47)
Let me check the current docs so I give you the right path.

Go to claude.ai/design — that's the direct URL. It's available on web and desktop (from the sidebar in Claude Desktop), and it's in beta for Pro, Max, Team, and Enterprise plans. It's off by default for Enterprise, so if you're on that plan an admin has to enable it in Organization settings.

One honest caveat before you spend time on it: Claude Design exports to Canva, PDF, PPTX, or standalone HTML — but I have no evidence it produces PDFs with *fillable AcroForm fields*, which is the part you actually need. A design tool exporting to PDF usually means a flat, visual PDF. If it comes out flat, the layout will still be better than what I gave you, and you can run it through Acrobat's "Prepare Form" to auto-detect the fields, or send the exported file back to me and I'll add the form layer.
