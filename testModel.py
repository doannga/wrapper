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

def combineXpath(list_xpath):
    result = []
    labels = ['0.0', '1.0', '2.0', '3.0', '4.0', '5.0', '6.0', '7.0', '8.0', '9.0', '10.0', '11.0', '12.0', '13.0','14.0', '15.0', '16.0', '17.0', '18.0', '19.0']
    for label in labels:
        xpaths = [list_xpath[i][1] for i in range(len(list_xpath)) if list_xpath[i][0] == label]
        if len(xpaths) > 1:
            xpathMerge = ''
            xpathArray = []
            for xpath in xpaths:
                xpathArray.append([x for x in str(xpath).split('/') if x.strip()])
            xpathMerge = mergeXpaths(xpathArray)
            result.append([label, xpathMerge])
        elif len(xpaths) ==1:
            result.append([label, xpaths[0]])
    return result
def mergeXpaths(xpathArray):
    result = ''
    while len(xpathArray) > 0:
        tags = [i[0] for i in xpathArray if len(i) > 0]
        if len(tags) <= 1:
            break
        if len(tags) > 1:
            tagMostAppear = getMostAppear(tags)
            numberAppear = tags.count(tagMostAppear)
            if numberAppear > 1:
                xpathArray = [i for i in xpathArray if len(i) > 0 and i[0] == tagMostAppear]
                for x in xpathArray:
                    x.remove(tagMostAppear)
                result = result + '/' + tagMostAppear
            else:
                for x in xpathArray:
                    x.pop(0)
                stringCompare = compareStrings(tags)
                if stringCompare != '':
                    result = result + '/' + compareStrings(tags)
    return result
def compareStrings(strings):
    result = ''
    if len(strings) <= 1:
        return result
    minLength = min([len(i) for i in strings])
    if minLength == 0:
        return result
    while len(strings) > 0:
        characters = [c[0] for c in strings if len(c) > 0]
        characterMostAppear = getMostAppear(characters)
        numberAppear = characters.count(characterMostAppear)
        if numberAppear <= 1:
            break
        strings = [i for i in strings if len(i) > 0 and i[0] == characterMostAppear]
        strings = [i[1:] for i in strings]
        result = result + characterMostAppear
    result = result.replace('[','')
    return result
def getMostAppear(strings):
    result = max(strings, key = strings.count)
    return result
def wrapper( list_xpath_content, list_mismath_attribute):

    classifier = pickle.load(open('trained_model/svm_model.pk','rb'))

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
        xpath = list_xpath_content[i][0] + '/text()'
        # print(xpath)
        if result_label[j] in list_mismath_attribute:
            result1.append([result_label[j],xpath])
        j+=1
    print(result1)
    result = combineXpath(result1)
    return result

if __name__ == '__main__':
    list_xpath_content = []
    with open('./DataTest/xpath_content1.json') as f:
        data = json.load(f)
    for item in data:
        list_xpath_content.append([item['xpath'], item['content']])
    list_mismath_attribute = ['14.0']
    result = wrapper(list_xpath_content,list_mismath_attribute)
    print(result)
    with open('Result/result2.text',encoding = 'utf-8', mode = 'w') as f:
        json.dump(result, f,indent = 4, ensure_ascii=False)
