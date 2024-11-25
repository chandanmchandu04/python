#Exception Chaining
try:
    a = 3
    b = 0
    c =a/b
except ZeroDivisionError as e:
    raise ValueError("this is chaining Error") from e

try:
    open("file.txt")
except OSError as exc:
    raise RuntimeError from exc