i = 0
count = 0
while i <= 6:
    print(f"number of balls {i}")

    if i == 3:
        print(f"ball number {i} wide ball")
        i = i + 1
        break
    count = count + 1

    print(f"runs {count}")
    count = count + 1
    i = i + 1

if count >= 6:
    print('over')
else:
    print('over not completed')