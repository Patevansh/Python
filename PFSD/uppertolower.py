def uppertolower(s):
    k=""
    for i in s:
        if i in "AEIOU":
            k+=i
        else:
            k+=i.lower()
    return k
s="ABCEFI"
print(uppertolower(s))