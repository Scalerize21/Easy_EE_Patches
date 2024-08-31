# Function to process the Patch.pnach file
def process_patch_file(patch_file_path, addresses_file_path, opcodes_file_path):
    with open(patch_file_path, 'r') as patch_file, \
         open(addresses_file_path, 'w') as addresses_file, \
         open(opcodes_file_path, 'w') as opcodes_file:

        for line in patch_file:
            line = line.strip()
            if line.startswith("patch=1,EE,"):
                parts = line.split(',')
                if len(parts) >= 5:
                    address = parts[2]
                    opcode = parts[4]
                    addresses_file.write(address + '\n')
                    opcodes_file.write(opcode + '\n')

# Example usage:
process_patch_file("Patch.pnach", "Addresses.txt", "Opcodes.txt")
