# Accept the input string with Regular expression of FA: (a+b)*bba.
def FA(s): 
    # Check if the string is empty 
    if not s: 
        return "Rejected (Empty string)" 
 
    # Check if the string contains only 'a' and 'b' characters 
    for char in s: 
        if char not in ('a', 'b'): 
            return "Rejected (Contains characters other than 'a' and 'b')" 
# Minimum length check (implicit in the regular expression) 
# No explicit check needed as 'bba' requires at least 3 characters 
# Check if the string ends with 'bba' 
        if not s.endswith('bba'): 
            return "Rejected (Doesn't end with 'bba')" 
# All conditions met, accept the string 
    return "Accepted (Matches (a+b)*bba)" 
# Input strings to test the function 
inputs = ['bba', 'ababbba', 'abba', 'abb', 'baba', 'bbb', ''] 
for i in inputs: 
    print(FA(i)) 
