#Exception Handling 
try:
    a = 10
    b = 0
    c = a/b
except Exception as e:
    print(e)

try:
    l = [1, 2, 3, 4]
    l[6]
except IndexError as e:
    print(e)
except ZeroDivisionError as e:
    print(e)
except Exception as e:
    print(e)

try:
    print("hello")
 
except Exception as e:
    print(e)

else:
    print("we got the file")
    a = 1
    b = 3
    c = a + b
    print(c)

finally:
    print("task completed successfully ")

#Nested Block
try:
    try:
        print("this is my try block")
    except:
        print("this is my except block")
    
except:
        print("this is my outer except block")
        try:
            print("this try is inside except")
        except:
            print("this except is inside my except block")

else:
    try:
        print("this is my else block try statement")
    except:
        print("this is my except inside else")

finally:
    try:
        print("this is try inside finally")
    except:
        print("this is my except inside except block")


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
