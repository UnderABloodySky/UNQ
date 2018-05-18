from Persona import *
import unittest

class TestPersona(unittest.TestCase):
    
    def setUp(self):
        
        self.pers = Persona("Martin","Mario","Maria", 10)
    
    def testCambiarNombre(self):
        self.pers.CambiarNombre("Pablo")
        self.assertEqual("Pablo", self.pers.nombre)
        
    def testPadreEsNulo(self):
        Roberto = Persona("Roberto", None, None, 10)
        self.assertEqual(None, Roberto.padre)
    def testMadreEsNulo(self):
        Martina = Persona("Martina", "Paula", "Paula", 10)
        self.assertEqual("Paula", Martina.madre)
    def testLargoNombre(self):
        Pepe = Persona("Pepe", None, None, 10)
        self.assertTrue(len(Pepe.nombre) == 4)
    def testPenPepe(self):
        Pepe = Persona("Pepe", None, None, 10)
        self.assertIn("e" , Pepe.nombre)
    def testPadreNuloYMadreNoNula(self):
        self.assertRaises(HijoAmorfo, Persona, "Pepe", None, "Maria", 10)
    def testMadreNulaYPadreNoNulo(self):
        self.assertRaises(HijoAmorfo, Persona, "Pepe", "Pedrito", None, 10)
    def testWhenEdadEs0ThenExceptionNoNacido(self):
        self.assertRaises(NoNacido, Persona, "Pepe", "Pedrito", "Carla", 0)
    def testWhenEdadEsNoneThenExceptionNoNacido(self):
        self.assertRaises(NoNacido, Persona, "Pepe", "Pedrito", "Carla", None)
    def testWhenEdadEsNoneThenRegexp(self):
        self.assertRaisesRegexp(NoNacido, ,Persona, "Pepe", "Pedrito", "Carla", None)

suite = unittest.TestLoader().loadTestsFromTestCase(TestPersona)
unittest.TextTestRunner(verbosity=2).run(suite)