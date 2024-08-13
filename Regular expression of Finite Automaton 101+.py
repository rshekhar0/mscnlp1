# Accept the input string with Regular expression of Finite Automaton: 101+.
def FA(s): 
    # If the length is less than 3, reject 
    if len(s) < 3: 
        return "Rejected (String too short)" 
 
    # Check the first three characters 
    if s[0] == '1' and s[1] == '0' and s[2] == '1': 
        # Check remaining characters 
        for i in range(3, len(s)): 
            if s[i] != '1': 
                return "Rejected (Not 101 followed by 1s)" 
        # All characters after 2nd index are '1', accept 
        return "Accepted (Matches 101+)" 
    else: 
        # First three characters don't match the pattern, reject 
        return "Rejected (Doesn't start with 101)" 
 
# Input strings to test the function 
inputs = ['1', '10101', '101', '10111', '01010', '100', '', '10111101', '1011111'] 
 
# Loop through the inputs and call the FA function for each 
for i in inputs: 
    print(FA(i)) 
