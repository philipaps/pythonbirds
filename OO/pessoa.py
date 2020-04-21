class Pessoa:
    def __init__(self, *filhos , nome=None, idade=35):#execultado quando se constroi o objeto
        #self.nome=None#existe mas sem valor
        self.nome=nome#passado o valor do parametro
        self.idade=idade
        self.filhos=list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__=='__main__':
    alves=Pessoa(nome='Alves')
    philip=Pessoa(alves,nome='Philip')#passando alves como atributo filho
    print(Pessoa.cumprimentar(philip))#sem necessidade
    print(id(philip))
    print(philip.cumprimentar())#forma mais usual,o self será passado automaticamente
    print(philip.nome)
    print(philip.idade)
    for filho in philip.filhos:
        print(filho.nome)