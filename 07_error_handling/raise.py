#Raise
try:
    a = 10
    b = 0
    a/b
except ZeroDivisionError as e:
    raise ZeroDivisionError("we cannot divide")

y = 4
try:
    if y == 4:
        raise FileNotFoundError("the given condition is true")

except FileNotFoundError as e:
    print(e)
