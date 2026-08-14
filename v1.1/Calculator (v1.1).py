# Generated from: notebooks_Intro.ipynb
# Converted at: 2026-08-14T16:41:28.667Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# Python Calculator (for two numbers only) v1.1

''' Features Added:
    1. Modulus Quotient
    2. Exponential
    3. "Now, the user is able to write numbers in decimal."
    Features Improved:
    1. Improved the alignment in commands '''

print ("Welcome To Python Calculator v1.1 !!!")
print ("Created by Aayush Sharma")
print ("Follow Aayush6244 on GitHub: https://github.com/Aayush6244")
print ("Please note these operations are upto two numbers only.")
print('''Here are the operations to include:- 
S. No. (Operation Name)
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Modulus Quotient
6. Exponential
Choose any of it of your choice''')

A = float(input("Enter your first no."))
Operation = float(input("Choose the operation by S. No."))
print ("While writing exponent, please input second no. as 0.")
B = float(input("Enter your second no."))

if Operation == 1:
    print ("You chose Addition.")
    print ("Answer.", A+B)
elif Operation == 2:
    print ("You chose Subtraction.")
    print ("Answer.", A-B)
elif Operation == 3:
    print ("You chose Multiplication.")
    print ("Answer.", A*B)
elif Operation == 4:
    print ("You chose Division.")
    print ("Answer.", A/B)
elif Operation == 5:
    print ("You chose Modulus Quotient.")
    print ("Answer.", A//B)
elif Operation == 6:
    print ("You chose Exponential.")
    Power = float(input("Enter the power of exponent in numbers: "))
    print ("Exponent Answer: " , A**Power)
else:
    print ("You did not choose any operation or there's an error in input. Please try again.")
