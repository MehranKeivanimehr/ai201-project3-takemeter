import json, re, html, os
from collections import defaultdict

files = {
    'Evidence-Based Take': ['xg.json','stats.json','tactical.json','possession.json'],
    'Bold Opinion / Hot Take': ['overrated.json','underrated.json','unpopular.json','hottake.json'],
    'Emotional Reaction': ['fucking_love.json','crying.json','heartbroken.json','sohappy.json'],
}

def clean_body(text):
    if not text:
        return ''
    return html.unescape(text)

def is_valid(body):
    if not body:
        return False
    b = body.strip()
    if b in ('[removed]', '[deleted]'):
        return False
    if len(b) < 30 or len(b) > 1200:
        return False
    if b.startswith('>'):
        return False
    # remove very URL-heavy
    if b.count('http') > 2:
        return False
    return True

all_comments = {}
label_pool = defaultdict(list)
for label, flist in files.items():
    for fn in flist:
        path = os.path.join('soccer_comments', fn)
        try:
            data = json.load(open(path, encoding='utf-8'))
        except Exception as e:
            print('error', fn, e)
            continue
        for c in data.get('data', []):
            cid = c.get('id')
            body = clean_body(c.get('body',''))
            if not is_valid(body):
                continue
            if cid in all_comments:
                continue
            all_comments[cid] = c
            label_pool[label].append({
                'id': cid,
                'body': body,
                'score': c.get('score',0),
                'permalink': c.get('permalink',''),
                'author': c.get('author',''),
                'created_utc': c.get('created_utc',''),
                'source_query': fn,
            })

def evidence_score(body):
    s = body.lower()
    terms = ['xg','expected goals','possession','passes','touches','shots','tackle','press','defensive','offensive','stat','metric','data','tactical','formation','build-up','progressive','ppda','xga','npxg']
    return sum(1 for t in terms if t in s)

def hot_score(body):
    s = body.lower()
    terms = ['overrated','underrated','best','worst','greatest','ever','should','unpopular opinion','hot take','clearly','no way','not even','biased','agenda','in my opinion','i think']
    return sum(1 for t in terms if t in s)

def emo_score(body):
    s = body.lower()
    terms = ['love','hate','cry','crying','heart','happy','sad','devastated','fuck','shit','unbelievable','emotional','feel','feeling','tears','joy','proud','disgusting','amazing','incredible','wtf','omg']
    return sum(1 for t in terms if t in s)

scorers = {
    'Evidence-Based Take': evidence_score,
    'Bold Opinion / Hot Take': hot_score,
    'Emotional Reaction': emo_score,
}

output = {}
for label, candidates in label_pool.items():
    sc = scorers[label]
    candidates.sort(key=lambda c: (sc(c['body']), c['score']), reverse=True)
    output[label] = candidates[:100]

with open('soccer_comments/candidates_full.json','w',encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print('wrote candidates_full.json')
