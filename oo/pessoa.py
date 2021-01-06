class Pessoa:
    # atributo default ou de classe - definido fora do __init__
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Ola {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')

    print(id(luciano))            #id do objeto
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)

    luciano.sobrenome = 'Ramalho' #criacao dinamica de metodo
    del luciano.filhos            #delecao dinamica de metodo
    luciano.olhos = 1             #atributo de classe modificado (apenas) no escopo do objeto
    print(luciano.__dict__) #conteudo do objeto listado como dicionario
    print(renzo.__dict__)
    print(Pessoa.olhos)     #atributo de classe chamado pela Classe
    print(renzo.olhos)      #atributo de classe chamado pelo objeto
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos)) # ids