def palindrome(l):
    List=l[::-1]
    if l==List:
        print(f'palindrome of List {l} is {List}')
    else:
        print(l ," is not palindrome")
n=input("Enter a word:")
palindrome(n)
