num = int(input("Enter a Number\n"))
x=num
y=int()
while (num != 0):
    y=(num%10)+(y*10)
    num=num//10        
if (y==x):
    print ('Palindrome')
else:
    print('Not Palindrome')
