l = [1, 2, 3, "virat", 5, 6]
for i in l:
    print('skip virat')
    print(i)

    if i == "virat":
        print('virat left the job')
        continue
    print('start from 5')

for i in range(5):
        if i == 3:
            break
        print(i)

x = 0
while x < 5:
      if x == 2:
            x += 1
            continue
      print(x)
      x += 1

a = 40
b = 40 
if a > b:
     print(' a is greater and a is the superior')
else:
     print('both are main and both are the rulers of the given senirio')