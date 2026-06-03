import csv, random as rd  # Bibliotecas para manipulação de .csv e valores aleatórios, respectivamente

def palavra_a_advinhar(categoria):  # Recebe um inteiro correspondente a uma das categorias escolhidas

  arquivo = open('Forca.csv', mode='r', encoding='utf-8')  # Leitura do dataset .csv 
  leitor = csv.reader(arquivo) # Variável para ler o arquivo CSV
  leitor_lista = list(leitor)  # Conversão do leitor para lista para facilitar manipulação

  sorteio_linha = rd.randint(1, len(leitor_lista) - 1) # Sorteia uma linha (que corresponde a uma palavra) de alguma coluna (que corresponde a uma categoria fornecida pelo usuário)
  coluna = categoria - 1 # Subtrai 1 do número da categoria, uma vez que conta a partir de 0
  return leitor_lista[sorteio_linha][coluna] # É retornada uma palavra sorteada a partir de uma categoria escolhida pelo jogador