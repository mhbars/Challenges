s=raw_input()
k=input()
for i in range(len(s)/k):
    s2=s[i*k:(i+1)*k]
    f=set()
    result=""
    for c in s2:
        if not c in f:
            f.add(c)
            result+=c
    print (result)
