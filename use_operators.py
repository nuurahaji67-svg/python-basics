n1= int(input("enter the first number"))
n2= int(input("enter the second number"))
sum=n1 + n2
diff=n1 - n2
prod=n1*n2
div = n1 / n2
q = n1 // n2
rem = n1 % n2
#taking user input
choice=input(f"\n1.Sum\n2.Diffrence\n3.Product\n4.Division\n5.Qoutient\n6.remainder\n\nEnter your choice: ")

if choice== "sum" or choice == "Sum" or choice =='1':
    print(f"\nSum : {sum}")

elif choice== "diffrence" or choice == "Diffrence" or choice=='2':
    print(f"\nDiffrence : {diff}")
elif choice== "product" or choice == "Product" or choice=='2':
    print(f"\nProduct : {prod}")


        
