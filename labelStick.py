import json 
i = 0
with open('Resources/data/timviecnhanh.json', encoding = 'utf-8', mode = 'r') as f:
  data = json.load(f)
  for i in range(len(data)):
  # careerbuider
    # if data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[1]/div[2]/h1':
    #   data[i]['label'] = '0.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[2]/span':
    #   data[i]['label'] = '2.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[1]/div[2]/div':
    #   data[i]['label'] = '1.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[3]/p[2]':
    #   data[i]['label'] = '3.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[2]/p[2]/label':
    #   data[i]['label'] = '5.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[6]/div/p':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[1]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[2]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[3]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[4]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[5]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[6]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[6]/div/p[7]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[1]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[2]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[3]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[4]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[5]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[6]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[7]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[8]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[5]/ul/li[9]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[5]/ul/li[1]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[5]/ul/li[2]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[5]/ul/li[3]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[5]/ul/li[4]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[5]/ul/li[5]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[5]/ul/li[6]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[1]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[1]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[2]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[3]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[4]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[5]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[6]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[7]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[8]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[7]/div/p[9]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[3]/p[1]/b/a[1]':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[3]/p[1]/b/a[2]':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[3]/p[1]/b/a[3]':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[3]/p[1]/b/a[4]':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[3]/p[1]/b/a[5]':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[1]/p[2]/label':
    #   data[i]['label'] = '13.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[1]/p[1]/b/a':
    #   data[i]['label'] = '4.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[4]/div[1]/div[1]/div[4]/ul/li[1]/p[1]/b/a':
    #   data[i]['label'] = '4.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[4]/ul/li/span':
    #   data[i]['label'] = '19.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[5]/span':
    #   data[i]['label'] = '14.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[3]/div[5]/div[1]/div[1]/div[4]/ul/li[2]/p[1]':
    #   data[i]['label'] = '12.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[7]/span':
    #   data[i]['label'] = '15.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[9]':
    #   data[i]['label'] = '16.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[8]':
    #   data[i]['label'] = '17.0'
    # else:
    #   data[i]['label'] = '20.0'
    # 
    if data[i].get('xpath') == '/html/body/div[1]/div[2]/div[1]/h1/span':
      data[i]['label'] = '0.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/span':
      data[i]['label'] = '0.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/p/span/span':
      data[i]['label'] = '1.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[1]/li[1]/a/span/span':
      data[i]['label'] = '1.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[1]/li[3]/span/span[1]':
      data[i]['label'] = '5.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[1]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[2]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[3]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[4]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[5]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[6]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[7]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[8]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[9]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[10]':
      data[i]['label'] = '8.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[1]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[2]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[3]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[4]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[5]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[6]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[7]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[8]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[9]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[10]':
      data[i]['label'] = '9.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[1]/a/span':
      data[i]['label'] = '6.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[2]/a/span':
      data[i]['label'] = '6.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[3]/a/span':
      data[i]['label'] = '6.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[4]/a/span':
      data[i]['label'] = '6.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[5]/a/span':
      data[i]['label'] = '6.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[3]':
      data[i]['label'] = '13.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[4]/ul/li/a':
      data[i]['label'] = '4.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[4]/ul/li/span':
      data[i]['label'] = '19.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[5]/span':
      data[i]['label'] = '14.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[6]/span':
      data[i]['label'] = '12.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[7]/span':
      data[i]['label'] = '15.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[9]':
      data[i]['label'] = '16.0'
    elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[8]':
      data[i]['label'] = '17.0'
    else:
      data[i]['label'] = '20.0'
    #careerlink
    # if data[i].get('xpath') == '/html/body/div[1]/div[2]/div[1]/h1/span':
    #   data[i]['label'] = '0.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/div[2]/span':
    #   data[i]['label'] = '0.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[1]/li[1]/a/span/span':
    #   data[i]['label'] = '1.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[1]/p/span/span':
    #   data[i]['label'] = '1.0'
    # elif data[i].get('xpath') == '':
    #   data[i]['label'] = '2.0'
    # elif data[i].get('xpath') == '':
    #   data[i]['label'] = '3.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[4]/ul/li/a':
    #   data[i]['label'] = '4.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[1]/li[3]/span/span[1]':
    #   data[i]['label'] = '5.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[1]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[2]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[3]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[4]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[5]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[6]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[2]/ul/li[7]/a/span':
    #   data[i]['label'] = '6.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[7]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[9]':
    #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[10]':
    #   data[i]['label'] = '7.0'
    # # elif data[i].get('xpath') == '':
    # #   data[i]['label'] = '7.0'
    # # elif data[i].get('xpath') == '':
    # #   data[i]['label'] = '7.0'
    # # elif data[i].get('xpath') == '':
    # #   data[i]['label'] = '7.0'
    # # elif data[i].get('xpath') == '':
    # #   data[i]['label'] = '7.0'
    # # elif data[i].get('xpath') == '':
    # #   data[i]['label'] = '7.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[1]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[2]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[3]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[4]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[5]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[6]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[7]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[8]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[9]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/p[10]':
    #   data[i]['label'] = '8.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[1]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[2]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[3]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[4]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[5]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[6]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[7]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[8]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[9]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[10]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[11]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/div[3]/p[12]':
    #   data[i]['label'] = '9.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[6]/span':
    #   data[i]['label'] = '12.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[3]':
    #   data[i]['label'] = '13.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[5]/span':
    #   data[i]['label'] = '14.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[7]/span':
    #   data[i]['label'] = '15.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[9]':
    #   data[i]['label'] = '16.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[8]':
    #   data[i]['label'] = '17.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[3]/li[4]/span/span/span[4]':
    #   data[i]['label'] = '18.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[2]/li[4]/ul/li/span':
    #   data[i]['label'] = '19.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[3]/li[4]/span/span/span[1]':
    #   data[i]['label'] = '19.0'
    # elif data[i].get('xpath') == '/html/body/div[1]/div[2]/div[2]/div[1]/div/ul[3]/li[4]/span/span/span[2]':
    #   data[i]['label'] = '19.0'
    # else:
    #   data[i]['label'] = '20.0'
  
with open('Resources/data/data_train_timviecnhanh.json', mode = 'w',encoding = 'utf-8') as f:
  json.dump(data, f, ensure_ascii=False, indent = 4)
  f.close()
    
    

    
    


    


