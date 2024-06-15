s1=int(input('Enter the side:'))
s2=int(input('Enter the side:'))
s3=int(input('Enter the side:'))
if(s1==s2 and s1==s3 and s2==s3):
    print("Equilateral triangle")
elif(s1==s2 and s1!=s3 and s2!=s3):
    print("Isosceles triangle")
else:
    print("Scalene triangle")