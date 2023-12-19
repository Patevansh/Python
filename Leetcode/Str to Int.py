class solution:
    def strtoint(self,s):
        l="0123456789"
        d=""
        k=0
        m=1
        for i in range(len(s)):
            if s[i]==" ":
                k+=1
                continue
            else:
                break
        if s[k]=="-":
            m=-1
            k+=1
        for i in range(k,len(s)):
            if s[i] in l:
                d=d+s[i]
            else:
                if d!="":
                    return int(d)*m
                else:
                    return 0
        return int(d)*m
sol=solution()
s="234abc"
print(sol.strtoint(s))