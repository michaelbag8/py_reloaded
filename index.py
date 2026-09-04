import sys


def apply_hex(tokens):
    i = 0
    result = []
    
    while i < len(tokens):
        # Check bounds before looking ahead
        if i + 1 < len(tokens):
            # Check if the next token marks this as a hex token
            if tokens[i + 1] == "(hex)":
                try:
                    # Branch B: Try converting and consume 2 tokens
                    converted_val = str(int(tokens[i], 16))
                    result.append(converted_val)
                except ValueError:
                    # If invalid hex, print warning and append the original raw token
                    print(f"Warning: '{tokens[i]}' is an invalid hex string.")
                    result.append(tokens[i])
                    result.append(tokens[i+1])
                    
                
                i += 2
                continue

        # Branch A: Append unchanged and consume 1 token
        result.append(tokens[i])
        i += 1

    return result





def process_file(input_path, output_path):

    with open(input_path, "r") as file:
        content = file.read()
    
    result = apply_hex(content)

    with open(output_path, "w") as file:
        file.write(result)

    return result


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 input.txt output.txt")
        sys.exit()
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)

if __name__ == "__main__":
    main()