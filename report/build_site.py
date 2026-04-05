#!/usr/bin/env python3
"""
Build multi-page report site with consistent navigation.
Pages:
  1. Product Audit    (Context + Audit)
  2. Redesign         (Strategy + Redesign + Highlights + Tradeoffs)
  3. Design Evolution (links to design-evolution.html)
  4. Live Prototype   (prototype link + tips)
"""

with open('Simular_SAI_Redesign_Report_BACKUP.html', 'r', encoding='utf-8') as f:
    content = f.read()

# ── Extract CSS from original ──────────────────────────────────────────────
style_start = content.find('<style>') + len('<style>')
style_end = content.find('</style>')
original_css = content[style_start:style_end]

# ── Extract JS ────────────────────────────────────────────────────────────
js_start = content.find('<script>') + len('<script>')
js_end = content.find('</script>')
original_js = content[js_start:js_end]

# ── Extract each section ──────────────────────────────────────────────────
def extract_section(src, section_id):
    start = src.find(f'<section id="{section_id}">')
    end = src.find('</section>', start) + len('</section>')
    return src[start:end] if start != -1 else ''

context   = extract_section(content, 'context')
audit     = extract_section(content, 'audit')
strategy  = extract_section(content, 'strategy')
redesign  = extract_section(content, 'redesign')
highlights = extract_section(content, 'highlights')
tradeoffs = extract_section(content, 'tradeoffs')

# ── Shared pieces ──────────────────────────────────────────────────────────
FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com">\n<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=DM+Sans:ital,opsz,wght@0,9..40,300..700;1,9..40,300..700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">'

SITE_NAV_CSS = """
/* ── Site-level page nav ── */
.site-nav {
  background: var(--surface);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 200;
}
.site-nav .inner {
  max-width: 920px; margin: 0 auto; padding: 0 32px;
  display: flex; align-items: center; justify-content: space-between;
  height: 52px;
}
.site-nav .brand {
  font-family: var(--mono); font-size: 11px; font-weight: 500;
  letter-spacing: 0.8px; text-transform: uppercase;
  color: var(--text-dim); text-decoration: none; white-space: nowrap;
}
.site-nav .brand:hover { color: var(--text); }
.site-nav .pages {
  display: flex; gap: 2px; overflow-x: auto; scrollbar-width: none;
}
.site-nav .pages::-webkit-scrollbar { display: none; }
.site-nav .pages a {
  white-space: nowrap; padding: 6px 14px; border-radius: 6px;
  text-decoration: none; color: var(--text-dim); font-size: 13px;
  font-weight: 450; transition: all 0.15s;
}
.site-nav .pages a:hover { color: var(--text); background: var(--surface2); }
.site-nav .pages a.active {
  color: var(--text); background: var(--surface2); font-weight: 550;
}
@media (max-width: 600px) {
  .site-nav .brand { display: none; }
  .site-nav .inner { justify-content: center; }
}
"""

LIGHTBOX_HTML = """<div class="lightbox-overlay" id="lightbox" onclick="closeLightbox()">
  <button class="lightbox-close" onclick="closeLightbox()" aria-label="Close">&times;</button>
  <img id="lightbox-img" src="" alt="">
</div>"""

JS_BLOCK = f"<script>{original_js}</script>"

FOOTER = """<footer>
  <div class="container">
    <p>&copy; 2026 YuRong C. &mdash; Simular Redesign Proposal</p>
  </div>
</footer>"""

def site_nav(active_page):
    """Generate site-level nav with the active page highlighted."""
    pages = [
        ('/report', 'Product Audit'),
        ('/report/redesign', 'Redesign'),
        ('/report/design_revolution', 'Design Evolution'),
        ('/report/prototype_intro', 'Live Prototype'),
    ]
    links = '\n    '.join(
        f'<a href="{href}" class="{"active" if href == active_page else ""}">{label}</a>'
        for href, label in pages
    )
    return f"""<nav class="site-nav">
  <div class="inner">
    <a class="brand" href="/report">Simular SAI &mdash; Product Design</a>
    <div class="pages">
    {links}
    </div>
  </div>
</nav>"""

def build_page(title, active_page, body_content, extra_css=''):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
{FONTS}
<style>
{original_css}
{SITE_NAV_CSS}
{extra_css}
</style>
</head>
<body>

{LIGHTBOX_HTML}

{site_nav(active_page)}

{body_content}

{FOOTER}

{JS_BLOCK}
</body>
</html>"""


# ══════════════════════════════════════════════════════════════════
# PAGE 1: PRODUCT AUDIT
# ══════════════════════════════════════════════════════════════════
audit_hero = """<header class="hero">
  <div class="container">
    <span class="badge">Product Audit</span>
    <h1>UX Audit &amp;<br>Product Context</h1>
    <p class="subtitle">End-to-end usability audit of Simular SAI — mapping friction points, trust gaps, and failure modes in an autonomous computer-use agent.</p>
    <div class="meta">
      <span>YuRong C.</span>
      <span>April 2026</span>
      <span>Simular AI &mdash; Product Design</span>
    </div>
  </div>
