# Define file paths
opcodes_file = 'Opcodes.txt'
addresses_file = 'Addresses.txt'
output_file = 'Patch.pnach'

# Read Opcodes
with open(opcodes_file, 'r') as file:
    opcodes = [line.strip() for line in file]

# Read Addresses
with open(addresses_file, 'r') as file:
    addresses = [line.strip() for line in file]

# Write to output file
with open(output_file, 'w') as file:
    for opcode, address in zip(opcodes, addresses):
        file.write(f'patch=1,EE,{address},word,{opcode}\n')
print(f'Done. The output file is {output_file}.')