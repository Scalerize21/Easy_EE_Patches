def shift_address(address, steps, direction):
    # Convert the address to an integer from hexadecimal
    address_int = int(address, 16)
    
    # Each step is 2 bytes (which is 4 in hexadecimal)
    shift_value = steps * 4  # 4 in decimal corresponds to 4 hexadecimal digits

    if direction == 'backwards':
        # Shift the address backwards
        new_address_int = address_int - shift_value
    elif direction == 'forwards':
        # Shift the address forwards
        new_address_int = address_int + shift_value
    else:
        raise ValueError("Invalid direction. Must be 'backwards' or 'forwards'.")

    # Return the new address as an 8-digit hexadecimal string, padded with zeros if necessary
    return f"{new_address_int:08x}".upper()

def process_patch_file(filename, steps, direction):
    with open(filename, 'r') as file:
        lines = file.readlines()

    updated_lines = []
    for line in lines:
        if line.startswith('patch='):
            parts = line.strip().split(',')
            if len(parts) >= 4:
                address = parts[2]
                new_address = shift_address(address, steps, direction)
                parts[2] = new_address
                updated_line = ','.join(parts)
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line.strip())
        else:
            updated_lines.append(line.strip())

    return updated_lines

def main():
    direction = input("Shift addresses backwards or forwards? ").strip().lower()
    if direction not in ['backwards', 'forwards']:
        print("Invalid input. Please enter 'backwards' or 'forwards'.")
        return
    
    try:
        steps = int(input("How many steps? "))
    except ValueError:
        print("Invalid input. Please enter a valid number for steps.")
        return

    filename = 'Patch.pnach'
    updated_lines = process_patch_file(filename, steps, direction)

    with open(filename, 'w') as file:
        for line in updated_lines:
            file.write(line + '\n')

    print(f"Addresses have been shifted {direction} by {steps} steps.")

if __name__ == "__main__":
    main()
