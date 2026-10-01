"""Operator-first presentation over the existing authoritative snapshot."""
import html
import re


def render(snapshot, status, runtime, controller_up):
    esc = lambda value: html.escape(str(value))
    if not snapshot:
        return '<section class="panel operator-summary"><h1>State unavailable</h1><p>Authoritative product state could not be read.</p></section>'
    d = snapshot['delivery']
    n = lambda key: int(d.get(key, 0))
    if not controller_up:
        reason = 'Controller offline. Construction cannot advance until supervision restores it.'
    elif runtime.get('paused') or runtime.get('safe'):
        reason = 'Dispatch paused or in safety mode. Resolve the safety condition before resuming.'
    elif n('accepted') or n('integrating'):
        reason = f"Integration checks are the next gate: {n('accepted')} accepted awaiting integration; {n('integrating')} integrating. Accepted is not yet delivered."
    elif n('awaiting_review'):
        reason = f"Review backlog: {n('awaiting_review')} delivery items need independent verdicts before integration. Provider traffic alone cannot clear this gate."
    elif n('waiting_capacity'):
        reason = f"Provider capacity is limiting {n('waiting_capacity')} delivery items. Available free routes are retried automatically."
    else:
        reason = 'Implementation and acceptance are progressing. Only integrated delivery increases completion.'
    cells = [('Delivered', f"{n('integrated')}/{n('total')}", 'integrated product items only'),
             ('Product work running', n('running'), 'excludes planning and diagnosis'),
             ('Review backlog', n('awaiting_review'), 'independent verdict required'),
             ('Ready to build', n('ready')+n('todo')+n('changes_requested'), 'dependencies and capacity separate'),
             ('Waiting for capacity', n('waiting_capacity'), 'provider or worker limits'),
             ('Dependency blocked', n('waiting_dependency'), 'prerequisites unfinished')]
    cards = ''.join(f'<div class="truth-stat"><span>{esc(k)}</span><b>{esc(v)}</b><small>{esc(note)}</small></div>' for k,v,note in cells)
    return f'''<section class="panel operator-summary" id="operator-summary">
    <div class="truth-head"><div><div class="runtime-label">EMPIRIUM STUDIO · BUILD OVERVIEW</div><div class="truth-status">{esc(status['label'])}</div><div class="truth-reason">Phase {esc(snapshot.get('current_phase') or 'unassigned')} · ETA: unknown — no reliable integrated-delivery estimate</div></div><div class="truth-warning"><b>Worker activity is not delivery completion</b><span>Queue counts are product-only. Bots include reviewers and support work.</span></div></div>
    <div class="operator-metrics">{cards}</div><div class="operator-blocker"><b>What is slowing delivery?</b><p>{esc(reason)}</p><small>Release remains gated. Expand Build details for affected tasks and failed checks. Provider/account settings are unchanged.</small></div>
    <div class="note">Free workers: <b>{esc(runtime.get('running','unknown'))}/{esc(runtime.get('effective','unknown'))}</b> effective capacity · {esc(runtime.get('mode','unknown route'))} · evidence refreshed with this page</div></section>'''


def apply(doc, snapshot, status, runtime, controller_up):
    """Keep diagnostics available without competing with delivery truth."""
    match = re.search(r'<main>(.*?)</main>', doc, re.S)
    if not match:
        raise ValueError('tracker main content missing')
    content = match.group(1)
    # Guard against duplicate wrapping in an already-updated renderer.
    if 'id="operator-summary"' in content:
        return doc
    office = re.search(r'<section class="panel bot-office".*?</section>', content, re.S)
    office_html = office.group(0) if office else ''
    if office:
        content = content[:office.start()] + content[office.end():]
    summary = render(snapshot,status,runtime,controller_up)
    body = summary + '<details class="panel setup-history"><summary>Live bot office — activity, not completion</summary>'+office_html+'</details>'
    body += '<details class="panel setup-history"><summary>Build details and provider diagnostics — roadmap, tasks, gates and history</summary>'+content+'</details>'
    css = '''<style>.operator-summary{border-color:rgba(88,166,255,.5)}.operator-metrics{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1px;background:var(--line)}.operator-metrics .truth-stat{background:var(--panel);padding:20px}.operator-blocker{padding:20px;border-top:1px solid var(--line)}.operator-blocker p{font-size:14px;line-height:1.6;color:var(--fg2)}.operator-blocker small{color:var(--dim)}.setup-history>summary{font-size:13px;color:var(--fg2);line-height:1.5}@media(max-width:640px){.operator-metrics{grid-template-columns:repeat(2,minmax(0,1fr))}}</style>'''
    return (doc[:match.start()]+'<main>'+body+'</main>'+doc[match.end():]).replace('</head>',css+'</head>',1)
