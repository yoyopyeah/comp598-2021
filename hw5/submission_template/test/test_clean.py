import unittest
from pathlib import Path
import os, sys
parentdir = Path(__file__).parents[1]
sys.path.append(parentdir)
from src.clean import *
import json


class CleanTest(unittest.TestCase):
    def setUp(self):
        # You might want to load the fixture files as variables, and test your code against them. Check the fixtures folder.
        dr = os.path.dirname(__file__)
        fixture1_path = os.path.join(dr, 'fixtures', 'test_1.json')
        fixture2_path = os.path.join(dr, 'fixtures', 'test_2.json')
        fixture3_path = os.path.join(dr, 'fixtures', 'test_3.json')
        fixture4_path = os.path.join(dr, 'fixtures', 'test_4.json')
        fixture5_path = os.path.join(dr, 'fixtures', 'test_5.json')
        fixture6_path = os.path.join(dr, 'fixtures', 'test_6.json')

        with open(fixture1_path) as f:
            self.fixture_1 = f.readline()
        with open(fixture2_path) as f:
            self.fixture_2 = f.readline()
        with open(fixture3_path) as f:
            self.fixture_3 = f.readline()
        with open(fixture4_path) as f:
            self.fixture_4 = f.readline()
        with open(fixture5_path) as f:
            self.fixture_5 = f.readline()
        with open(fixture6_path) as f:
            self.fixture_6 = f.readline()


    def test_title(self):
        print("\nTesting \"title\"")
        self.assertEqual(validate_title(self.fixture_1), False)
        print("OK")
    
    def test_time(self):
        print("\nTesting \"createdAt\"")
        self.assertEqual(validate_time(self.fixture_2), False)
        print("OK")

    def test_valid_json(self):
        print("\nTesting json structure validity")
        self.assertEqual(validate_json(self.fixture_3), False)
        print("OK")

    def test_author(self):
        print("\nTesting \"author\"")
        self.assertEqual(validate_author(self.fixture_4), False)
        print("OK")
    
    def test_total_count(self):
        print("\nTesting \"total_count\"")
        self.assertEqual(validate_count(self.fixture_5), False)
        print("OK")
    
    def test_tags(self):
        print("\nTesting \"tags\"")
        json_obj = json.loads(self.fixture_6)
        tags_true = [word for line in json_obj["tags"] for word in line.split()]
        self.assertEqual(len(validate_tags(self.fixture_6)), len(tags_true))
        print("OK")
       
    
if __name__ == '__main__':
    unittest.main()