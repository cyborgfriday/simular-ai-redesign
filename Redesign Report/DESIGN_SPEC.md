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

### Standard hero structure

```html
<header class="hero">
  <div class="container">
    <span class="badge">Page Label</span>
    <h1>Page Title<br><em>optional italic line</em></h1>
    <p class="subtitle">One to two sentence lead. Max ~60 characters wide.</p>
    <div class="meta">
      <span>YuRong Cheng</span>
      <span>April 2026</span>
    </div>
  </div>
</header>
```

### Badge rules (per page)

| Page | Badge text | Badge style |
|---|---|---|
| `report_audit.html` | `Simular SAI · Product Audit` | default (grey) |
| `report_redesign.html` | `Simular SAI · Redesign` | default (grey) |
| `report_prototype.html` | `Simular SAI · Live Prototype` | default (grey) |
| `design-evolution.html` | `Design Evolution` | **accent (orange)** — add class `accent` |

For the accent badge on `design-evolution.html`:
```html
<span class="badge accent">Design Evolution</span>
```
```css
.hero .badge.accent { color: var(--accent); border-color: rgba(180,83,9,0.25); }
```

### h1 italic `<em>` colour

- All pages: `<em>` inside `.hero h1` uses **`color: var(--accent)`** (orange).
- This applies to any italic fragment in the hero title (e.g. `Cards as <em>Communication</em>`).

```css
.hero h1 em { font-style: italic; color: var(--accent); }
```

### Full hero CSS

```css
.hero {
  padding: 96px 0 64px;
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  /* NO text-align: center */
}
.eyebrow, .hero .badge {
  font-family: var(--mono); font-size: 0.625rem; font-weight: 500;
  letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--text-dim); display: block; margin-bottom: 16px;
}
.hero .badge {
  display: inline-block; padding: 5px 14px; border-radius: 4px;
  border: 1px solid var(--border); letter-spacing: 1px; margin-bottom: 24px;
}
.hero .badge.accent { color: var(--accent); border-color: rgba(180,83,9,0.25); }
.hero h1 {
  font-family: var(--serif);
  font-size: clamp(2.25rem, 4vw + 0.5rem, 3.5rem);
  font-weight: 400; line-height: 1.12;
  margin-bottom: 20px; letter-spacing: -0.025em; color: var(--text);
}
.hero h1 em { font-style: italic; color: var(--accent); }
.hero .subtitle {
  font-size: 1rem; color: var(--text-dim);
  max-width: 560px; margin: 0 0 28px;
  font-weight: 400; line-height: 1.8;
}
.hero .meta { display: flex; gap: 28px; font-size: 0.8125rem; color: var(--text-dim); }
.hero .meta span { display: flex; align-items: center; gap: 6px; }
```

---

## 5. Navigation Bar (Shared — copy exactly)

All four pages must use this **identical** CSS and HTML. Do not modify the structure or font sizes.

### CSS (paste into `<style>`)

```css
.site-nav {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 200;
}
.site-nav .inner {
  max-width: 1160px; margin: 0 auto; padding: 0 32px;
  display: flex; align-items: center; justify-content: space-between;
  height: 52px;
}
.site-nav .brand {
  font-family: var(--mono); font-size: 0.625rem; font-weight: 500;
  letter-spacing: 0.8px; text-transform: uppercase;
  color: var(--text-dim); text-decoration: none; white-space: nowrap;
}
.site-nav .brand:hover { color: var(--text); }
.site-nav .pages { display: flex; gap: 2px; overflow-x: auto; scrollbar-width: none; }
.site-nav .pages::-webkit-scrollbar { display: none; }
.site-nav .pages a {
  white-space: nowrap; padding: 6px 14px; border-radius: 6px;
  text-decoration: none; color: var(--text-dim); font-size: 0.8125rem;
  font-weight: 450; transition: all 0.15s;
}
.site-nav .pages a:hover { color: var(--text); background: var(--surface2); }
.site-nav .pages a.active { color: var(--text); background: var(--surface2); font-weight: 550; }
@media (max-width: 600px) { .site-nav .brand { display: none; } .site-nav .inner { justify-content: center; } }
```

### HTML (paste just after `<body>`, before the hero)

Set the correct `class="active"` on the link that matches the current page.

```html
<nav class="site-nav">
  <div class="inner">
    <a class="brand" href="report_audit.html">Simular &mdash; Product Redesign</a>
    <div class="pages">
      <a href="report_audit.html" class="">Product Audit</a>
      <a href="report_redesign.html" class="">Redesign</a>
      <a href="design-evolution.html" class="">Design Evolution</a>
      <a href="report_prototype.html" class="">Live Prototype</a>
    </div>
  </div>
</nav>
```

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
| Hero padding | `56px 0 40px` |
| Between h2 and content | `8px` (h2 margin-bottom) |
| Between eyebrow and h2 | `8px` |
| Between h3 and content | `16px` |
| Between h4 and content | `10px` |
| Between cards in a list | `24px` |
| Card internal padding | `24px–32px` |

**`design-evolution.html` exception:** uses `.comp-section { padding: 52px 0 }` instead of `72px 0` — tighter layout for card-comparison display.

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
