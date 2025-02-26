s="abcdabcabcdf"
pattern="abcdf"
l=len(s)
pl=len(pattern)
for i in range(l-pl+1):
    if pattern == s[i:i+pl]:
        print("Found at index:",i)
