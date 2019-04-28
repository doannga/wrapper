from lxml import etree
import json
import simplejson
import os
i = 0
content_array = []
for item in os.listdir('Resources/careerlink'):
	item_dir = f'Resources/careerlink/{item}'
	with open(item_dir, encoding = 'utf8', mode = 'r') as f:
		root = etree.HTML(f.read())
		f.close()
	tree = etree.ElementTree(root)
	for node in root.iter():
		path = tree.getpath(node)
		content = tree.xpath(''+path+'/text()')
		contents = ''.join(content).strip()
		if 'header' not in path and 'div[3]/ul/li' not in path and 'footer' not in path and 'nav' not in path and 'option' not in path and 'table' not in path and contents.strip() != '' and 'function' not in contents and '{' not in contents and  'body' in path:
			content_array.append({
								'xpath': path,
								'content': contents,
								'label': ''
								})
with open('./Resources/data/careerlink.json','w') as file:
	json.dump(content_array,file,ensure_ascii=False, indent = 4, sort_keys = True,separators=(',', ': '))
