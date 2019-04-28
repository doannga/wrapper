import json
data = []
i = 0
with open ('./Resources/data/1.json',encoding='utf8', mode = 'r') as f:
	data_ = json.load(f)
print(data_[0])
print(len(data_))
for i in range(len(data_)):
  print(type(data_[i].get('xpath')))
  if data_[i].get('content') != "" and 'option' not in data_[i].get('xpath') :
    content = data_[i].get('content')
    label = data_[i].get('label')
    xpath = data_[i].get('xpath')
    data.append({
				"content": content,
				"label": label,
				"xpath": xpath
			})
print(data)
json.dump(data, open('./Result/test1.txt','w'), indent = 4)
