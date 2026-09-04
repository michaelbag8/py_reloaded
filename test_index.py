import unittest
import os
from index import process_file, apply_hex



class TestProcessFile(unittest.TestCase):

    def setUp(self):
        self.path = "file_in.txt"
        self.out = "file_out.txt"
        self.content = "Hello Michael Welcome home"

    
        with open(self.path, "w") as file:
            file.write(self.content)

    def test_process_file_copies_content(self):
        
        result = process_file(self.path, self.out)

        self.assertEqual(result, self.content)

        with open(self.out, "r") as file:
            output_content = file.read()

        self.assertEqual(output_content, self.content)

    def tearDown(self):
        if os.path.exists(self.path):
            os.remove(self.path)

        if os.path.exists(self.out):
            os.remove(self.out)

class TestApplyHex(unittest.TestCase):
    def test_basic_conversion(self):
        result = apply_hex(["1E", "(hex)"])
        self.assertEqual(result, ["30"])
    
    def test_hex_with_surrounding_words(self):
        result = apply_hex(["The", "value", "is", "1E", "(hex)", "today"])
        self.assertEqual(result, ["The", "value", "is", "30", "today"])

    def test_hex_without_previous_word(self):
        result = apply_hex(["(hex)", "today"])
        self.assertEqual(result, ["(hex)", "today"])
    
    def test_hex_invalid(self):
        result = apply_hex(["hello", "(hex)", "today"])
        self.assertEqual(result,  ["hello", "(hex)", "today"])

if __name__ == "__main__":
    unittest.main()
