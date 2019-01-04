import sys
from BuildDataset import makeTrainDataset,makeValisdationSet,makeTestDataset
from BuildDecisionTree import DT_Learn
from Pruning import postPruningTree
from Analisi import classify,accuracy
sys.setrecursionlimit(15000000)

lenghtTR = input('Definire la grandezza del training set in termini di esempi da 1 a 60000 : ')
dataset = makeTrainDataset(int(lenghtTR))
lenghtTS = input('Definire la grandezza del test set in termini di esempi da 1 a 10000 : ')
data , label = makeTestDataset(int(lenghtTS))
attr = []
for i in range(len(dataset[0])):
    attr.append(i)
print('Inizio fase di training')
tree = DT_Learn(dataset,attr,attr[-1])
print ('Fase di training terminata')
print('si classificano i dati')
classification = classify(tree,data)
print('Fine classificazione dei dati')
a = accuracy(classification,label)
print( 'l accuratezza è : ' + str( a ) + '%' )
test , val = makeValisdationSet(int(lenghtTR))
print ('Inizio fase di pruning dell albero')
t = postPruningTree(val,attr[-1],a,tree)
print('Pruning terminato')
print('si classificano i dati')
classification = classify(tree,data)
print('Fine classificazione dei dati')
a = accuracy(classification,label)
print( 'l accuratezza dopo il pruning è : ' + str( a ) + '%' )