</header>"""

audit_body = audit_hero + '\n' + context + '\n' + audit

audit_html = build_page(
    'Product Audit — Simular SAI',
    '/report',
    audit_body
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(audit_html)
print("✓ index.html")


# ══════════════════════════════════════════════════════════════════
# PAGE 2: REDESIGN
# ══════════════════════════════════════════════════════════════════
redesign_hero = """<header class="hero">
  <div class="container">
    <span class="badge">Design Solution</span>
    <h1>Design Strategy &amp;<br>Redesign Solution</h1>
    <p class="subtitle">Strategic redesign of human-in-the-loop interaction — building trust, transparency, and user control into autonomous agent workflows.</p>
    <div class="meta">
      <span>YuRong C.</span>
      <span>April 2026</span>
      <span>Simular AI &mdash; Product Design</span>
    </div>
  </div>
</header>"""

redesign_body = redesign_hero + '\n' + strategy + '\n' + redesign + '\n' + highlights + '\n' + tradeoffs

redesign_html = build_page(
    'Redesign — Simular SAI',
    '/report/redesign',
    redesign_body
)

with open('redesign.html', 'w', encoding='utf-8') as f:
    f.write(redesign_html)
print("✓ redesign.html")


# ══════════════════════════════════════════════════════════════════
# PAGE 3: LIVE PROTOTYPE
# ══════════════════════════════════════════════════════════════════
prototype_body = """<header class="hero">
  <div class="container">
    <span class="badge">Interactive Prototype</span>
    <h1>Live Prototype</h1>
    <p class="subtitle">Try the redesigned human-in-the-loop interaction flow. The prototype simulates the agent's execution plan confirmation, mid-task interruption, and sign-in handoff states.</p>
    <div class="meta">
      <span>YuRong C.</span>
      <span>April 2026</span>
      <span>Simular AI &mdash; Product Design</span>
    </div>
    <div style="margin-top: 40px;">
      <a href="https://simular-redesign.yrcheng.tech/prototype" target="_blank" style="display:inline-flex;align-items:center;gap:10px;padding:14px 32px;background:var(--text);color:var(--bg);text-decoration:none;border-radius:8px;font-weight:600;font-size:15px;transition:all 0.2s;letter-spacing:0.2px;">Open Prototype &#8594;</a>
    </div>
  </div>
</header>

<section style="border-bottom: 1px solid var(--border);">
  <div class="container">
    <h2><span class="num">→</span> Before You Try</h2>
    <p class="section-intro">The prototype is a realistic simulation of the redesigned SAI interface. Here are a few things to know before jumping in.</p>

    <div class="card-grid">
      <div class="card">
        <span class="label label-amber">Navigation</span>
        <h4>Use the Action Buttons</h4>
        <p>The prototype is driven by the action buttons in the interface — <strong>Approve Plan</strong>, <strong>Modify Plan</strong>, and <strong>Sign In</strong>. These advance the interaction states in sequence.</p>
      </div>
      <div class="card">
        <span class="label label-blue">Quick Tip</span>
        <h4>Skip Animations</h4>
        <p>Each state has a short transition animation. To skip directly to the next state, press <strong>Space</strong> or click the action button again during the animation. You can also hold <strong>Shift</strong> to reduce motion.</p>
      </div>
      <div class="card">
        <span class="label label-green">Scope</span>
        <h4>What's Simulated</h4>
        <p>This prototype covers the key human-in-the-loop touchpoints: <strong>task submission</strong>, <strong>execution plan review</strong>, <strong>mid-task modification</strong>, and <strong>authentication handoff</strong>. Agent task execution itself is not simulated.</p>
      </div>
      <div class="card">
        <span class="label label-purple">Demo Mode</span>
        <h4>Locked Interactions</h4>
        <p>Some interactions are marked <strong>Demo Only</strong> — these are intentionally disabled to keep the prototype focused. They represent real features in the design spec but are not interactive here.</p>
      </div>
    </div>

    <div class="highlight" style="margin-top: 36px;">
      <p><strong>Suggested flow:</strong> Submit a task → Review the execution plan → Try modifying a step → Approve the updated plan → Handle the sign-in handoff. Each step is designed to surface a different human-in-the-loop design decision.</p>
    </div>

  </div>
</section>"""

prototype_html = build_page(
    'Live Prototype — Simular SAI',
    '/report/prototype_intro',
    prototype_body
)

with open('prototype_intro.html', 'w', encoding='utf-8') as f:
    f.write(prototype_html)
print("✓ prototype_intro.html")


# ══════════════════════════════════════════════════════════════════
# UPDATE root vercel.json (single source of truth for routing)
# ══════════════════════════════════════════════════════════════════
import json

root_vercel = {
    "cleanUrls": True,
    "rewrites": [
        { "source": "/", "destination": "/prototype/AgentUI.html" },
        { "source": "/prototype", "destination": "/prototype/AgentUI.html" },
        { "source": "/prototype/:path*", "destination": "/prototype/AgentUI.html" }
    ]
}

with open('../vercel.json', 'w') as f:
    json.dump(root_vercel, f, indent=2)
    f.write('\n')
print("✓ ../vercel.json updated")

print("\nDone! Files created:")
print("  index.html           → /report")
print("  redesign.html        → /report/redesign")
print("  design_revolution.html → /report/design_revolution")
print("  prototype_intro.html → /report/prototype_intro")
