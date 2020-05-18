from people import People
import re

file_path = 'D:\\MioReader\\Data_Converter_Python\\GorbPlusRes\\' #расположение файлов

def convert(file_path_read, file_path_write):
    gorbFile = open(file_path + file_path_read, 'r', encoding='utf-8')
    resultFile = open(file_path + 'result.txt', 'r', encoding='utf-8')
    gorbPlusResult = open(file_path + file_path_write, 'a+', encoding='utf-8')

    resList = []
    listOfResult = []

    print('Start writting {}'.format(file_path_read))

    next(resultFile)                           #пропускаю первую строку
    for line in resultFile:                    #сплит резалта
        resList = line.split()                 #загоняю резалт в лис
        People(resList[0]+' '+resList[1]+' '+resList[2], resList[3], resList[12])
        
    gorbPlusResult.writelines('file;N;-2;-1;0;1;2;p-2;p-1;p0;p1;p2;TypeExperiment;Target;N_Type_Target;N_Type;Type_Target;N_Target;Hit;' + '\n')
    next(gorbFile)                              #пропускаю первую строку
    for line in gorbFile:                       #сплит горба
        resList = line.split(';')

        gorbList = re.search('[а-яА-ЯёЁ]+\s+[а-яА-ЯёЁ]+\s+[а-яА-ЯёЁ]+', resList[0])
        name = gorbList[0]
        gorbList = re.search('[-+]?\d+', resList[0])
        id = gorbList[0]
        for obj in People.nameList:
            if name == obj.getFIO() and id == obj.getNumOfExperiment():
                gorbPlusResult.write(line.replace('\n', ''))
                gorbPlusResult.write(obj.getResult() + '\n')
                break

    print('Writting completed {}'.format(file_path_write))

    gorbFile.close()
    resultFile.close()
    gorbPlusResult.close()
    
convert('total_VGorb.csv', 'VGorb_plus_res.csv')
convert('total_W2Gorb.csv', 'W2Gorb_plus_res.csv')