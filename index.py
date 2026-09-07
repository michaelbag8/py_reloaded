import sys


def apply_hex(tokens):
    i = 0
    result = []
    
    while i < len(tokens):
       
        if i + 1 < len(tokens):
         
            if tokens[i + 1] == "(hex)":
                try:
                    
                    converted_val = str(int(tokens[i], 16))
                    result.append(converted_val)
                except ValueError:
                    
                    print(f"Warning: '{tokens[i]}' is an invalid hex string.")
                    result.append(tokens[i])
                    result.append(tokens[i+1])
                
                i += 2
                continue

        result.append(tokens[i])
        i += 1

    return result

def apply_bin(tokens):
    i = 0
    result = []
    
    while i < len(tokens):
        
        if i + 1 < len(tokens):
        
            if tokens[i + 1] == "(bin)":
                try:
                    
                    converted_val = str(int(tokens[i], 2))
                    result.append(converted_val)
                except ValueError:
                    
                    print(f"Warning: '{tokens[i]}' is an invalid bin string.")
                    result.append(tokens[i])
                    result.append(tokens[i+1])
                
                i += 2
                continue
        
        result.append(tokens[i])
        i += 1

    return result



def process_file(input_path, output_path):

    with open(input_path, "r") as file:
        content = file.read()
    

    with open(output_path, "w") as file:
        file.write(content)

    return content


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 input.txt output.txt")
        sys.exit()
    
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)

if __name__ == "__main__":
    main()


