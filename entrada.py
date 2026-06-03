import interface as it

#Bloco: Validação da entrada(auxiliares)

def validacao(letra):  #Verifica se a entrada é um único caractere alfabético

  if letra.isalpha() != True or len(letra) != 1:

    it.exibir_aviso_letra("Digite exatamente um caractere alfabético.")  #Exibe mensagem corretiva ao usuário

    return False

  return True  #Retorna booleano


def acento(letra):  #Transforma caracteres com acento nas versões sem acento

  if letra == "Á" or letra == "À" or letra == "Â" or letra == "Ã":
    return "A"
  elif letra == "É" or letra == "È" or letra == "Ê":
    return "E"
  elif letra == "Í" or letra == "Ì" or letra == "Î":
    return "I"
  elif letra == "Ó" or letra == "Ò" or letra == "Ô" or letra == "Õ":
    return "O"
  elif letra == "Ú" or letra == "Ù" or letra == "Û":
    return "U"

  return letra

#----------------

#Bloco: Tratamento de entrada

def entrada():

  validade = False

  letra = it.solicitar_letra()  #Solicita uma sugestão de letra ao usuário

  validade = validacao(letra)  #Verifica se a entrada é um único caractere alfabético

  while(validade == False):  #Caso a verificação falhe, solicita nova entrada

    letra = it.solicitar_letra()

    validade = validacao(letra)

  letra = acento(letra.upper())  #Caso a verificação acerte,
                                 #transforma a entrada em maiúscula
  return letra                   #para tratamento facilitado
#Retorna a entrada adequada

#--------------

#Bloco: Formatador para comparação

def format(palavra):

  slots = []
  for c in palavra:             #Converte a palavra secreta na versão
      if c == " ":              #"descoberta", ou seja, com espaços preenchidos
          slots.append(" ")
      else:
          slots.append(c)

  return " ".join(slots)