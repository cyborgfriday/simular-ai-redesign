# Audit Page — Complete Refactor Plan
File: `report_audit.html`

---

## Overview of All Changes

1. **Summary block** — flip order, problems first
2. **§00 Scope of Testing** — delete entirely
3. **§01 Who This Is For** — replace full persona card with lightweight 3-line profile strip; replace The Task block with user story layout
4. **§02 Journey** — trim body paragraphs
5. **§03 Blockers** — trim Blocker 02

---

## 1. Summary Block — Restructure (problem-first)

Inside `<section id="summary">`, reorder the three `<h4>` blocks.

**Current order:**
1. What was tested
2. Key problems found
3. Redesign direction

**New order:**
1. Key problems found ← move to top
2. What was tested ← move to second, replace text
3. Redesign direction ← unchanged

**New text for "What was tested" (replace entire paragraph):**

> Tested against a non-technical SMB founder running a multi-step research and delivery task — the scenario that best surfaces where human-in-the-loop design breaks down.

---

## 2. §00 Scope of Testing — Delete Entirely

Delete the entire `<section id="overview">` block including all its contents.

---

## 3. §01 Who This Is For — Replace Persona Card

**Current:** Full persona card with 3-column grid (Goals / Frustrations / Tech Profile) + Scenario footer block.

**Replace the entire persona card `<div>` with this lightweight strip:**

```html
<div style="border: 1px solid var(--border); border-radius: var(--radius); padding: 20px 24px; margin: 24px 0; background: var(--surface);">

  <!-- Identity row -->
  <div style="display: flex; align-items: baseline; gap: 12px; margin-bottom: 16px;">
    <span style="font-family: var(--serif); font-size: 1.25rem; color: var(--text);">Julia Marsh</span>
    <span style="font-family: var(--mono); font-size: 0.625rem; color: var(--text-dim); text-transform: uppercase; letter-spacing: 0.6px;">Proto-Persona · SMB Founder · Singapore</span>
  </div>

  <!-- Profile row -->
  <div style="display: flex; gap: 24px; margin-bottom: 16px; flex-wrap: wrap;">
    <span style="font-size: 0.8125rem; color: var(--text-dim);">Non-technical</span>
    <span style="font-size: 0.8125rem; color: var(--text-dim);">First-time agent user</span>
    <span style="font-size: 0.8125rem; color: var(--text-dim);">Cautious with permissions</span>
    <span style="font-size: 0.8125rem; color: var(--text-dim);">Google Workspace · Canva · ChatGPT (casual)</span>
  </div>

  <!-- Tension row -->
  <div style="display: flex; gap: 32px; flex-wrap: wrap;">
    <span style="font-size: 0.8125rem; color: var(--text);"><span style="color: var(--green);">↗</span> Just delegate it and get a result</span>
    <span style="font-size: 0.8125rem; color: var(--text);"><span style="color: var(--red);">↘</span> Don't make me manage it</span>
  </div>

</div>
```

**Also update** the section intro paragraph (just before the persona card) to:

> Technical users have scripting, APIs, and no-code alternatives. SAI's real opportunity is with users who don't. That's who this audit tests for.

(This text already exists — just confirm it's unchanged.)

**After the persona strip, replace everything from `<h3>The Task — and Why I Chose It</h3>` to the end of the section** with this new user story block:

```html
<h3>The Task — and Why I Chose It</h3>

<p style="font-size: 0.875rem; color: var(--text-dim); margin-bottom: 16px; line-height: 1.7;">
  Julia has a product curation call on Thursday. She opens SAI and types:
</p>

<!-- Prompt quote -->
<div style="border-left: 2px solid var(--border); padding: 14px 20px; margin: 0 0 20px; background: var(--surface2); border-radius: 0 var(--radius) var(--radius) 0;">
  <p style="font-size: 0.875rem; font-style: italic; color: var(--text); margin: 0; line-height: 1.8;">
    "I am launching a home decor curation brand in Singapore, focusing on Nordic and Japanese home accessories (e.g., vases, small lighting, stools, stationery — no large furniture). Please research brands popular in Singapore and trending in Europe/Japan, curate 20 items with market analysis and pricing, then compile everything into a Google Sheet report I can use for import decisions."
  </p>
</div>

<!-- Why this task + chain -->
<p style="font-size: 0.875rem; color: var(--text-dim); margin-bottom: 12px; line-height: 1.7;">
  This task isn't a single capability test — it chains four steps, each requiring the agent to earn trust differently. Any break in the chain means no usable output.
</p>

<p style="font-family: var(--mono); font-size: 0.75rem; color: var(--text-dim); letter-spacing: 0.3px;">
  <span style="color: var(--blue);">Research</span>
  <span style="margin: 0 8px; color: var(--border);">→</span>
  <span style="color: var(--blue);">Judgement</span>
  <span style="margin: 0 8px; color: var(--border);">→</span>
  <span style="color: var(--red);">Auth handoff ⚠</span>
  <span style="margin: 0 8px; color: var(--border);">→</span>
  <span style="color: var(--amber);">Delivery</span>
</p>
```

**Delete** the old `<div class="card">` task quote block and the 4-column flex grid entirely.

---

## 4. §02 How the Task Unfolded — Trim Body Paragraphs

For each journey step, the caption (the italic or dimmed text below the screenshot placeholder) already tells the story. The body paragraphs restate the same thing. Trim as follows:

**Initial State**
- Keep: heading + first caption sentence only
- Delete: second sentence ("The suggested tasks give no indication of how the agent handles...")

**Start**
- Keep: heading + caption
- Delete: body paragraph entirely

**First friction point**
- Keep: caption
- Trim body to: "It's unclear whether the task has paused or is still running in parallel."
- Delete: rest of body

**Authentication handoff**
- Keep: caption
- Delete: body paragraph entirely

**Incomplete output**
- Keep: caption
- Trim body to: "SAI produced the sheet without images and gave no explanation for the omission."
- Delete: rest of body

**Loss of visibility**
- Keep: heading + caption
- Delete: body paragraph entirely

**Wrong environment**
- Keep: caption
- Trim body to: "The agent had no way to signal what it needed or surface the right credential interface."
- Delete: rest of body

**No recovery**
- Keep: caption
- Trim body to: "The agent had no mechanism to detect the denial, no fallback, and no way to tell the user what it needed to proceed."
- Delete: rest of body

**Hard stop**
- Keep: quoted message caption + one sentence: "No summary of what was accomplished, no partial output, no path forward except starting over."
- Delete: rest of body

**Second attempt** — keep entirely unchanged.

---

## 5. §03 The UX Blockers — Trim Blocker 02

**Blocker 02** currently has two paragraphs. The second paragraph re-narrates the auth loop story the reader just saw in §02.

Delete the second paragraph of Blocker 02 entirely. It starts with:
> "This caused a concrete failure: when authentication was needed..."

Keep only the first paragraph (the one about the single stream of log entries).

Blockers 01 and 03 — unchanged.

---

## 6. §04 Two Problems Worth Solving — No Changes

Leave entire section unchanged.

---

## Do Not Touch

- Hero section (h1, subtitle, meta)
- §03 Blockers 01 and 03
- §04 entire section
- Nav, footer, all CSS, all JS, lightbox overlay
