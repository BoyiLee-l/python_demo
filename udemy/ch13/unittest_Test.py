import unittest
import cap


class MyTest(unittest.TestCase):
    def test_one(self):
        text = "sample"
        result = cap.cap_text(text)
        self.assertEqual(result, "Sample")
    
    def test_two(self):
        text = "just testing"
        result = cap.cap_text2(text)
        self.assertEqual(result, "Just Testing")

if __name__ == "__main__":
    unittest.main()