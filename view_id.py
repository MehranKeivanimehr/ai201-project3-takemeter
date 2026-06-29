import json, sys
ids = sys.argv[1:]
data = json.load(open('soccer_comments/candidates_full.json',encoding='utf-8'))
found = {}
for label, items in data.items():
    for it in items:
        if it['id'] in ids:
            found[it['id']] = (label, it)
for i in ids:
    label, it = found.get(i, (None,None))
    if it:
        print(f"\n=== {i} (suggested {label}, score {it['score']}) ===")
        print(it['body'])
        print(it['permalink'])
    else:
        print(f"{i} not found")
