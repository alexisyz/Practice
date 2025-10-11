#Hangman game.
s = input() # Original string.
s = s.upper() # Converts it to uppercase.
c = "" # Guesses string.
p = 6 # Attempts counter.
while p > 0: # While attempts remain.
    k = input()
    k = k[0] # Only takes the first letter.
    c = c + k.upper() # Concatenate to the guess string and convert to uppercase.
    b = "" # Reset b.
    for i in range(len(s)):
        f = "_" # Character to concatenate.
        for j in range(len(c)): # Check if any guess was correct.
            if s[i] == c[j]: # If a match was found.
                f = c[j] # Replaces the character to concatenate.
        
        b = b + f # Concatenate the character.
    for i in range(len(b)): # Check the formed string.
        if b[i] == "_": # If the word is not yet complete.
            f = "0" # Activate flag.
            break # Exit the loop.
    if f != "0": # If the word is complete.
        print(f"Won with {p} remaining attempts")
        print(b)
        p = -1
    else:
        print(f"{c}  {b}  attempts: {p-1}") # Prints the formed string, the original string, and the remaining attempts.
        p = p - 1 # Discard the attempt.

if p == 0: # If lost.
    print(f"Lost, the word was: {s}")
