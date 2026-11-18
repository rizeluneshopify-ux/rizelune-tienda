# Publica el exfoliante y el aceite facial y activa los packs de rutina.
# Uso: python3 datos/publicar-nuevos.py          (simulación: no cambia nada)
#      python3 datos/publicar-nuevos.py --ya     (lo hace de verdad)
import json, re, os, subprocess, sys, tempfile, datetime
sys.path.insert(0, '/tmp/claude-0/-home-user/5897ab18-cc48-56a9-8458-06822eddabe6/scratchpad/aud')
from tr import q
YA = '--ya' in sys.argv
ROOT = '/root/tiendas/dfqp9i-am'; os.chdir(ROOT)
ENV = dict(os.environ, NODE_USE_ENV_PROXY='1', NODE_NO_WARNINGS='1')
THEME = ['--store', 'dfqp9i-am.myshopify.com', '--theme', '210260099402']
SERUM = 'gid://shopify/Product/16124464922954'
EXF = 'gid://shopify/Product/16152349638986'
OIL = 'gid://shopify/Product/16152368742730'
FILES = ['config/settings_data.json', 'templates/index.json', 'templates/collection.json']

def strip(t): return json.loads(re.sub(r'^\s*/\*.*?\*/', '', t, flags=re.S))
def header(t):
    m = re.match(r'^\s*/\*.*?\*/\s*', t, flags=re.S); return m.group(0) if m else ''

# 0) lo publicado tiene que coincidir con lo local
tmp = tempfile.mkdtemp()
subprocess.run(['shopify', 'theme', 'pull', *THEME] + sum([['--only', f] for f in FILES], []) + ['--path', tmp], env=ENV, capture_output=True)
for f in FILES:
    if strip(open(os.path.join(tmp, f)).read()) != strip(open(f).read()):
        sys.exit(f'ALTO: {f} publicado es distinto del local. Revisar antes de seguir.')
print('0 ok: tema publicado = local')

# 1) productos activos
for pid in (EXF, OIL):
    d = q('query($id:ID!){ product(id:$id){ title status } }', {'id': pid})['product']; print('1', d['title'], d['status'], '→ ACTIVE')
    if YA:
        r = q('mutation U($p: ProductUpdateInput!){ productUpdate(product:$p){ product{ status } userErrors{ message } } }', {'p': {'id': pid, 'status': 'ACTIVE'}}, mut=True)
        assert not r['productUpdate']['userErrors'], r

# 2) ajustes de packs
raw = open('config/settings_data.json').read(); d = strip(raw); c = d['current']
c.update({'rz_ritual1_activo': True, 'rz_ritual1_b': 'exfoliante-capilar-romero-menta', 'rz_ritual1_precio': '52,99',
          'rz_ritual2_activo': True, 'rz_ritual2_b': 'aceite-facial-bakuchiol', 'rz_ritual2_precio': '56,99',
          'rz_ritual3_activo': True, 'rz_ritual3_b': 'exfoliante-capilar-romero-menta', 'rz_ritual3_c': 'aceite-facial-bakuchiol', 'rz_ritual3_precio': '89,98'})
print('2', {k: v for k, v in c.items() if k.startswith('rz_ritual')})
if YA: open('config/settings_data.json', 'w').write(header(raw) + json.dumps(d, ensure_ascii=False, indent=2))

# 3) bloques de packs visibles y sin lista de espera fija
for f, sec in (('templates/index.json', 'packs'), ('templates/collection.json', 'catalogo')):
    raw = open(f).read(); t = strip(raw); s = t['sections'][sec]
    for b in ('r1', 'r2', 'r3'): s['blocks'][b].pop('disabled', None)
    s['settings']['lista_espera'] = False
    print('3', f, sec, [k for k, b in s['blocks'].items() if b.get('disabled')], s['settings'])
    if YA: open(f, 'w').write(header(raw) + json.dumps(t, ensure_ascii=False, indent=2))

# 4) subir
if YA:
    r = subprocess.run(['shopify', 'theme', 'push', *THEME, '--allow-live'] + sum([['--only', f] for f in FILES], []), env=ENV, capture_output=True, text=True)
    print('4 push', 'ERROR' if 'rror' in r.stdout + r.stderr else 'ok')

# 5) descuentos (si no existen ya)
existing = q('{ discountNodes(first:50){ nodes{ id discount{ __typename ... on DiscountAutomaticBxgy{ title status } } } } }')['discountNodes']['nodes']
titles = {n['discount'].get('title') for n in existing}
M = open('datos/disc-ritual.graphql').read()
start = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
for title, b in (('Pack Ritual Raíz · sérum + exfoliante', EXF), ('Pack Pelo y Piel · sérum + aceite facial', OIL)):
    if title in titles: print('5', title, 'ya existe'); continue
    v = {'title': title, 'startsAt': start, 'a': SERUM, 'b': b, 'amount': '7.99'}
    print('5 crear', v)
    if YA:
        r = q(M.split('\n', 2)[2] if M.startswith('#') else M, v, mut=True); print('  ', r)
print('HECHO' if YA else 'SIMULACIÓN OK (nada cambiado)')
