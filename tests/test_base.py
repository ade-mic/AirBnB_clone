# Import the unittest module and the BaseModel class
import unittest
import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    # Define a test method for the __init__ method of the BaseModel class
    def test_init(self):
        # Create an instance of the BaseModel class
        self.base_model = BaseModel()
        # Check that the instance has an id attribute that is a string
        self.assertIsInstance(self.base_model.id, str)
        # Check that the instance has a created_at attribute
        self.assertIsInstance(self.base_model.created_at, datetime.datetime)
        # Check that the instance has an updated_at attribute
        self.assertIsInstance(self.base_model.updated_at, datetime.datetime)

    # Define a test method for the save method of the BaseModel class
    def test_save(self):
        # Save the instance
        self.base_model.save()
        # Check that the updated_at attribute has changed after saving
        self.assertNotEqual(self.base_model.created_at, self.base_model.updated_at)

    # Define a test method for the to_dict method of the BaseModel class
    def test_to_dict(self):
        # Convert the instance to a dictionary
        base_model_dict = self.base_model.to_dict()
        # Check that the dictionary has a __class__ key
        # with the value 'BaseModel'
        self.assertEqual(self.base_model_dict['__class__'], 'BaseModel')
        # Check that the dictionary has an id key with the same
        #  value as the instance id
        self.assertEqual(base_model_dict['id'], self.base_model.id)
        # Check that the dictionary has a created_at key with the
        #  value of the instance created_at in ISO format
        self.assertEqual(base_model_dict['created_at'],
                         self.base_model.created_at.isoformat())
        # Check that the dictionary has an updated_at
        #  key with the value of the instance updated_at in ISO format
        self.assertEqual(base_model_dict['updated_at'],
                         self.base_model.updated_at.isoformat())

    def test_kwargs(self):
        self.base_model.name = "First Model"
        self.base_model.number = 17
        base_model_json = self.base_model.to_dict()
        new_base_model = BaseModel(**base_model_json)
        self.assertIsNot(new_base_model, self.base_model)
        self.assertDictEqual(self.base_model.__dict__, new_base_model.__dict__)

    def test_str_method(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)
    

# Add an entry point to execute the tests from the command line
if __name__ == '__main__':
    unittest.main()
