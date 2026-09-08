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

def apply_case(tokens):
    i = 0
    result = []
    
    while i < len(tokens):

        if "up" in tokens[i] or "low" in tokens[i] or "cap" in tokens[i]:

            marker, count = parse_case_marker(tokens[i])
            actual_count = min(count, len(result))
        
        result.append(tokens[i])
        i += 1

    return result

def case_apply(token):
    tokens = re.findall(r"\(.*?\)|\S+", token)

    case_functions = {
        "(up)": str.upper,
        "(cap)": str.capitalize,
        "(low)": str.lower
    }

    i = 0
    while i + 1 < len(tokens):
        makers = tokens[i+1]
        if makers in case_functions:
            tokens[i] = case_functions[makers](tokens[i])
            tokens.pop(i+1)
        else:
            i += 1

    return " ".join(tokens)

def parse_case_marker(marker):

    parts = marker.split(",")
    count = 0
    if len(parts) == 1:
        count = 1
    else:
        count = int(parts[1].rstrip(")"))

    if "up" in marker:
        case_type = "up"

    elif "cap" in marker:
        case_type = "cap"

    elif "low" in marker:
        case_type = "low"
    
    return case_type, count


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


