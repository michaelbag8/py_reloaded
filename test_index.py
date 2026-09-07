import unittest
import os
from index import process_file, apply_hex, apply_bin, apply_case



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

class TestApplyBin(unittest.TestCase):
    def test_basic_conversion(self):
        result = apply_bin(["101", "(bin)"])
        self.assertEqual(result, ["5"])
    
    def test_bin_with_surrounding_words(self):
        result = apply_bin(["The", "value", "is", "101", "(bin)", "today"])
        self.assertEqual(result, ["The", "value", "is", "5", "today"])

    def test_bin_without_previous_word(self):
        result = apply_bin(["(bin)", "today"])
        self.assertEqual(result, ["(bin)", "today"])
    
    def test_bin_invalid(self):
        result = apply_bin(["hello", "(bin)", "today"])
        self.assertEqual(result,  ["hello", "(bin)", "today"])

class TestApplyCase(unittest.TestCase):
    def test_basic_case_up(self):
        result = apply_case(["hello", "(up)"])
        self.assertEqual(result,["HELLO"])

    def test_basic_case_low(self):
        result = apply_case(["HELLO", "(low)"])
        self.assertEqual(result,["hello"])
    
    def test_basic_case_cap(self):
        result = apply_case(["hello", "(cap)"])
        self.assertEqual(result,["Hello"])

    def test_counted(self):
        result = apply_case(["the", "quick", "fox", "(up, 2)"])
        self.assertEqual(result,["the","QUICK","FOX"])

    def test_overflow(self):
        result = apply_case(["the", "quick", "fox", "(up, 5)"])
        self.assertEqual(result,["THE","QUICK","FOX"])

    def test_no_word_before(self):
        result = apply_case(["(up)", "today"])
        self.assertEqual(result,["(up)", "today"])

if __name__ == "__main__":
    unittest.main()
