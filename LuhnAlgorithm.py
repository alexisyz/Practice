#Card validator

n = int(input()) #Quantity.
t = 0 #Total of valid cards.

while n != 0:
    s = input() #Receive number.
    b = 0 #Temporary.
    a = 0 #Summator.
    c = 0 #Detect every 2 values.
    k = len(s)-1 #Total index.
    for i in range(k+1):
        b = int(s[k-i]) #We save the number.
        c = c + 1
        if c == 2:
            b = b*2
            if b > 9:
                b = b - 9
            c = 0
        
        a = a + b
    
    if a%10 != 0:
        t = t + 1
    
    n = n - 1 #Discount analyzed card.

print(t)
