import json, sys
ids = ['msy0omv','msvdb4m','mt19z6b','mg8yiit','msz7e2h','msv1uwd','mstp8a8','msub5rh','mstzcky','msm2qx8','msyzju7','mszhakx','msu8ml7','mt3yhdk','mstpx8r','mstosf8','msj5s29','msy94jk','msu24kz','mstom0d','lr2f1xb','mstpr84','ms2f5p0','msrn3pn','mstxtvg','mshoj5v','msxwy40','msu66nr']
data=json.load(open('soccer_comments/candidates_full.json',encoding='utf-8'))
out=[]
for label in data:
    for it in data[label]:
        if it['id'] in ids:
            out.append(it)
with open('soccer_comments/view_selected.txt','w',encoding='utf-8') as f:
    for it in out:
        f.write(f"\n=== {it['id']} ===\n")
        f.write(it['body']+'\n')
