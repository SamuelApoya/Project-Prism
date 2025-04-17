def helloWord(a):
    if a % 10:
        out = 'Hello World'
    else:
        out = 'Go and sleep'
    return out

print(helloWord(a=10))