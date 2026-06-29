import json
ids=['mpjdxfw','msqjsy4','msthnrp','mt45rf9','msxu306','ms36yoo','mpg9sfh','msow72z','mscpduv','msiraq2','mrwuc5f','mqik5s2','mpq0a7z','mpk1tst','mqpjzef','mt41t0e','mstaexr','mt3pio2','mqosqpr','ms7rg2e','mrmk21l','mt3tphk','mqot5ep','mrthm8r','ms80yby','mslfzlu','ms6ljaf','msrkn6r']
data=json.load(open('soccer_comments/candidates_full.json',encoding='utf-8'))
out=[]
for label in data:
    for it in data[label]:
        if it['id'] in ids:
            out.append(it)
with open('soccer_comments/view_hot.txt','w',encoding='utf-8') as f:
    for it in out:
        f.write(f"\n=== {it['id']} score {it['score']} ===\n")
        f.write(it['body']+'\n')
