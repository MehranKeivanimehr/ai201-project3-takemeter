import json, re

# Selected comment IDs per label (real public r/soccer comments from pullpush.io archive)
selected = {
    'Evidence-Based Take': [
        'mt3nkr9','mrya68k','msu0oom','mt0biqq','msx83il','msg6cd2','mscdke0',
        'mt37ioq','msu3jdp','msxbgrn','ms2k472','msfouun','msimgpe','mt00e0l',
        'mszxt7p','msz4ztn','msl4tr6','msegg92','ms81ccx','msxyp2t','mt42f1w',
        'msxuati','mt071mw','mszyqfu','mszp7m8','mst8hef','mt42tcf','mt0e5mj'
    ],
    'Bold Opinion / Hot Take': [
        'mpjdxfw','msqjsy4','msthnrp','mt45rf9','msxu306','ms36yoo','mpg9sfh',
        'msow72z','mscpduv','msiraq2','mrwuc5f','mqik5s2','mpq0a7z','mpk1tst',
        'mqpjzef','mt41t0e','mstaexr','mt3pio2','mqosqpr','ms7rg2e','mrmk21l',
        'mt3tphk','mqot5ep','mrthm8r','ms80yby','mslfzlu','ms6ljaf','msrkn6r'
    ],
    'Emotional Reaction': [
        'msy0omv','msvdb4m','mt19z6b','mg8yiit','msz7e2h','msv1uwd','mstp8a8',
        'msub5rh','mstzcky','msm2qx8','msyzju7','mszhakx','msu8ml7','mt3yhdk',
        'mstpx8r','mstosf8','msj5s29','msy94jk','msu24kz','mstom0d','mscj0vw',
        'mstpr84','ms2f5p0','msrn3pn','mstxtvg','mshoj5v','msxwy40','msu66nr'
    ]
}

extra_notes = {
    'mrya68k': 'Uses second-leg shot/possession/xG stats to explain Arteta\'s view, then adds a personal conclusion.',
    'msz4ztn': 'Discusses a methodological way to normalize defensive-progression stats rather than making a direct match claim.',
    'mt42f1w': 'References underlying stats without enumerating them.',
    'mszyqfu': 'Rebuts an xG-based claim by citing specific match events (post hits, saves, foul).',
    'msxu306': 'Includes a YouTube link as an illustrative example.',
    'mg8yiit': 'Primarily emotional but also asserts Alisson is the best GK in the world.',
    'mszhakx': 'Primarily vents frustration; includes substantive team/recruitment critique.',
    'msm2qx8': 'Emotional appeal built around a rhetorical comparison.',
    'msiraq2': 'Opinion about TV/media coverage rather than an on-field soccer claim.',
    'mrthm8r': 'Predictive hot take with minimal supporting evidence.',
    'mpq0a7z': 'Predictive hot take.',
    'mqpjzef': 'Competition-format opinion rather than a player/team evaluation.',
    'mqosqpr': 'Competition-format opinion.',
    'mqot5ep': 'Competition-format opinion.',
    'mpg9sfh': 'Cultural/opinion take about post-title celebrations.',
    'mscpduv': 'Includes a hyperbolic jersey-bet as part of the hot take.',
}

def clean(text):
    # Pullpush occasionally replaces curly quotes/apostrophes/ellipses with U+FFFD
    text = text.replace('\ufffd', "'")
    # collapse multiple whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text

data = json.load(open('soccer_comments/candidates_full.json', encoding='utf-8'))
by_id = {}
for label, items in data.items():
    for it in items:
        by_id[it['id']] = it

dataset = []
for label, ids in selected.items():
    for cid in ids:
        it = by_id.get(cid)
        if not it:
            print('missing', cid)
            continue
        note = f"Real public r/soccer comment retrieved via the pullpush.io Reddit archive."
        if cid in extra_notes:
            note += " " + extra_notes[cid]
        dataset.append({
            'text': clean(it['body']),
            'label': label,
            'notes': note
        })

with open('takemeter_dataset.json','w',encoding='utf-8') as f:
    json.dump(dataset, f, ensure_ascii=False, indent=2)

print('total', len(dataset))
from collections import Counter
print(dict(Counter(d['label'] for d in dataset)))
