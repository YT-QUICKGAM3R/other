f = open("data.txt","r")
f1 = f.readlines()
f.close()
listLength = len(f1)
for x in range(0,listLength-1):
  f1[x] = f1[x][:-1]
success=0
for a in f1:
  x = a.replace('-', ' ').split(' ')
  x[2] = x[2][:-1]
  minCount = int(x[0])
  maxCount = int(x[1])
  letter = x[2]
  phrase = x[3]
  if phrase.count(letter)>=minCount and phrase.count(letter)<=maxCount:
    success = success + 1
print(success)
