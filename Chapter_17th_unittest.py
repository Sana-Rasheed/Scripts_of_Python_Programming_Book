
# Example 1
import unittest 

def  join_names(first, last):
    return ' '.join([first.capitalize(), last.capitalize()])

return_data =  join_names('ahmed', 'hadi')
print(return_data)

class TestStringMethods(unittest.TestCase):  #class is inherited from unittest .testcases
    def  test_is_capitalized(self):
        temp1, temp2 = return_data.split(' ')
        self.assertTrue(temp1.istitle()) # moves to the next line if true
        self.assertTrue(temp2.istitle()) # moves to the next line if true
    def test_length(self):
        self.assertTrue(len(return_data.split(' ')), 2) 
    def test_split(self):
        self.assertEqual(type(return_data), str) # moves to the next line if both are of str type
# End of TestStringMethods class

if __name__ == '__main__':
    unittest.main()


# Output
# Ahmed Hadi
# ----------------------------------------------------------------------
# Ran 3 tests in 0.008s
# OK

# Example 2
return_data =  'Ahmed hadi' # 'Shabir ahmed'
if __name__ == '__main__':
    unittest.main()

# Output
# F..ahmed hadi
# ======================================================================
# FAIL: test_is_capitalized (__main__.TestStringMethods)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "E:\task\Python task\Python\Python\untitled5.py", line 9, in test_is_capitalized
#    self.assertTrue(temp1.istitle())
# AssertionError: False is not true
# ----------------------------------------------------------------------
# Ran 3 tests in 0.076s
# FAILED (failures=1)
