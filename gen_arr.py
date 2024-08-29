#/usr/bin/python

import sys

def bin_to_c_array(bin_file, array_name):
    try:
        with open(bin_file, "rb") as f:
            byte_array = f.read()
    except FileNotFoundError:
        print(f"Error: The file {bin_file} was not found.")
        return

    array_declaration = f"static const unsigned char {array_name}[] = {{\n"

    # Format the byte data into a C array format
    for i, byte in enumerate(byte_array):
        if i % 12 == 0:
            array_declaration += "    "
        array_declaration += f"0x{byte:02X}, "
        if i % 12 == 11 or i == len(byte_array) - 1:
            array_declaration += "\n"

    array_declaration += "};\n"
    
    return array_declaration


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python bin_to_c_array.py <input_file.bin> <array_name>")
        sys.exit(1)

    input_file = sys.argv[1]
    array_name = sys.argv[2]
    
    c_array = bin_to_c_array(input_file, array_name)
    
    if c_array:
        output_file = f"{array_name}.h"
        with open(output_file, "w") as f:
            f.write(c_array)
        print(f"C array declaration saved to {output_file}")

