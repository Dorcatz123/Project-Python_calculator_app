line_break = '-'*120
import math
import sympy as sym

class SimpleMath:
    def __init__(self):
        
        self.previous_calc = []
        

    def add(self, x, y):
        
        self.previous_calc.append([f'{x}+{y}=', x+y])
        print(line_break)
        print(f"\nYour output is: {x+y}") 
       
    
    def substract(self, x, y):
        self.previous_calc.append([f'{x}-{y}=', x-y])
        print(line_break)
        print(f"\nYour output is: {x-y}") 
        
    
    def multiply(self, x, y):
        self.previous_calc.append([f'{x}*{y}=', x*y])
        print(line_break)
        print(f"\nYour output is: {x*y}") 
        
    
    def division(self, x, y):
        try:
           self.previous_calc.append([f'{x}/{y}=', x/y])
           print(line_break)
           print(f"\n Your output is: {x/y}") 
        except ZeroDivisionError:
           print(line_break)
           print("\nCan't divide by zero!!")
        
           
    def return_previous_output(self):
        self.prev_result_gen = (x for x in self.previous_calc[-1::-1])
        
    def iterate_previous_output(self):
            print(line_break)
            print("\n")
            return f"{next(self.prev_result_gen)}"
       

class PolyCalculator:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        
    def solve(self):
        det = ((self.b)**2 - 4*self.a*self.c)
        #### using syms module to solve an algebraic equation:  
        x = sym.Symbol('x')
        answer = sym.solve((self.c/(self.a*x))+(self.b/self.a)+x-0,x)
        if det >= 0:
          if len(answer) == 2:  
              print(f"\n\nThe factorization is: (x-{answer[0]})(x-{answer[1]})")
          elif len(answer) == 1:
              print(f"\n\nThe factorization is: (x-{answer[0]})(x-{answer[0]})")
        else:
           print("\n\nCan't be factorized! negative determinant!")

        

            
