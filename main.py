#.info discribes introdution to vdieo
#.xml discribes danmu;

import os

def mp4Transform(srcPath:str,dstPath:str):
    fileRead = open(srcPath, "rb")
    fileWrite = open(dstPath, "wb")
    size = os.path.getsize(srcPath)
    fileRead.seek(3)
    data = fileRead.read(size - 3)
    fileWrite.write(data)
    fileWrite.flush()
    fileWrite.close()
    fileRead.close()

def getInfo(srcPath:str,dstPath:str):
    fileRead = open(srcPath,'r',encoding='UTF-8')
    fileWrite = open(dstPath,'a+',encoding='UTF-8')

    data = fileRead.read()
    dataSplited = data.split('"')

    partNoFlag = dataSplited.index('PartNo')
    partNoIndex = partNoFlag + 2
    partNameFlag = dataSplited.index('PartName')
    partNameIndex = partNameFlag + 2
    timeFlag = dataSplited.index('TotalTime')
    timeIndex = timeFlag + 2

    partNo = 'Part No. is :'+dataSplited[partNoIndex]+'\n'
    partName = 'Part name is :'+dataSplited[partNameIndex]+'\n'
    time = 'Part time is :'+dataSplited[timeIndex]+'\n'+'\n'

    fileWrite.write(partNo)
    fileWrite.write(partName)
    fileWrite.write(time)

    fileRead.close()
    fileWrite.close()

def makedir(srcPath:str,dstPath:str):
    fileRead = open(srcPath, 'r', encoding='UTF-8')

    data = fileRead.read()
    dataSplited = data.split('"')

    titleFlag = dataSplited.index('Title')
    titleIndex = titleFlag + 2
    title = dataSplited[titleIndex]

    dirName = dstPath+'/'+title
    folder = os.path.exists(dirName)
    if not folder:
        os.mkdir(dirName)
    else:
        print("There is already a same folder.")

    fileRead.close()
    return dirName

def fileTransform(srcPath:str,dirNum:int):
    videoPaths = []
    infoPaths = []
    subFolderPaths = []
    for i in range(dirNum):
        subFolderPaths.append(srcPath+'/'+str(i+1))
    for i in range(dirNum):
        currentFiles =[]
        currentPath = subFolderPaths[i]
        for m,p,q in os.walk(currentPath):
            currentFiles = q
        for j in currentFiles:
            if j.find('.mp4') != -1:
                videoPaths.append(currentPath+'/'+j)
            if j.find('.info') != -1:
                infoPaths.append(currentPath+'/'+j)
    return videoPaths,infoPaths,subFolderPaths

def work():
    print("Please input vedio root dirctory:")
    rootPath = input()
    print("Please input number of videos:")
    videoNum = int(input())
    videoPaths,infoPaths,subFolderPaths = fileTransform(rootPath,videoNum)
    print("Please input dircotry you want put transformed videos in:")
    inputDstPath = input()
    folder = os.path.exists(inputDstPath)
    if not folder:
        os.mkdir(inputDstPath)
    dstPath = makedir(infoPaths[0],inputDstPath)
    infoPath = dstPath + '/information.html'
    for i in videoPaths:
        mp4Transform(i,dstPath+'/'+str(videoPaths.index(i))+'.mp4')
    for i in infoPaths:
        getInfo(i,infoPath)
    print("Success!")


if __name__ == '__main__':
    work()