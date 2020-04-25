from unittest import  TestCase

from OO.carro import Motor

class CarroTesteCase(TestCase):
    def teste_velocidade_inicial(self):
        #tem que ter prefixo test
        motor=Motor()
        self.assertEqual(0,motor.velocidade)

    def test_acelerar(self):
        motor=Motor()
        motor.acelerar()
        self.assertEqual(1,motor.velocidade)
