#Goal:Greater or Lesser Value comparison between two given integer values.

#Step1:Take inputs of two integer value to be compared.
a =input("Enter the number a: ")
b = input("Enter the number b: ")

#Step2:Use conditional statements.
if a>b :
 print ("{} Is Greater Than {}").format(a,b)
elif a<b :
 print ("{} Is Greater Than {}").format(b,a)
else :
 print ("{} and {} are Equal ").format(a,b)

