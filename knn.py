import pars
import math



def normalize(data):
    minimum = []
    maximum = []
    for i in range(len(data[0]) - 1):
        tmp_1 = min(data[0: len(data)][i])
        print(data[0:len(data)][i])
        minimum.append(tmp_1)
        tmp_2 = max(data[0: len(data)][i])
        maximum.append(tmp_2)
    for i in range(len(data) - 1):
        for j in range(len(data[0]) - 1):
            data[i][j] = abs((data[i][j] - minimum[j]) / (maximum[j] - minimum[j]))
    print(data)
    return data

def GetTestData(data):
    test_data = []
    count_f = 0
    for i in range(3001, 4000):
        if count_f < 400:
            test_data.append(data[i][1:9])
            if data[i][8] == 'False':
                count_f += 1
        else:
            if data[i][8] == 'True':
                test_data.append(data[i][1:9])
    
    for i in range(len(test_data)):
        test_data[i][0:7] = list(map(lambda x: float(x), test_data[i][0:7]))

    return test_data

def Dist(a, b):
    sum = 0.0
    for i, j in zip(a[0:7], b[0:7]):
        sum += (i - j)**2
    return math.sqrt(sum)

def DistSort(data, x):
    tmp = data
    for line in tmp:
        d = Dist(line, x)
        line.append(d)
    
    return sorted(tmp, key = lambda dat : dat[len(dat) - 1])

def Weight(x, y):
    return 1 / Dist(x, y)

def FindClass(data, k):
    first_k = []

    for i in range(k):
        first_k.append(data[i])
    
    weight_0 = 0.0
    weight_1 = 0.0

    for i in first_k:
        if i[len(i) - 2] == 'True':
            weight_1 += (1 / i[len(i) - 1])
        else:
            weight_0 += (1 / i[len(i) - 1])

    clas = 'False' if weight_0 > weight_1 else 'True'
    return clas

    



def kNearestNeighbors(data, k):
    train_data = pars.pars_data(data)

    test_data = GetTestData(data)

    count = len(test_data)
    succes = 0

    for test in test_data:
        sort_data = DistSort(train_data, test)
        clas = FindClass(sort_data, k)
        if clas == test[len(test) - 1]:
            succes += 1
    return (succes / count) * 100



data = pars.csv_reader('nasa.csv')

print('Accuracy: {0}%'.format(kNearestNeighbors(data, 11)))