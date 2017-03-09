file = "documenthmm.txt"
decode = 331122313
states = []
oberservation = []
StartP = []
TransitionP = []
EmissionP = []
tag  = []
probability = []
with open(file) as f:
    mymodel = f.readlines()

start = True
transition = True
emission = True
whole = True
count = 0
while whole and count <= len(states):
    for i in range(0,len(mymodel)):
        if mymodel[i] == 'Alphabet\n':
            n = mymodel[i+2]
            newn = n.rstrip('\n').split('\t')
            oberservation = newn
        if mymodel[i] == 'States\n':
            newline = str(mymodel[i+2])
            splitLine = newline.rstrip('\n').split('\t')
            states = splitLine
        if mymodel[i] == 'StartProbability\n':
            while start:
                for m in range(i, len(mymodel)-1):
                    line = str(mymodel[m+1])
                    newlines = line.rstrip('\n').split('\t')
                    s = newlines[0]
                    try:
                        s1 = float(s)
                        if s1 < 1.0:
                            StartP = newlines
                    except ValueError:
                        start = False
                        break
        if mymodel[i] == 'TransitionProbability\n':
            while transition:
                for m in range(i, len(mymodel)-1):
                    line = str(mymodel[m+1])
                    newlines = line.rstrip('\n').split('\t')
                    s = newlines[0]
                    try:
                        s1 = float(s)
                        if s1 < 1.0:
                            TransitionP.append(newlines)
                    except ValueError:
                        transition = False
                        break
        if mymodel[i] == 'EmissionProbability\n':
            while emission and count<len(states):
                for m in range(i, len(mymodel)-1):
                    line = str(mymodel[m+1])
                    newlines = line.rstrip('\n').split('\t')
                    s = newlines[0]
                    try:
                        s1 = float(s)
                        if s1 < 1.0:
                            EmissionP.append(newlines)
                            count+=1
                            if count == len(states):
                               whole = False
                    except ValueError:
                        pass


# print oberservation
# print states
# print StartP
# print TransitionP
# print EmissionP

#HMM calculation
timestamp = 0
decoded = list(str(decode))
for d in range(0,len(decoded)):
    number = int(decoded[d])-1
    temp = {}
    if d == 0:
        for q in range(0,len(states)):
            stateq = float(StartP[q])*float(EmissionP[q][number])
            temp[states[q]] = stateq
        sort = sorted(temp.items(), key=lambda x: (-x[1], x[0]))
        temp2 = temp
        tag.append(sort[0][0])
        probability.append(sort[0][1])
    else:
        for p in range(0,len(states)):
            t = []
            for q in range(0,len(states)):
                stateq = float(temp2[states[q]]) * float(TransitionP[q][p]) * float(EmissionP[p][number])
                t.append(stateq)
            value = max(t)
            temp[states[p]] = value
        temp2 = temp
        sort = sorted(temp.items(), key=lambda x: (-x[1], x[0]))
        tag.append(sort[0][0])
        probability.append(sort[0][1])

pp = 1
for i in range(0,len(probability)):
    pp = pp * probability[i]

print "tag sequence is: ",tag
print "probability of this tag sequence is: ",pp
print probability























