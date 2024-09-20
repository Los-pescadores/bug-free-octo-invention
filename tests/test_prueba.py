#Archivo de ejemplo para las pruebas unitarias.
#El nombre del archivo debe iniciar con el prefijo test_

#Importar unittest para crear las pruebas unitarias
import unittest

#Clase de ejemplo, debe tener un nombre que termina con el sufijo TestCase, y conservar la herencia
class ExampleTestCase(unittest.TestCase):
    #Prueba para verificar que el caso funciona. El nombre del método usa el prefijo test_
    def test_something_1(self):
        self.assertEqual(1,1)   
    def test_something_2(self):
        self.assertEqual(2,2)   
