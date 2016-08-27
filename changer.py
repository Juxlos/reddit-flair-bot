import json
with open('flair_list.json') as source:
    data = json.load(source)
k = data['flairs']
t = []
for flair in k:
    j = flair.split('-')
    j[0] = '{0}flair'.format(j[0])
    t.append('-'.join(j))
data['flairs'] = t
def jsonwrite():
    with open('flair_list.json','w') as data_file:
        json.dump(data,data_file, indent=4, separators=(',', ': '))
jsonwrite()
