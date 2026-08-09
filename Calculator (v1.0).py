# Generated from: notebooks_Intro.ipynb
# Converted at: 2026-08-09T07:59:47.220Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

#Python Calculator (for two numbers only)
print("Welcome To Python Calculator")
print('''Here are the operations to include:- 
1. Addition
2. Subtraction
3. Multiplication
4. Division
Choose any of it of your choice''')
A = int(input("Enter your first no."))
Operation = int(input("Choose the operation by S. No."))
B = int(input("Enter your second no."))
if Operation == 1:
    print ("Answer.", A+B)
elif Operation == 2:
    print ("Answer.", A-B)
elif Operation == 3:
    print ("Answer.", A*B)
elif Operation == 4:
    print ("Answer.", A/B)
else:
    print ("You did not choose any operation or there's an error in input. Please try again.")
    # This calculator is made as a 1st working version which includes basic arithmatic operations (+, -, *, /)
