import tracker_operator as op
from pathlib import Path


def snap():
    return {'delivery':{'total':20,'integrated':0,'remaining':20,'running':2,'ready':3,'awaiting_review':5,'waiting_capacity':4,'waiting_dependency':6,'accepted':2,'integrating':1},'control':{'total':30,'integrated':25},'current_phase':'F0','release':{'ready':False}}


def test_delivery_not_control_completion():
    s=op.render(snap(),{'label':'BUILDING'}, {'effective':12,'running':9}, True)
    assert '0/20' in s and '25/30' not in s
    assert 'Integration checks' in s and 'ETA: unknown' in s
    assert 'review backlog' in s.lower()


def test_unknown_state_not_ready():
    s=op.render(None,{'label':'UNKNOWN'},{},False)
    assert 'State unavailable' in s and 'RELEASE READY' not in s


def test_collapses_diagnostics_and_preserves_office():
    doc='<html><head></head><body><main><section class="panel bot-office">BOTS</section><section>PROVIDER LOG</section></main></body></html>'
    s=op.apply(doc,snap(),{'label':'BUILDING'},{},True)
    assert s.index('id="operator-summary"') < s.index('PROVIDER LOG')
    assert '<summary>Build details' in s and '<summary>Live bot office' in s
    assert s.count('BOTS') == 1


def test_live_renderer_wires_operator_snapshot():
    assert 'tracker_operator.apply(doc, snapshot, product_status, free_runtime, ctl_up)' in Path('tracker_build.py').read_text()
