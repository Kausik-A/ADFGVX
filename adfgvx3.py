import itertools

message = open('adfgvx.encode','r').read() 
totalLength = int(len(message)/3)
maxPerm = ""
maxPSI = [0,0]

for permSequence in range(3, 8):
    wordsList = list(itertools.permutations(range(0, permSequence)))
    words = [message[i: i + permSequence] for i in range(0, len(message), permSequence)]
    for sequence in wordsList:
        psi = 0
        letterFreq = []
        tempMsg = ""
        tripletLetterFreq = {}
        
        for x in words:
            if len(x) == permSequence :
                for i in range(0, permSequence):
                    tempMsg = tempMsg + x[sequence[i]]
            else:
                tempMsg = tempMsg + x

        permLen = len(tempMsg)/3
        permRange = len(tempMsg) if permLen.is_integer() else len(tempMsg)-1
        
        for val in range(0,permRange,3):
            temp = "".join(tempMsg[val: val+3])
            tripletLetterFreq[temp] = tripletLetterFreq[temp] + 1 if temp in tripletLetterFreq else 1
        
        for i in tripletLetterFreq:
            letterFreq.append(tripletLetterFreq[i] / int(permLen))
        
        for i in range(0,len(letterFreq)):
            psi += (letterFreq[i])**2
        if maxPSI[1] < psi:
            maxPSI[0] = sequence
            maxPSI[1] = psi
            maxPerm = tempMsg

print("Decoded text: " +maxPerm)