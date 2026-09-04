import unittest
import os
from index import process_file


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


if __name__ == "__main__":
    unittest.main()
