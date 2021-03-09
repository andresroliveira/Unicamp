def isNum(s):
    flag = 1

    try:
        n = int(s)
    except ValueError:
        flag = 0

    return flag

def isDig(c):
    return (c >= 'a' and c <= 'z') or (c >= 'A' and c <= 'Z')

def isAlfa(s):
    for c in s:
        if(not isDig(c)):
            return False
    return True

n = int(input())
h = 0
e = 0

while n:
    s = input()

    if(isNum(s)):
        print(s)
    elif(s[0] == '#'):
        if(isAlfa(s[1:])):
            h += 1
        else:
            e += 1
    else:
        if(isAlfa(s)):
               print(s)
        else:
               e += 1
    
    n -= 1

if(h == 1):
    print("1 hashtag foi removida.")
elif(h > 1):
    print("%d hashtags foram removidas." %h)

if(e == 1):
    print("1 emoticon foi removido.")
elif(e > 1):
    print("%d emoticons foram removidos." %e)
