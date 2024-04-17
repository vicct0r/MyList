# Implementando o protocolo do Iterator em Python
# Essa é apenas uma aula para introduzir os protocolos de collections.abc no
# Python. Qualquer outro protocolo poderá ser implementando seguindo a mesma
# estrutura usada nessa aula.
# https://docs.python.org/3/library/collections.abc.html

from collections.abc import Sequence

class MyList(Sequence):
    def __init__(self):
        self._data = {}
        self._index = 0
        self._next_index = 0
    
    def append(self, *values):
        for value in values:
            self._data[self._index] = value
            self._index += 1

# Sequence me faz ter que definir alguns métodos para seu funcionamento;
# __len__ e __getitem__ são os principais para o funcionamento do Sequence que foi herdado pela classe.

    def __len__(self) -> int:
        return self._index


    def __getitem__(self, index):
        return self._data[index]

    # Permitindo mudar os valores da lista passando o índice 
    def __setitem__(self, index, value):
        self._data[index] = value


    def __iter__(self):
        return self

    # Tratando o erro do __next__;
    # Se eu não fizer um condicional passando o próximo index, ele irá procurar pelo proximo
    # valor mesmo que ele ultrapasse o tamanho total da lista. 

    def __next__(self):
        if self._next_index >= self._index:
            # é crucial voltar next_index para 0;
            # Pois o __next__ ele só percorre os itens uma vez, e fica salvo no último valor.
            # Então zerar permite com que eu possa percorrer os itens do objeto (lista) mais de uma vez no mesmo código.
            self._next_index = 0 
            raise StopIteration
        
        value = self._data[self._next_index]
        self._next_index += 1
        return value


# Testando o meu objeto MyList:

lista = MyList()
lista.append('João')
lista[0] = 'Victor'
lista.append('Inacio')
lista.append('Marcelo', 'Silva', 'Tavares')

# Por mais que os valores da minha lista estejam armazenados em um dicionário;
# Ele se comporta como uma lista pois a chave do dict é o index da minha 'Lista'.
for index, item in enumerate(lista):
    print(index, item)