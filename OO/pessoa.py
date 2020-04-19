class Pessoa:
    def cumprimentar(self):
        return 'Ola'


if __name__=='__main__':
    p=Pessoa()
    print(Pessoa.cumprimentar(p))#sem necessidade
    print(id(p))
    print(p.cumprimentar())#forma mais usual,o self será passado automaticamente
