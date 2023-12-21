import string
ch=string.digits + string.ascii_letters
chl=list(ch)
def convert(num,base):
  output=""
  if base<2:
    print("Base cannot be 2")
    return
  elif base<len(ch):
    while(num>0):
      rm=num%base
      output+=chl[rm]
      num=num//base
    print(output[::-1])
  else:
    print("Enter base within 2-61")
convert(8,8)