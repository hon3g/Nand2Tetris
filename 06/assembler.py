import parser_
import sys


# fetch path to assembly file from command line
asm_file = sys.argv[1]

# read file and append each line to a list
with open(asm_file, 'r') as file:
    asm_code = []
    for line in file:
        asm_code.append(line)

# remove white space, comments, and empty lines
asm_code = parser_.clean_code(asm_code)


print('---------------------')
for i in asm_code:
    print(i)
print('---------------------')
