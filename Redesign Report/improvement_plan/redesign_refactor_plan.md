# Redesign Page Refactor Plan
File: `report_redesign.html`

---

## Goal

The Redesign page is too long and repetitive. The same content (flows, Before/After comparisons) is presented twice — once organized by **task** (§04) and again organized by **pillar** (§05). The Trade-offs table, which is the most valuable section for the Simular team and CEO, is buried at the end.

The fix: collapse §04 + §05 into a single unified section, compress the Strategy section, and move Trade-offs up.

---

## New Page Structure

Replace the current 4-section layout (§03 Strategy → §04 Redesign → §05 Highlights → §06 Trade-offs) with this 3-section layout:

```
§03  Design Strategy       [compressed — visual-first]
§04  Two Core Flows        [merged §04 + §05 — one pass through content]
§05  Design Decisions      [moved up from §06]
```

---

## Section-by-Section Instructions

---

### §03 — Design Strategy (COMPRESS)

**Current:** Full paragraphs for each strategy card + HITL spectrum with long descriptions + highlighted design principle block.

**Change:** Keep the visual components (spectrum + 4 strategy cards) but strip out the body copy inside each card. Replace with one-line descriptions only.

**Specific edits:**

In each `.strategy-card`, remove the long paragraph. Keep only the title + subtitle + finding tags.

**Before (Legibility card):**
```
Legibility
Make the agent's plan readable before execution
Users should see what the agent intends to do, understand the scope, and identify potential risks — before a single action is taken. This builds calibrated trust (PAIR: Mental Models) rather than blind trust.
[F2] [F3]
```

**After:**
```
Legibility
Make the agent's plan readable before execution
[F2] [F3]
```

Apply the same trim to all 4 strategy cards (Boundary Awareness, Controllability, Progressive Disclosure).

**Also:** Remove the `.highlight` block (the "Design principle: Rather than forcing a fixed position..." paragraph) entirely. The HITL spectrum visual already communicates this.

---

### §04 — Two Core Flows (MERGE + RESTRUCTURE)

**Current:** §04 has Task 1 + Task 2 as separate task-framed sections with Before/After. §05 repeats the same content reframed by pillar, adding 4 new Before/After comparisons.

**Change:** Delete §05 entirely. Restructure §04 to fold in the relevant pillar information inline. Each flow gets one Before/After — not two.

**New §04 structure:**

```
Section heading:
  "04 — Two Core Flows"
  Subheading: "The redesign targets two failure modes. Each flow addresses one."

[Product Architecture tree] — keep as-is

[Flow 1 block]
  Label: FLOW 1
  Title: Plan Pre-Confirmation
  Pillar tags: Legibility · Progressive Disclosure    ← add these inline
  Root cause reference: Addresses Root Cause 1 + 2
  Before/After comparison: ONE pair only (keep the current §04 version, drop the §05 "Chat-first homepage" comparison)
  Design note (1–2 sentences): Why — the 10s review cost trades off against silent failure loops. Agent shifts to chat-first layout only after plan approved.

[Flow 2 block]
  Label: FLOW 2
  Title: Authentication Handoff
  Pillar tags: Boundary Awareness · Controllability   ← add these inline
  Root cause reference: Addresses Root Cause 3
  Before/After comparison: ONE pair only (keep §04 version, drop §05 "View/Control Mode" comparison)
  Design note (1–2 sentences): Auth contained in cloud panel. View-only default prevents accidental interference; interactive mode activates on agent-initiated handoff.

[Post-Completion block]
  Title: Post-Completion — Structured Delivery
  Keep as-is (this one is not duplicated elsewhere)
```

**Delete entirely from §05:**
- Pillar 1 — Legibility section (Chat-First to Split View Before/After)
- Pillar 2 — Boundary Awareness section ("Simular Computer" Mental Model Before/After)
- Pillar 3 — Controllability section (View/Control Mode Separation Before/After)
- Pillar 4 — Progressive Disclosure section (Task Progress Sidebar Before/After)

**Keep from §05 (move into §04 as a compact block after the two flows):**

The 4 Microinteraction cards (Takeover Dialog, Workspace Tabs, Auth Handoff Flow, Plan Modification). These are not duplicated elsewhere. Reformat as a 2×2 grid under a heading "Microinteraction Details". Remove the loose comparison block at the bottom of §05 (the two-column browser/post-completion captions — these are already covered in Flow 1/2).

---

### §05 — Design Decisions & Trade-offs (MOVE UP, MINOR EDITS)

**Current:** §06, placed last.

**Change:** Renumber to §05. Move it immediately after the Two Core Flows section. No content changes needed — the table is already good.

Optional: Add a one-sentence intro before the table:
> "Every decision here has a cost. These are the tradeoffs and the reasoning behind each call."

---

## What to Delete (Summary)

| Element | Location | Action |
|---|---|---|
| Long paragraphs inside each `.strategy-card` | §03 | Delete body copy, keep title + subtitle + tags |
| `.highlight` block (design principle paragraph) | §03 | Delete entirely |
| §05 Pillar 1 — Legibility (Chat-First Before/After) | §05 | Delete |
| §05 Pillar 2 — Boundary Awareness (VM naming Before/After) | §05 | Delete |
| §05 Pillar 3 — Controllability (View/Control Before/After) | §05 | Delete |
| §05 Pillar 4 — Progressive Disclosure (Sidebar Before/After) | §05 | Delete |
| Loose 2-col browser/post-completion caption block | §05 bottom | Delete |
| §05 section heading + intro copy | §05 | Delete (section is merged into §04) |

## What to Keep and Move (Summary)

| Element | From | To |
|---|---|---|
| 4 Microinteraction cards (Takeover Dialog, Workspace Tabs, Auth Handoff, Plan Modification) | §05 | End of new §04, as 2×2 grid |
| Trade-offs table + heading | §06 | Becomes new §05 |

## What to Add (Summary)

| Element | Where |
|---|---|
| Pillar tags (e.g. `Legibility · Progressive Disclosure`) | Inline in Flow 1 and Flow 2 headers |
| One-line design note per flow | Below each Before/After |
| Optional one-sentence intro before trade-offs table | Top of new §05 |

---

## Section Numbering After Changes

| Old | New | Title |
|---|---|---|
| §03 | §03 | Design Strategy |
| §04 | §04 | Two Core Flows ← merged with old §05 |
| §05 | — | Deleted (merged into §04) |
| §06 | §05 | Design Decisions & Trade-offs |

---

## Do Not Touch

- Nav bar and page header
- Hero section (title, subtitle, meta)
- Lightbox overlay
- Prototype CTA block
- Product Architecture tree
- Footer
- All CSS / JS
- `report_audit.html`, `design-evolution.html`, `report_prototype.html`
