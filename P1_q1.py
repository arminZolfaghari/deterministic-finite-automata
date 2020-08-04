# Open the DFA_input_1.txt file
file1 = open("DFA_Input_1.txt", "r")

number_line = 0

alphabet = []
states = []
first_state = ""
final_states = []
current_state = next_state = ""
# DFA_dict is dictionary for store DFA information
DFA_dict = {}

# Read file line by line
for line in file1:
    if number_line == 0:
        # Alphabet of DFA
        alphabet = line.strip().split(" ")
    elif number_line == 1:
        # All states in DFA
        states = line.strip().split(" ")
    elif number_line == 2:
        # First state in DFA (Start state)
        first_state = line.strip()
    elif number_line == 3:
        # All final states in DFA
        final_states = line.strip().split(" ")
    else:
        line_strip = line.strip()
        # Example for line_strip : Q0 a Q1
        str_line_strip = line_strip.split(" ")
        # str_line_strip[0] = current state (in this example --> Q0)
        # str_line_strip[1] = input alphabet (in this example --> a)
        # str_line_strip[2] = next state (in this example --> Q1)
        current_state = str_line_strip[0] + " " + str_line_strip[1]
        # current_state = current state + input alphabet (in this example --> "Q0 a")
        next_state = str_line_strip[2]
        DFA_dict[current_state] = next_state
        # DFA_dict in this example --> {"Q0 a":"Q1"}
    number_line += 1

input_string = input()

startState = first_state
nextState = ""
value = 1
# this loop and if condition , denote DFA can build input string or no!
for i in range(0, len(input_string)):
    currentState = startState + " " + input_string[i]
    if (str(currentState) in DFA_dict) and (input_string[i] in alphabet):
        nextState = DFA_dict[currentState]
    else:
        value = 0
        break

    startState = str(nextState)

if (value == 1) and (nextState in final_states):
    print("this string (" + input_string + ") will be accepted")

else:
    print("This string (" + input_string + ") won't be accepted")


