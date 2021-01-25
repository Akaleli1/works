num = 4326720030779807
new = 0
          
def checksum(num):
    
    normalSum = new
    doubleSum = new
    
    for i in range(len(num)):
        num = int(num)
        if i % 2 == 0:
            hold = num % 10
            num = num // 10
            
            normalSum += hold
        
        else:
            digit = num % 10
            digit *= 2
            if num > 10:
                num = num // 10
                
            
            if digit >= 10 :
                temp = digit % 10
                digit = digit // 10
                digit =  digit + temp
            
            doubleSum += digit
    
    total = doubleSum + normalSum
    
    if total % 10 == 0:
        
        return True
    
    else:
        return False
    
def isValid(num):
    
    num = str(num)
    
    if(checksum(num)):
    
        if num[:2] == '51' or num[:2] == '52' or num[:2] == '53' or num[:2] == '54'or num[:2] == '55':
            if len(num) == 16:
                print('MASTERCARD')
                
        elif num[:2] == '34' or num[:2] == '37':
            if len(num) == 15:
                print('AMEX')
                
        elif num[:1] == '4':
            if len(num) == 13 or len(num) == 16:
                print('VISA')
                
    else:
        print("INVALID")

isValid(num)