from BuildDecisionTree import mostFrequentClass

def accuracy(classification, lbl):
    correct = 0
    wrong = 0
    i = 0
    for val in classification:
        if int( val ) == lbl[i]:
            correct += 1
        else:
            wrong += 1
        i += 1
    accuracy = float( (correct / (correct + wrong)) * 100 )
    return accuracy

def mostCommonClass(tree, attr):
    list = []
    for key in tree[attr].keys():
        if (type( tree[attr][key] ) == type( "string" )):
            list.append( tree[attr][key] )
    return mostFrequentClass( list )

def classify(tree,test):
    classification = []
    for record in test:
        t = tree
        while type(t) != type('string'):
            attr = next(iter(t))
            if record[attr] in t[attr].keys():
                t = t[attr][record[attr]]
            else:
                t = str(mostCommonClass(t,attr))
        classification.append(t)
    return classification


