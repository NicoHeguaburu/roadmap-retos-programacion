import unittest

def suma (a: int, b: int):
    return (a + b)


class TestSuma(unittest.TestCase):

    def test_sumar(self):
        self.assertEqual(suma(2,3),5)
        self.assertEqual(suma(8,3),11)
        self.assertEqual(suma(9,3),12)
        self.assertEqual(suma(2,4),6)



#Ejercicio extra:

data = { 
    "name" : "Nicolás Heguaburu",
    "age" : 22,
    "birth_date" : "12 de julio del 2002",
    "programming_lenguages" : ["python", "javascript", "java"]
}



class TestDataExsist(unittest.TestCase):

    def test_data_exist(self):
        self.assertIn("name", data)
        self.assertIn("age", data)
        self.assertIn("birth_date", data)
        self.assertIn("programming_lenguages", data)

    


class TestDataValue(unittest.TestCase):

    def test_data_value(self):
        self.assertEqual(data["name"], "Nicolás Heguaburu")
        self.assertEqual(data["age"], 22)
        self.assertEqual(data["birth_date"], "12 de julio del 2002")
        self.assertEqual(data["programming_lenguages"], ["python", "javascript", "java"])





if __name__  == "__main__":
    unittest.main()

