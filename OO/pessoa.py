class Pessoa:
    def __init__(self,nome=None,idade=35):#execultado quando se constroi o objeto
        #self.nome=None#existe mas sem valor
        self.nome=nome#passado o valor do parametro
        self.idade=idade

    def cumprimentar(self):
        return f'Ola {id(self)}'


if __name__=='__main__':
    p=Pessoa('Philip')
    print(Pessoa.cumprimentar(p))#sem necessidade
    print(id(p))
    print(p.cumprimentar())#forma mais usual,o self será passado automaticamente
    p.nome='Philip'
    print(p.nome)