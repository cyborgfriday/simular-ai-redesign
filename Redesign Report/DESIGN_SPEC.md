# Redesign Report — Design Consistency Spec

> **Baseline reference:** `report_audit.html` (most refined version)
> **For agents:** Apply these rules to your assigned page. Do not deviate.

---

## 1. Typography Scale

```css
body {
  font-family: var(--sans);
  font-size: 1rem;          /* NOT 15.5px — use 1rem */
  line-height: 1.75;
  font-weight: 400;
}

/* Page title — MUST use clamp() for responsiveness */
.hero h1 {
  font-family: var(--serif);
  font-size: clamp(2.25rem, 4vw + 0.5rem, 3.5rem);
  font-weight: 400;
  line-height: 1.12;
  letter-spacing: -0.025em;
}

/* Section heading */
h2 {
  font-family: var(--serif);
  font-size: 1.875rem;
  font-weight: 400;
  line-height: 1.2;
  letter-spacing: -0.025em;
}

/* Sub-section heading */
h3 {
  font-family: var(--serif);
  font-size: 1.375rem;
  font-weight: 400;
  line-height: 1.3;
  letter-spacing: -0.02em;
  margin: 48px 0 16px;
}

/* Label / item heading */
h4 {
  font-size: 1.0625rem;
  font-weight: 650;
  line-height: 1.4;
  letter-spacing: -0.01em;
  margin: 24px 0 10px;
}

/* Section lead text */
.section-intro {
  font-size: 1.125rem;
  color: var(--text-dim);
  line-height: 1.8;
  max-width: 72ch;
  margin-bottom: 44px;
}

/* Body paragraph */
p {
  font-size: 1rem;
  line-height: 1.75;
  margin-bottom: 16px;
}

/* Small label / eyebrow */
.eyebrow, .badge {
  font-family: var(--mono);
  font-size: 0.625rem;    /* ~10px */
  font-weight: 500;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--text-dim);
}

/* Nav links */
nav a {
  font-size: 0.8125rem;   /* 13px — use rem not px */
  font-weight: 450;
}
```

**Rule:** Only these 7 text styles are allowed. No other custom font sizes.

---

## 2. Colour Tokens

```css
:root {
  --bg: #faf9f7;
  --surface: #ffffff;
  --surface2: #f3f2ef;
  --border: #e8e6e1;
  --text: #2c2c2c;
  --text-dim: #7a7670;
  --accent: #b45309;
  --accent-light: #92400e;
  --accent-bg: rgba(180,83,9,0.04);
  --green: #15803d;
  --amber: #a16207;
  --red: #b91c1c;
  --blue: #1d4ed8;
  --radius: 10px;
}
```

**Rule:** Use only these tokens. No hardcoded hex colours in components.

---

## 3. Layout

```css
.container {
  max-width: 1160px;
  margin: 0 auto;
  padding: 0 32px;
}

section {
  padding: 72px 0;
  border-bottom: 1px solid var(--border);
}
section:last-of-type { border-bottom: none; }
```

---

## 4. Hero / Page Header

**Alignment: LEFT-aligned** (not centered — reference `design-evolution.html`)

```html
<div class="hero">
  <div class="container">
    <p class="eyebrow">Simular SAI · Redesign Report</p>
    <h1>Page Title<br><em>optional italic line</em></h1>
    <p class="subtitle">One to two sentence lead. Max ~60 characters wide.</p>
  </div>
</div>
```

```css
.hero {
  padding: 96px 0 64px;
  border-bottom: 1px solid var(--border);
  /* NO text-align: center */
}
.hero .subtitle {
  font-size: 1rem;
  color: var(--text-dim);
  max-width: 560px;
  line-height: 1.8;
}
```

---

## 5. Navigation Bar

All four pages share the same nav structure and sizing:

```css
nav {
  position: sticky; top: 0; z-index: 100;
  background: rgba(250,249,247,0.92);
  backdrop-filter: blur(16px);
  border-bottom: 1px solid var(--border);
  padding: 10px 0;
}
nav .container { display: flex; gap: 4px; overflow-x: auto; scrollbar-width: none; }
nav a {
  white-space: nowrap;
  padding: 5px 12px;
  border-radius: 6px;
  text-decoration: none;
  color: var(--text-dim);
  font-size: 0.8125rem;
  font-weight: 450;
  transition: all 0.2s;
}
nav a:hover { color: var(--text); background: var(--surface2); }
```

Nav links must include cross-page navigation to all four report pages.

---

## 6. When to Use Cards vs Lists

### Use a card (bordered box with background) ONLY when:
- Comparing discrete options side-by-side (e.g. HITL vs HOTL vs HOOL)
- Showing a before/after with visual screenshot
- The item has 3+ distinct sub-fields that need visual grouping
- The item is interactive (clickable, expandable)

### Use a simple list (`<ul>`, `<ol>`) when:
- Listing 3+ items of the same type
- Showing steps, criteria, or observations
- The content is primarily text with no sub-fields
- You would otherwise stack identical-looking cards vertically

**Rule:** If you can express it in a bullet list, use a bullet list. Cards are for content that genuinely benefits from visual separation.

---

## 7. When to Use Grid vs Single Column

### Use grid ONLY when:
- Items are visually comparable side-by-side (before/after, version comparisons)
- Items are short and roughly equal in length
- There are exactly 2–3 items per row

### Use single column when:
- Items have unequal lengths (grid creates awkward whitespace)
- Content is narrative / sequential
- Mobile readability matters
- In doubt — default to single column

**Rule:** Do not use grid for more than 3 columns. Prefer `display: flex; flex-direction: column; gap: 24px` over grid for lists of cards.

---

## 8. Spacing System

| Context | Value |
|---|---|
| Section padding (top/bottom) | `72px 0` |
| Hero padding | `96px 0 64px` |
| Between h2 and content | `10px` (h2 margin-bottom) |
| Between h3 and content | `16px` |
| Between h4 and content | `10px` |
| Between cards in a list | `24px` |
| Card internal padding | `24px–32px` |

---

## 9. Fonts to Load

All pages must load the same font stack:

```html
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,400;0,600;1,400&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

Variables:
```css
--serif: 'Lora', 'Georgia', serif;
--sans:  'DM Sans', -apple-system, BlinkMacSystemFont, system-ui, sans-serif;
--mono:  'JetBrains Mono', 'SF Mono', monospace;
```

---

## 10. Per-page Agent Instructions

| Page | Branch | Focus |
|---|---|---|
| `report_audit.html` | `agent/audit` | Already cleanest — align hero to left, verify type scale |
| `report_prototype.html` | `agent/prototype` | Fix h1 to clamp(), left-align hero, fix h2/h3/h4 sizes, reduce unnecessary cards |
| `report_redesign.html` | `agent/redesign` | Fix h1 to clamp(), left-align hero, fix h2/h3/h4 sizes, convert card-stacks to lists where appropriate |
| `design-evolution.html` | *(no separate branch)* | Hero already left-aligned ✅; keep container width at 1340px (intentional — needed for side-by-side card display); align type scale only |
