import sys


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