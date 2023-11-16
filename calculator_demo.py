from calculator import *
import traceback
line_break = '-'*120
user_input = input("Start the simple Calculator: Press 1 \n  Start the polynomial Calculator: Press 2:?").lower()
logo = '''                                                                                                
  ,ad8888ba,             88                        88                                           
 d8"'    `"8b            88                        88              ,d                           
d8'                      88                        88              88                           
88            ,adPPYYba, 88  ,adPPYba, 88       88 88 ,adPPYYba, MM88MMM ,adPPYba,  8b,dPPYba,  
88            ""     `Y8 88 a8"     "" 88       88 88 ""     `Y8   88   a8"     "8a 88P'   "Y8  
Y8,           ,adPPPPP88 88 8b         88       88 88 ,adPPPPP88   88   8b       d8 88          
 Y8a.    .a8P 88,    ,88 88 "8a,   ,aa "8a,   ,a88 88 88,    ,88   88,  "8a,   ,a8" 88          
  `"Y8888Y"'  `"8bbdP"Y8 88  `"Ybbd8"'  `"YbbdP'Y8 88 `"8bbdP"Y8   "Y888 `"YbbdP"'  88          '''

print(logo)
print(line_break)


def simple_calculator(user_input):
    print("\n\nHi! welcome to Simple Math calculator!")
    new_calc = SimpleMath()                                                                                      
    while user_input == '1':
        print(line_break)
        user_input2 = input("\n\n\n Start a new calculation: Press 1 \n      access additional features: Press 2 \n                  exit calculator: Press 'q'")
            
        if user_input2 == '1':
            
            print('''\n\nInstructions: input the first number at the first user prompt, \n\n   then select the operation you want to perform in the next prompt
    \n       and then input the second number in the third user prompt. \n\n           You can keep doing calulations with the previous output or press 'q' to start a new calculation!''')   
            cal_on = True
            print(line_break)
            check = True
            while check:
                try:
                    first_input = float(input("\nEnter the first number:"))
                    check = False
                except:
                    print("\nThe number should be a real number!")

            ######Appending to the previous_calc list in the object to access the previous values.
                    
            new_calc.previous_calc.append(['user starts calculation, first input:', first_input])
            operations = {'+': new_calc.add, '-': new_calc.substract, '*': new_calc.multiply, '/': new_calc.division }
            while cal_on:
                print(line_break)
                check = True
                while check:
                    operation = input('''\n Select an operation or Press 'q' to exit calculation: \n addition: Press '+' \n substraction: Press '-'  \n multiplication: Press '*"  \n division: Press '/' ''')
                    if operation in ['q','+','-','*','/','0']:
                       check = False
                    else:
                        print("\nInvalid input please try again!")
                        
                if operation!= '0' and operation!= 'q':
                   print(line_break)
                   check = True
                   while check:
                       try:
                           second_input = float(input("\nEnter the second number:"))
                           check = False
                       except:
                           print("\nThe number should be a real number!")
                           
              ###### Doing the calculation by using the functions in the simplemath class, using the previous output to carry on computation:
                       
                   operations[operation](new_calc.previous_calc[-1][1], second_input)
                   
                elif operation == 'q':
                   cal_on = False
                   print(line_break)
                   
                
        #### for accessing previous outputs by printing self.previous_calc:       
        elif user_input2 == '2':
             try:
                 new_calc.return_previous_output()
                 access_feature = True
                 while access_feature:
                     print(line_break)
                     ad_feature = input("\n access previous outputs: Press 'b' \n to exit: Press 'q'").lower()
                     if ad_feature == 'b':
                         print(new_calc.iterate_previous_output())                     
                     elif ad_feature == 'q' :
                         access_feature = False
                     else:
                         print("\nInvalid input! please try again!")
             except StopIteration:
                 print(line_break)
                 print("\n\nCan't print anymore values!")
                     
        elif user_input2 == 'q':
            user_input = 'n'
            print("\n Good bye!")

        else:
            print("\nInvalid input! please try again!")
                       
        
def poly_calculator(user_input):
     print(line_break)
     print("\n\nHi! welcome to polycalculator!")
     print(line_break)
     print('''\n\nInstructions: Input the coefficients a, b and c of \n the polynomial ax^2+bx+c and the calculator will solve the equation for you!!''')
     print(line_break)
     while user_input == '2':
         user_input2 = input("\n\n\n Start a new calculation: Press 1 \n            exit calculator: Press 'q'").lower()
         if user_input2 == '1':
             try:
                 a = float(input("\n\nenter the coefficient a in ax^2+bx+c:"))
                 b = float(input("\nenter the coefficient b in ax^2+bx+c:"))
                 c = float(input("\nenter the coefficient c in ax^2+bx+c:"))
                 poly_obj = PolyCalculator(a,b,c)
                 poly_obj.solve()
                 
             except ZeroDivisionError:
                 
                 print("\n\n coefficient a should be non zero value!")

             except:
                 
                 #traceback.print_exc()
                 print("\nInput should be a real number!")
                 
             
         elif user_input2 == 'q':
             user_input = 'n'
             print('Good bye!!')
         else:
             print("\nInvalid input! plese try again!")
      
    
if user_input == '1':
    
    simple_calculator(user_input)
    
elif user_input == '2':
    
    poly_calculator(user_input)
    
else:
    print("\nInvalid input please try again!")

