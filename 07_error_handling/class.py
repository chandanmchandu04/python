#Changing the Name of the error By creating the class.
#To change the error message we use raise method to change it.
class MyError(Exception):
    pass
    
def fun(a, b):
    if b == 0:
        raise MyError("Error occured")
    return a/b

try:
    fun(10,0)
    raise MyError("this is another error")

except Exception as e:
    print(e)
