import dados as dd
import entrada as ent
import interface as it

#----------------

#Bloco: atualização do avanço do jogador


def atualiza(palavra_secreta, avanco):  #Compara a palavra parcialmente preenchida com a versão descoberta

  if ent.format(palavra_secreta) == avanco:
    return True
  return False

#----------------

#Bloco: Lógica do jogo/Verificação da sugestão


def jogo():

  avanco = ""            #Controlador de avanço
  letras_corretas = []   #Lista de letras corretas
  letras_erradas = []    #Lista de letras erradas
  erros = 0              #Número de erros
  historico = []         #Lista de todas as letras sugeridas
  nomes_categorias = ["Animais",  #Lista de nomes das categorias
                      "Comidas",
                      "Livros",
                      "Filmes",
                      "Objetos"]


  cat = it.exibir_menu_categorias(nomes_categorias)  #Solicita a escolha da categoria(tema)

  palavra = dd.palavra_a_advinhar(cat)  #Sorteia uma palavra daquela categoria

  it.exibir_tela_jogo(palavra, letras_corretas, letras_erradas, erros, nomes_categorias[cat - 1])  #Exibe interface de acordo com o desempenho do jogador

  while(erros <= 6):  #Loop do jogo(máximo de 6 tentativas

    letra = ent.entrada() #Tratamento de entrada

    if letra in historico:  #Verifica sugestões repetidas

      it.exibir_aviso_letra("Esta letra já foi sugerida.")  #Exibe mensagem corretiva ao usuário

    elif letra in palavra and letra not in letras_corretas:

      letras_corretas.append(letra)  #Inclui letra acertada na lista de acertos

      avanco = it.exibir_tela_jogo(palavra, letras_corretas, letras_erradas, erros, nomes_categorias[cat - 1])  #Retorna o estado parcial da palavra

      if atualiza(palavra, avanco):  #Finaliza o jogo se a palavra for preenchida em sua totalidade

        it.exibir_tela_vitoria(palavra, erros)  #Exibe tela de vitória

        break  #Encerra  o jogo


    else:

      letras_erradas.append(letra)  #Inclui letra errada na lista de erros

      erros += 1  #Incrementa/Gasta uma tentativa

      it.exibir_tela_jogo(palavra, letras_corretas, letras_erradas, erros, nomes_categorias[cat - 1])  #Exibe interface de acordo com o desempenho do jogador


    historico.append(letra)  #inclui sugestão no histórico geral

  if erros == 7:      #Saída do loop determina derrota

    it.exibir_tela_derrota(palavra)