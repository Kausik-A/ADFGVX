#!/usr/bin/env python
# coding: utf-8

# In[7]:


from collections import Counter
from sys import argv
import math

f1 = open ("adfgvx.encode", "r")
data = f1.read().replace('\n', '').replace(" ", "")
data = (''.join(c for c in data if c.isalpha()))
data = data.lower()



def PSI(frequency):
    psiValue = 0
    for i in frequency:
        psiValue = psiValue + (frequency[i] * frequency[i])
    return psiValue

def getFreq(count_char,size_char):
    charFreq = {}
    for i in count_char:
        charFreq[i] = (count_char[i] / size_char)
    return charFreq



singleCharCountValue = Counter(x for x in data if x.isalpha())
singleCharFrequency = getFreq(singleCharCountValue,len(data))
psiValue = PSI(singleCharFrequency)
print("Psi value of single letters for adfgvx.encode: "+ str(psiValue))

totCount = len(data) / 2
if(not totCount.is_integer()):
    decimal, whole = math.modf(totalCount)
    totCount = whole
    size = len(data)-1
else:
    size = len(data)

countDoubleChar = {}
for item in range(0, size, 2) :
    character = "".join(data[item : item + 2])
    if character in countDoubleChar:
       countDoubleChar[character] += 1
    else:
       countDoubleChar[character] = 1

doubleCharFreq = getFreq(countDoubleChar,totCount)

doublePSIVal = PSI(doubleCharFreq)
print("Psi value of a pair of letters for adfgvx.encode: ",doublePSIVal)


# In[8]:


from collections import Counter
from sys import argv
import math

f1 = open ("alice_in_wonderland.txt", "r")
data = f1.read().replace('\n', '').replace(" ", "")
data = (''.join(c for c in data if c.isalpha()))
data = data.lower()



def PSI(frequency):
    psiValue = 0
    for i in frequency:
        psiValue = psiValue + (frequency[i] * frequency[i])
    return psiValue

def getFreq(count_char,size_char):
    charFreq = {}
    for i in count_char:
        charFreq[i] = (count_char[i] / size_char)
    return charFreq



singleCharCountValue = Counter(x for x in data if x.isalpha())
singleCharFrequency = getFreq(singleCharCountValue,len(data))
psiValue = PSI(singleCharFrequency)
print("Psi value of single letters for alice in wonderland: "+ str(psiValue))

totCount = len(data) / 2
if(not totCount.is_integer()):
    decimal, whole = math.modf(totalCount)
    totCount = whole
    size = len(data)-1
else:
    size = len(data)

countDoubleCharacter = {}
for item in range(0, size, 2) :
    character = "".join(data[item : item + 2])
    if character in countDoubleCharacter:
       countDoubleCharacter[character] += 1
    else:
       countDoubleCharacter[character] = 1

doubleCharFreq = getFreq(countDoubleChar,totCount)

doublePSIVal = PSI(doubleCharFreq)
print("Psi value of a pair of letters for alice in wonderland: ",doublePSIVal)


# In[ ]:




