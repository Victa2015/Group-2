import unittest
import Contact from my_contact

class TestMyContacts(unittest.TestCase):

	def test_search_function_using_expected_input(self):
		"""passes a name that can be found in the dictionary
		  and tests the result against the expected output 
		"""