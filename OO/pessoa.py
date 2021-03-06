class Pessoa:
    olhos=2
    def __init__(self, *filhos , nome=None, idade=35):#execultado quando se constroi o objeto
        #self.nome=None#existe mas sem valor
        self.nome=nome#passado o valor do parametro
        self.idade=idade
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'Ola meu nome é {self.nome}'

class Homem(Pessoa):
    def cumprimentar(self):
        #cumprimentar_classepai=Pessoa.cumprimentar(self)#passando o atual objeto
        #da forma mais correta
        cumprimentar_classepai = super().cumprimentar()
        return f'{cumprimentar_classepai}, Aperto de mão'

class Mutante(Pessoa):
    olhos=3

if __name__=='__main__':
    alves=Mutante(nome='Alves')
    #herdando de pessoa como alternativa poredera ser:
    #alves = Homem(nome='Alves')
    philip=Homem(alves,nome='Philip')#passando alves como atributo filho
    print(Pessoa.cumprimentar(philip))#sem necessidade
    print(id(philip))
    print(philip.cumprimentar())#forma mais usual,o self será passado automaticamente
    print(philip.nome)
    print(philip.idade)
    for filho in philip.filhos:
        print(filho.nome)
    #atributo dinamico em tempo de execulsão
    philip.sobrenome=nome='Fulano'
    print(philip.sobrenome)#somente pra este objeto
    del philip.filhos #remove dinamicamente
    philip.olhos=1
    #del philip.olhos
    print(philip.__dict__)
    print(alves.__dict__)
    print(Pessoa.olhos)#viavel pois é um atributos de classe
    print(alves.olhos)
    print(id(Pessoa.olhos),id(philip.olhos))
    pessoa=Pessoa('anonimo')
    print(isinstance(pessoa,Pessoa))
    #==========================
    print(philip.cumprimentar())
    print(alves.cumprimentar())
