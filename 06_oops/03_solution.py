def debug(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper

    

def greet(name, greetings="hello"):
        print(f"{greetings}, {name}")