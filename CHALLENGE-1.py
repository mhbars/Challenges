String=input()
s=0
k=0
for i in range(len(String)):
    if String[i]=='A' or String[i]=='E' or Sstring[i]=='I' or String[i]=='O' or String[i]=='U':
        k+=len(String)-i
    else:
        s+=len(String)-i
if s==k:
    print("Draw")
elif k>s:
    print("Kevin "+ str(k))
else:
    print("Stuart "+ str())
