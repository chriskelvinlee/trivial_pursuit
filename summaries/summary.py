import os
import ast

path = "../reruns/"
fileList = os.listdir(path)
fileList = sorted(fileList, key=lambda string: int(string.strip("query_.tx")))

numsCorrect = [0,0,0,0,0]
total = 0

confidences = [[],[],[],[],[]]
indexes = []

for fname in fileList:
    f = open(path + fname)
    lines = f.readlines()

    #CORRECTNESS PORTION
    correct = lines[6].strip("Corect: \n\t").split('\t\t')
    answer = lines[7].strip("Answer: \n\t").split('\t\t')

    dicts = ast.literal_eval(lines[27])

    thisQ = [0,0,0,0,0]
    for i in range(len(correct)):
        if correct[i] == answer[i]:
            thisQ[i] = 1
            numsCorrect[i] += 1
        elif answer[i] == "9":
            if len(dicts[i - 1]) == 1:
                if (dicts[i-1].keys()[0] == lines[2].strip("\n")):
                    numsCorrect[i - 1] += 1
                    thisQ[i] = 1
    if thisQ[4] == 1 and thisQ[3] == 0:
        print fname
    total += 1

    #CONFIDENCE PORTION
    confidence = lines[8].strip("Confidec: \n\t").split('\t\t')
    for i in range(len(confidence)):
        confidences[i].append(int(confidence[i]))
    indexes.append(int(fname.strip("query.txt_")))

output = open('results.txt', "w")
print >> output, confidences
print >> output, indexes
print >> output, numsCorrect
print >> output, total
