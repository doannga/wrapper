import numpy as np
from random import randint
import os
import json
import settings
import pickle
from processFile import FileReader, FileStore
from preProcessData import FeatureExtraction ,NLP
from pyvi import ViTokenizer
from sklearn.svm import LinearSVC
from gensim import corpora, matutils
from sklearn.metrics import classification_report
from argparse import ArgumentParser
import os.path

def get_json(filePath):
    data = []
    i = 0
    with open (filePath,encoding='utf8', mode = 'r') as f:
        data_ = json.load(f)
    for i in range(len(data_)):
        if data_[i].get('content') != "" and 'option' not in data_[i].get('xpath') and 'script' not in data_[i].get('xpath'):
            content = data_[i].get('content')
            label = data_[i].get('label')
            xpath = data_[i].get('xpath')
            data.append({
                "content": content,
                "label": label,
                "xpath": xpath
                })
    # json.dump(data, open('./Result/text1.txt','w', encoding= 'utf-8'), indent = 4)
    return data
# def testModel(filePath):
#     #  Read input data
#     new_data = get_json(filePath)
#     classifier = pickle.load(open('trained_model/logistic_model.pk','rb'))

#     # tf-idf
#     vectorizer = pickle.load(open(settings.VECTOR_EMBEDDING,'rb'))
#     data_features = []
#     i = 0
#     result = []
#     for i in range(len(new_data)):
#         data_features.append(' '.join(NLP(text=new_data[i].get('content')).get_words_feature()))
#         features = vectorizer.transform(data_features)
#         result_label = classifier.predict(features)
#         xpath = new_data[i].get('xpath')
#         result.append({
#             'xpath': xpath,
#             'label': result_label[i],
#             'content': new_data[i].get('content')
#         })
#     return result
def isDifferentPosition(array, stringNeedCompare, position, attr):
	for i in array:
		if stringNeedCompare != i[attr][position]:
			return True
	return False

def getSameString(strings):
	result = ''
	if len(strings) > 0:
		lastPosition = -1
		firstString = strings[0]
		for s in strings:
			if len(s) < len(firstString):
				firstString = s

		for i in range(len(firstString)):
			for s in strings:
				if s[i] != firstString[i] :
					lastPosition = i
					break
		if lastPosition > -1:
			result = firstString[:lastPosition]
			result = result.replace('[','')
	return result
def combineXpath(list_xpath):
    result = []
    labels = ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0','14.0', '15.0', '16.0', '17.0', '18.0', '19.0']
    for label in labels:
        xpaths = []
        item = 0
        for item in range(len(list_xpath)):
            if list_xpath[item][0] == label:
                index = next((j for j, it in enumerate(xpaths) if it['xpath'] == list_xpath[item][1]), -1)
                if index == -1:
                    xpathItems = list_xpath[item][1].split('/')
                    xpathItems = [x for x in xpathItems if x.strip()]
                    xpaths.append({
						'xpath': list_xpath[item][1],
						'xpathItems': xpathItems
					})
        if len(xpaths) > 1:
            combineXpath = ''
            minLength = min([len(i['xpathItems']) for i in xpaths])
            for i in range(minLength):
                stringNeedCompare = xpaths[0]['xpathItems'][i]
                if isDifferentPosition(xpaths, stringNeedCompare, i, 'xpathItems'):
                    differentPosition =	i
                    break
            if differentPosition != -1:
                for i in range(differentPosition):
                    combineXpath = combineXpath + '/' + xpaths[0]['xpathItems'][i]
                lastStrings = []
                if differentPosition < minLength:
                    for xpath in xpaths:
                        lastStrings.append(xpath['xpathItems'][differentPosition])
                    sameString = getSameString(lastStrings)
                    if sameString != '':
                        combineXpath = combineXpath + '/' + sameString
            result.append([label,combineXpath])
        if len(xpaths) == 1:
            result.append([label, xpaths[0]['xpath']])

    return result


def wrapper( list_xpath_content, list_mismath_attribute):

    classifier = pickle.load(open('trained_model/logistic_model.pk','rb'))

    # tf-idf
    vectorizer = pickle.load(open(settings.VECTOR_EMBEDDING,'rb'))
    data_features = []
    i = 0
    result1 = []
    j = 0
    for i in range(len(list_xpath_content)):
        # print(list_xpath_content[i][1])
        data_features.append(' '.join(NLP(text=list_xpath_content[i][1]).get_words_feature()))
        features = vectorizer.transform(data_features)
        result_label = classifier.predict(features)
        # print(result_label)
        index_label = enumerate(result_label)
        xpath = list_xpath_content[i][0]
        # print(xpath)
        if result_label[j] in list_mismath_attribute:
            result1.append([result_label[j],xpath])
        j+=1
    print(result1)
    result = combineXpath(result1)
    return result

if __name__ == '__main__':
    list_xpath_content = []
    with open('./dataTest.json') as f:
        data = json.load(f)
    for item in data:
        list_xpath_content.append([item['xpath'], item['content']])
    list_mismath_attribute = ['5.0','8.0']
    result = wrapper(list_xpath_content,list_mismath_attribute)
    print(result)
    with open('Result/result1.text',encoding = 'utf-8', mode = 'w') as f:
        json.dump(result, f,indent = 4, ensure_ascii=False)
