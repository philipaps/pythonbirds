"""
Exercio :motor para controlar a velocidade:
->ter os atributos:
1-atributo velocidade
2-metodo acelerar, incrementando a velocidade de 1 unidade
3-metodo frear decrementa de 2 unidades

->direção com os seguintes atributos:
1-valor de direção possivel:norte, sul, leste, oeste
2-metodo girar a direita
3-metodo girar a esquerda
    n
o       l
    s

"""
NORTE='Norte'
SUL='Sul'
LESTE='Leste'
OESTE='Oeste'

class Carro:
    def __init__(self,direcao,motor):
        self.motor=motor
        self.direcao=direcao

    def calcula_velocidade(self):
        return self.motor.velocidade

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def calcula_direcao(self):
        return  self.direcao.valor

    def girar_a_direita(self):
        self.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_esquerda()


class Direcao:
    rotacao_direita_dct = {NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE}
    rotacao_esquerda_dct= {NORTE:OESTE,OESTE:SUL,SUL:LESTE,LESTE:NORTE}
    def __init__(self):
        self.valor=NORTE

    def girar_direita(self):
        self.valor=self.rotacao_direita_dct[self.valor]
        # if self.valor==NORTE:
        #     self.valor=LESTE
        # elif self.valor==LESTE
        #     self.valor=SUL
        # elif self.valor==SUL:
        #     self.valor=OESTE
            #SE TIVER ESTRUTURA COM MUITOS ELIF  VERIFICAR POSSIBILIDADE DE USAR O DICIONARIO

    def girar_esquerda(self):
        self.valor=self.rotacao_esquerda_dct[self.valor]


class Motor:
    def __init__(self):
        self.velocidade=0

    def acelerar(self):
        self.velocidade+=1

    def frear(self):
        self.velocidade-=2
        self.velocidade=max(0,self.velocidade)

