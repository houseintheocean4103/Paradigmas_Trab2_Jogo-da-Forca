import interface as it
import logica as log

def menu():  #Função principal

  opcao = it.exibir_tela_inicial()  #Exibe a tela inicial e solicita o início do jogo ou seu encerramento

  if opcao == '1':  #Caso um jogo seja iniciado:

    novo_jogo = False

    log.jogo()  #Executa uma rodada de forca

    novo_jogo = it.perguntar_continuar()  #Pergunta ao usuário se um novo jogo será iniciado ou se a aplicação deve ser encerrada

    while(novo_jogo == True):  #Caso o usuário deseje continuar, o programa criará novas rodadas

      log.jogo()

      novo_jogo = it.perguntar_continuar()

    it.exibir_tela_saida()  #Exibe mensagem de encerramento do jogo

  else:

    it.exibir_tela_saida()  #Caso um jogo seja imediatamente fechado: