
message = open('alice_in_wonderland.txt','r').read() 
encrypted = open('adfgvx.encode','r').read() 
msglen = len(encrypted)
encryptlen = len(message)

let = {}
frequency = {}
valmatch = 0
for i in range(0, len(encrypted), 2):
    substring = "".join(encrypted[i: i + 2])
    if substring in let:
        let[substring] += 1
        frequency[substring].append(valmatch)
    else:
        let[substring] = 1
        matchOrder = list()
        matchOrder.append(valmatch)
        frequency[substring] = matchOrder
    valmatch += 1
i = 0
j = int(msglen / 2)
flag = False

while (flag == False and j != encryptlen+1):
    substringText = message[i:j]
    frequency = {}
    permutedChars = {}
    valmatch = 0
    for k in range(0, len(substringText)):
        letter = substringText[k]
        if letter in permutedChars:
            permutedChars[letter] += 1
            frequency[letter].append(valmatch)
        else:
            permutedChars[letter] = 1
            matchOrder = list()
            matchOrder.append(valmatch)
            frequency[letter] = matchOrder
        valmatch += 1
    i += 1
    j += 1
    totalLength = len(frequency)
    matchLength = 0
    for i in frequency:
        iVal = frequency[i]
        for j in frequency:
            jVal = frequency[j]
            matchLength += 1 if iVal == jVal else 0

    if totalLength == matchLength:
        print("permutation match with", frequency)
        print("substringtext flag from Alice")
        print(substringText)
        flag = True
