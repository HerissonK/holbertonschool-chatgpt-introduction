$ cat factorial.py
#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result -= n
    return result

f = factorial(int(sys.argv[1]))
print(f)

$ ./factorial.py 2
^CTraceback (most recent call last):
  File "/private/tmp/factorial.py", line 9, in <module>
    factorial(int(sys.argv[1]))
  File "/private/tmp/factorial.py", line 5, in factorial
    while n > 1:
          ^^^^^
KeyboardInterrupt