import traceback
def fun1():
    func2()

def func2():
    raise Exception("error rasied")

try:
    fun1()
except Exception: 
    print("second error raised")
    traceback.print_exc