# Function to reverse the operation of EzPS4PS2LUA.py
def reverse_lua_script(lua_file_path, addresses_file_path, opcodes_file_path):
    with open(lua_file_path, 'r') as lua_file, \
         open(addresses_file_path, 'w') as addresses_file, \
         open(opcodes_file_path, 'w') as opcodes_file:

        for line in lua_file:
            line = line.strip()
            if line.startswith("eeObj.WriteMem32(0x"):
                parts = line.split(', 0x')
                if len(parts) == 2:
                    address = parts[0].split('(0x')[1].strip()
                    opcode = parts[1].split(')')[0].strip()
                    addresses_file.write(address + '\n')
                    opcodes_file.write(opcode + '\n')

# Specify file paths
lua_file_path = "PS2_PS4_Patch.lua"
addresses_file_path = "Addresses.txt"
opcodes_file_path = "Opcodes.txt"

# Execute the function to reverse the Lua script
reverse_lua_script(lua_file_path, addresses_file_path, opcodes_file_path)
