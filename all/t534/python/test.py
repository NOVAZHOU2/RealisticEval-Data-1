class TestRemoveElementInArray(unittest.TestCase):

    def test_returns_original_array_when_element_not_found(self):
        result = remove_element_in_array([1, 2, 3, 4], 5)
        self.assertEqual(result, [1, 2, 3, 4])

    def test_handles_empty_array_correctly(self):
        result = remove_element_in_array([], 1)
        self.assertEqual(result, [])

    def test_removes_element_from_array_of_objects(self):
        obj1 = {'id': 1}
        obj2 = {'id': 2}
        obj3 = {'id': 3}
        result = remove_element_in_array([obj1, obj2, obj3], obj2)
        self.assertEqual(result, [obj1, obj3])

    def test_does_not_modify_original_array(self):
        original_array = [1, 2, 3]
        result = remove_element_in_array(original_array, 2)
        self.assertEqual(original_array, [1, 2, 3])
        self.assertEqual(result, [1, 3])
