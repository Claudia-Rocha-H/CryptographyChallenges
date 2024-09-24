#Manual process
p = "Three can keep a secret, if two of them are dead."
i = len(p)-1
reversed = ""
while i >= 0:
    reversed += p[i]
    i-=1
print(reversed)

#using slicing
print(p[::-1])
