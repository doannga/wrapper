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
def wrapper( list_xpath_content, list_mismath_attribute):

    classifier = pickle.load(open('trained_model/logistic_model.pk','rb'))

    # tf-idf
    vectorizer = pickle.load(open(settings.VECTOR_EMBEDDING,'rb'))
    data_features = []
    i = 0
    result = []
    for i in range(len(list_xpath_content)):
        data_features.append(' '.join(NLP(text=list_xpath_content[i][1].get_words_feature()))
        features = vectorizer.transform(data_features)
        result_label = classifier.predict(features)
        xpath = list_xpath_content[i][0]
        if result_label in list_mismath_attribute:
            result.append([result_label,xpath])

    return result

# if __name__ == '__main__':
#     result = testModel('./Resources/data/data_empty.json')
#     with open('Result/result1.text',encoding = 'utf-8', mode = 'w') as f:
#         json.dump(result, f,indent = 4, ensure_ascii=False)
