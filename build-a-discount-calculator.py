# ** start of main.py **

# def meaning definition of function
# type keyword used for data type check <class 'int'>
# print aur return mai zameen asmaan da difference
# MADE BY DANIYAL SAQIB

def apply_discount(price, discount):
    if (not isinstance(price,(int,float))):
        return "The price should be a number" # validation
    elif (not isinstance(discount,(int,float))):
        return "The discount should be a number" # validation    
    elif (price <= 0):
        return "The price should be greater than 0"
    elif (discount < 0 or discount > 100):
        return "The discount should be between 0 and 100"
    # everything is valid
    else:
        final = price - (discount/100)*price
        return final
        #end of function

#testing phase
print(apply_discount("oh", 5))
print(apply_discount(100, 20))
print(apply_discount(200, 50))
print(apply_discount(50, 0))
print(apply_discount(69, 100))
print(apply_discount(74.5, 20.0))                     
    

# h = 3 brainstorming only
# str(h)
# print(h)


# ** end of main.py **

