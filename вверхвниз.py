import string

def caps(pid, ar = string.ascii_lowercase, ast = string.ascii_uppercase):
    strt =''
    for i in range(len(pid)):
        if pid[i] in ar:
            strt += pid[i].swapcase()
        else:
            strt += pid[i] 
    return strt

def down(pid):
    return caps(pid, string.ascii_uppercase, string.ascii_lowercase)

def rorrim(pid):
    return caps(pid, string.ascii_letters)

a = input()
print(caps(a))
print(down(a))
print(rorrim(a))
