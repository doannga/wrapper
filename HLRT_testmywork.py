from os import listdir
from os.path import isfile, join

import textwrap

#path with html files
path = "./Resources/test_mywork.html"

#open files from path
file = open(path, 'r')
#read page
page = file.readlines()
#format lines without \n and \t
page = [textwrap.dedent(line.rstrip()) for line in page] 
print(page)
#close page
file.close()
#add page to pages

#print(page)

# HLRT = [] #HLRT is void at the begining

# i = 0
# while i < len(page) and page[i]!="<div class="col-md-7" data-v-e0e9ca9c>": #skip first occurrece of head
#     i += 1
# print(i)
# while i < len(page) and page[i]!="</body>": #l1 is before next tail
#     print(i)
#     if "<h3>" in page[i]: #extract atributes from lk to rk
#         LR = [] #LR is void at the begining
#         print(page[i])
#         LR.append(page[i].replace("<h3>", "").replace("</h3>",""))
#         i+=1
#         while i < len(page) and page[i]!="</div>": # while end of rk
#             print(i)
#             if "<li>" in page[i]:
#                 print(page[i])
#                 li = page[i].split("</b>")
#                 LR.append(li[1].replace("</li>", ""))
#             i += 1
#         HLRT.append(LR) #save tuples
#     else:
#         i += 1

# print(HLRT)