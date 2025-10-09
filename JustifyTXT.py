# Justify text (20 characters).
def ver(n): # Check submitted string to justify it to 20 characters.
    b =  len(n) # Original sub-string size.
    s = "" # Sub-string.
    e = 0 # Spaces (Detect cases).

    if b == 20: # If it is already justified.
        return(n) # Returns it.
    
    if b == 21:
        return(caso3(n)) # Returns the period or comma correction.
    
    if b > 20: # If it is larger, trim the last word.
        for i in range(b):
            if n[(b-1)-i] == " ": # Find the first space in reverse.
                for j in range(b-(i+1)): # Save string before the space.
                    s = s + n[j] # Save the rest of the sub-string.
                break
    
    for i in range(len(s)): # Find the number of spaces.
        if s[i] == " ":
            e = e + 1 # Counts the spaces.
    
    if e == 0: # A single word.
        return caso1(s)
    elif e >= 1: # Two or more words.
        return caso2(s)
    

def caso1(n):
    s = "" # Modified Sub-string.
    for i in range(len(n)):
        s = s + n[i] # Adds the text.
        if len(s) + (len(n)-(i+1)) == 20: # If the separation plus the rest of the text fit.
            for j in range(len(n)-(i+1)):
                j = j + 1 # Starts from the next one.
                s = s + n[i+j]
            return(s) # Return adjusted string.
        s = s + " " # Adds the space.
        if len(s) + (len(n)-(i+1)) == 20: # If the separation plus the rest of the text fit.
            for j in range(len(n)-(i+1)):
                j = j + 1 # Starts from the next one.
                s = s + n[i+j]
            return(s) # Return adjusted string.



def caso2(n):
    m = len(n) # String size/length.
    k = 1 # Spaces to add.
    while k > 0:
        s = "" # Modified Sub-string.
        for i in range(len(n)):
            s = s + n[i]
            if n[i] == " ":
                for b in range(k): # Gradually adds more extra spaces.
                    if (len(s) + (m - (i+1))) == 20: # If the size of 's' plus the rest of 'n' equals 20.
                        for j in range(m - (i+1)): # Iterates over the remaining text.
                            j = j + 1 # Iterates one less time because j starts at 1.
                            s = s + n[i + j]
                        return s # Returns the justified text.
                    s = s + " " # Extra space.
                    
                    
        k = k + 1 # One more space is added.
        if len(s) > 20:
            return "0"

def caso3(n):
    m = len(n) # String size/length.
    k = 1 # Spaces to add.
    s = "" # Modified Sub-string.
    for i in range(len(n)):
        s = s + n[i]
        if n[i] == "." or n[i] == ",": # If the next character is a period or comma.
            for j in range(len(n) - (i+2)): # Iterates over the remaining text.
                    j = j + 2 # Iterates one less time because j starts at 1.
                    s = s + n[i + j]
            return s # Returns the justified text.

def indice(n): # In charge of repositioning the index.
    b =  len(n) # Original sub-string size.
    if b == 21 or b == 20: # If it includes all the text.
        return 0 # Do not modify the index.
    else:
        for i in range(b):
            if n[(b-1)-i] == " ": # Find the first space in reverse.
                return (i+1) # Returns how much it should step back.


s = input() # String.
n = "" # Sub-string.
i = 0 # Counter.
while i < len(s):
    if len(n) >= 20 and s[i] == " ": # Once 20 is reached, enter when the first space is found.
        t = indice(n) # Extra values at the start of the last word of N.
        n = ver(n) # Concatenate the justified text.
        print(n)
        n = "" # Reset the sub-string.
        i = i - t # Position at the first letter of the last word of N.
    else:
        n = n + s[i]
    i = i + 1

if n != "":
    print(n)
