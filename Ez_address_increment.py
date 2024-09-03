# Define the file name
filename = "addresses.txt"

# Read the addresses from the file
with open(filename, "r") as file:
    lines = file.readlines()

# Strip whitespace and newline characters from the start and end addresses
start_address = lines[0].strip()
end_address = lines[1].strip()

# Convert start and end addresses to integers
start = int(start_address, 16)
end = int(end_address, 16)

# Generate the addresses with increments of 4 bytes
addresses = []
for addr in range(start, end + 1, 4):
    addresses.append(f"{addr:08X}")

# Write the addresses back to the file
with open(filename, "w") as file:
    for address in addresses:
        file.write(address + "\n")

print(f"The addresses have been written to {filename}")
