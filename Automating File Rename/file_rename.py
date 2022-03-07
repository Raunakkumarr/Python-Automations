import os
folderPath = 'E:\Pioneer photo\selected photos\\'
fileSequence = 1

for filename in os.listdir(folderPath):
    #if filename.endswith('jpg'):
    os.rename(folderPath+filename, folderPath+"selected"+str(fileSequence)+'.jpg')
    fileSequence +=1
