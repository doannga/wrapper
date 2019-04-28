import json
import os
class DataLoader(object):
	def __init__(self, dataPath):
		self.dataPath = dataPath
	def get_json(self):
		data = []
		with open (dataPath,encoding='utf8', mode = 'r') as f:
			data_ = json.load(f)
			for item in data_["data"]:
				for cont in item["item"]:
					if cont['label'] != "":
						content = cont["content"]
						label = cont['label']
						xpath = cont['xpath']
						data.append({
							"content": content,
							"label": label,
							"xpath": xpath
						})
		return data
	
