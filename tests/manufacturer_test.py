import unittest
from models.manufacturer import Manufacturer

class TestManufacturer(unittest.TestCase):

    def setUp(self):
        self.manufactuer = Manufacturer("Chanel", "012345678")


    def test_manufacturer_has_name(self):
        self.assertEqual("Chanel", self.manufactuer.name)
    
    def test_manufacturer_has_contact(self):
        self.assertEqual("012345678", self.manufactuer.contact)