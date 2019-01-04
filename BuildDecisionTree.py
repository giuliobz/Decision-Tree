from math import log

def DT_Learn(data, attributes, targetAttr):
    d = data[:]
    classes = []
    for record in d:
        classes.append(record[targetAttr])
    if  (len( attributes ) - 1) <= 0:
        return str( mostFrequentClass(classes) )
    elif classes.count( classes[0] ) == len( classes ):
        return str( classes[0] )
    else:
        best = takeBestAttribute( d, attributes, targetAttr)
        tree = {best: {}}
        for val in getValues( d, best ):
            subData = buildSubDataset(d,best,val)
            attribute = []
            for attr in attributes :
                if(attr!=best):
                    attribute.append(attr)
            subtree = DT_Learn(subData,attribute,targetAttr)
            tree[best][val] = subtree
    return tree

def mostFrequentClass(lst):
    l = lst[:]
    highest_freq = 0
    most_freq = None
    list = []
    for item in l:
        if list.count( item ) <= 0:
            list.append( item )
    for val in list:
        if l.count( val ) > highest_freq:
            most_freq = val
            highest_freq = l.count( val )

    return most_freq


def takeBestAttribute(data, attributes, targetAttr):
    d = data[:]
    bestGain = 0
    bestAttr = None
    for attr in attributes:
        gain = informationGain( d, attr, targetAttr )
        if (gain >= bestGain and attr != targetAttr):
            bestGain = gain
            bestAttr = attr
    return bestAttr

def getValues(data, attr):
    d = data[:]
    valori = []
    for record in d:
        valori.append(record[attr])
    list = []
    for val in valori:
        if list.count( val ) <= 0:
            list.append( val )
    return list

def buildSubDataset(data, attr, value):
    d = data[:]
    list = []
    for record in d:
        if(record[attr] == value):
            list.append(record)
    return list

def entropia(data, target_attr):
    frequenzaValori = {}
    entropia = 0
    for record in data:
        if (record[target_attr] in frequenzaValori):
            frequenzaValori[record[target_attr]] += 1
        else:
            frequenzaValori[record[target_attr]] = 1
    for freq in frequenzaValori.values():
        p = freq/len(data)
        entropia += (-p) * log(p, 2 )
    return entropia


def informationGain(data, attr, targetAttr):
    frequenzaValori = {}
    subset_entropy = 0
    for record in data:
        if (record[attr] in frequenzaValori):
            frequenzaValori[record[attr]] += 1
        else:
            frequenzaValori[record[attr]] = 1
    for val in frequenzaValori.keys():
        p = frequenzaValori[val] / sum( frequenzaValori.values() )
        subDataset = buildSubDataset(data,attr,val)
        subset_entropy += p * entropia( subDataset, targetAttr )
    return (entropia( data, targetAttr ) - subset_entropy)

