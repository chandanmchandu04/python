# import logging
# logging.basicConfig(level=logging.DEBUG)

# print("print statement does not allow debugging")

# logging.debug("debugging started")
# logging.info("logging started")
# logging.warning("print statement does not pop-up warning")
# logging.error("this is my first error")
# logging.critical("this is critical")


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

def div(a, b):
    try:
        result = a/b
        logging.info(f"division of {a} by {b} is {result}")
        return result
    except ZeroDivisionError as e:
        logging.error("there is an error in division")

a = 20
b = 0
result = div(a,b)
print(result)


import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')

def factorial(n):
    if n < 0:
        logging.error("input will not be negative")
        return None
    elif n == 0:
        logging.warning("factorial of 0 is 1")
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *=i
            logging.info(f"factorial of {n} is {result}")
        return result

n = 5
fac = factorial(n)
print(fac)
if fac is not None:
    print(f"factorial of {n} is {fac}")
else:
    print("error occured")