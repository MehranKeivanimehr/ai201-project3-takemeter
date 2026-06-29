import json, sys
sys.stdout = open('soccer_comments/emotional_snippets.txt','w',encoding='utf-8')
data=json.load(open('soccer_comments/candidates_full.json',encoding='utf-8'))
for i,it in enumerate(data['Emotional Reaction'][:80], start=1):
    print(i, it['id'], it['score'], it['body'][:220].replace('\n',' '))
