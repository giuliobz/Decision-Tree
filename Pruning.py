from Analisi import accuracy,classify,mostFrequentClass

def postPruningTree(validationSet,targetAttr,ac,tree):
    t = tree
    acc = ac
    if(type(t) != type("string")):
        radice = next(iter(t))
        for key in t[radice].keys():
            if(type(t[radice][key]) != type("string")):
                node = t[radice][key]
                classes = buildLabelValidation(validationSet,targetAttr)
                cls = mostCommonClass(node)
                t[radice][key] = str(cls)
                a = accuracy(classify(t,validationSet),classes)
                if(a > acc):
                    acc = a
                else:
                    t[radice][key]= postPruningTree(validationSet,targetAttr,acc,node)
    return t

def buildLabelValidation(validationSet,targetAttr):
    classes = []
    for i in range(len(validationSet)):
        classes.append(validationSet[i][targetAttr])
    return classes

def mostCommonClass(tree):
    cls = buildClassList(tree)
    return mostFrequentClass(cls)

def buildClassList(tree):
    cls = []
    if(type(tree) == type("string")):
        return cls.appen(next(iter(tree)))
    else:
        radice = next(iter(tree))
        for key in tree[radice].keys():
            if(type(tree[radice][key])==type("string")):
                cls.append(int(tree[radice][key]))
            else:
                cls.extend(buildClassList(tree[radice][key]),)
    return cls

