import os

LARGURA = 50

ESTAGIOS_FORCA = [
    # Estágio 0 — forca vazia
    [
        "  +------+  ",
        "  |      |  ",
        "  |         ",
        "  |         ",
        "  |         ",
        "  |         ",
        "  +---------",
    ],
    # Estágio 1 — cabeça
    [
        "  +------+  ",
        "  |      |  ",
        "  |      O  ",
        "  |         ",
        "  |         ",
        "  |         ",
        "  +---------",
    ],
    # Estágio 2 — cabeça + corpo
    [
        "  +------+  ",
        "  |      |  ",
        "  |      O  ",
        "  |      |  ",
        "  |         ",
        "  |         ",
        "  +---------",
    ],
    # Estágio 3 — cabeça + corpo + braço esquerdo
    [
        "  +------+  ",
        "  |      |  ",
        "  |      O  ",
        "  |     /|  ",
        "  |         ",
        "  |         ",
        "  +---------",
    ],
    # Estágio 4 — cabeça + corpo + dois braços
    [
        "  +------+  ",
        "  |      |  ",
        "  |      O  ",
        "  |     /|\\ ",
        "  |         ",
        "  |         ",
        "  +---------",
    ],
    # Estágio 5 — cabeça + corpo + braços + perna esquerda
    [
        "  +------+  ",
        "  |      |  ",
        "  |      O  ",
        "  |     /|\\ ",
        "  |     /   ",
        "  |         ",
        "  +---------",
    ],
    # Estágio 6 — boneco completo (derrota)
    [
        "  +------+  ",
        "  |      |  ",
        "  |      O  ",
        "  |     /|\\ ",
        "  |     / \\ ",
        "  |         ",
        "  +---------",
    ],
]

# ============================================================
# UTILITÁRIOS DE TERMINAL
# ============================================================

def limpar_tela():                                     #Limpa a saída de dados
    os.system("cls" if os.name == "nt" else "clear")

def linha_separadora(char="-", largura=LARGURA):       #Cria uma linha separadora para fins de interface
    return char * largura

def centralizar(texto, largura=LARGURA):               #Centraliza o texto para fins de interface
    return texto.center(largura)

def imprimir_cabecalho():                              #Exibe cabeçalho do jogo
    print(linha_separadora("="))
    print(centralizar("J O G O   D A   F O R C A"))
    print(centralizar("UFPA · ICEN · BCC"))
    print(linha_separadora("="))

def exibir_forca(erros):
    """
    Imprime o estágio atual do desenho da forca conforme
    o número de erros cometidos.

    Parâmetros:
        erros (int): quantidade de erros (0 a 6).
    """
    estagio = ESTAGIOS_FORCA[min(erros, 6)]
    print()
    for linha in estagio:
        print("  " + linha)
    print()

def exibir_letras_usadas(letras_corretas, letras_erradas):
    """
    Exibe as letras usadas separadas em corretas e erradas.

    Parâmetros:
        letras_corretas (list): letras acertadas.
        letras_erradas  (list): letras erradas.
    """
    corretas = ", ".join(sorted(letras_corretas)) if letras_corretas else "—"
    erradas = ", ".join(sorted(letras_erradas)) if letras_erradas else "—"
    print(f"  Acertos : {corretas}")
    print(f"  Erros   : {erradas}")

def formatar_palavra(palavra, letras_corretas):
    """
    Formata a palavra para exibição, revelando apenas as letras
    que já foram acertadas pelo jogador. Espaços são preservados.

    Parâmetros:
        palavra        (str):       palavra secreta em maiúsculas.
        letras_corretas (list[str]): letras já acertadas.

    Retorna:
        str: palavra formatada com letras ou underscores.
    """
    slots = []
    for c in palavra:
        if c == " ":
            slots.append(" ")
        elif c in letras_corretas:
            slots.append(c)
        else:
            slots.append("_")
    return " ".join(slots)

def exibir_tela_inicial():
    """
    Exibe a tela inicial com as opções de menu.
    Retorna a opção escolhida pelo usuário (string).
    """
    limpar_tela()
    imprimir_cabecalho()
    print()
    print(centralizar("Bem-vindo ao Jogo da Forca!"))
    print()
    print(linha_separadora())
    print("  1 - Iniciar")
    print("  2 - Sair")
    print(linha_separadora())
    print()
    opcao = input("  Escolha uma opção: ").strip()
    return opcao

def exibir_menu_categorias(categorias):
    """
    Exibe o menu de seleção de categoria.

    Parâmetros:
        categorias (list[str]): lista de nomes de categorias disponíveis.

    Retorna:
        int: índice da categoria escolhida (1-based).
    """
    while True:
        limpar_tela()
        imprimir_cabecalho()
        print()
        print(centralizar("Escolha uma categoria:"))
        print()
        print(linha_separadora())
        for i, cat in enumerate(categorias, start=1):
            print(f"  {i} - {cat}")
        print(linha_separadora())
        print()
        opcao = input("  Digite o número da categoria: ").strip()
        
        if opcao.isdigit():
            opcao_int = int(opcao)
            if 1 <= opcao_int <= len(categorias):
                return opcao_int
        
        print()
        print("  [!] Opção inválida. Tente novamente.")
        input("  Pressione ENTER para continuar...")


def exibir_tela_jogo(palavra, letras_corretas, letras_erradas, erros, categoria):
    """
    Renderiza a tela principal do jogo com todos os componentes:
    forca, palavra, letras usadas e tentativas restantes.

    Parâmetros:
        palavra         (str):       palavra secreta.
        letras_corretas (list[str]): letras acertadas.
        letras_erradas  (list[str]): letras erradas.
        erros           (int):       número de erros cometidos.
        categoria       (str):       categoria da palavra atual.
    """
    limpar_tela()
    imprimir_cabecalho()

    # Categoria e tentativas restantes
    tentativas_restantes = 6 - erros
    print(f"  Categoria : {categoria}")
    print(f"  Tentativas restantes: {tentativas_restantes}")
    print(linha_separadora())

    # Desenho da forca
    exibir_forca(erros)

    # Palavra com slots
    print(linha_separadora())
    palavra_fmt = formatar_palavra(palavra, letras_corretas)
    print()
    print(centralizar(palavra_fmt))
    print()
    print(linha_separadora())

    # Letras usadas
    exibir_letras_usadas(letras_corretas, letras_erradas)
    print(linha_separadora())

    return palavra_fmt


def solicitar_letra():
    """
    Solicita ao jogador que digite uma letra.

    Retorna:
        str: letra digitada em maiúsculo.
    """
    print()
    letra = input("  Digite uma letra: ").strip().upper()
    return letra


def exibir_aviso_letra(mensagem):
    """
    Exibe um aviso relacionado à entrada de letra.

    Parâmetros:
        mensagem (str): texto do aviso a ser exibido.
    """
    print()
    print(f"  [!] {mensagem}")
    print()
    input("  Pressione ENTER para continuar...")


def exibir_tela_vitoria(palavra, erros):
    """
    Exibe a tela de vitória com a palavra revelada e estatísticas.

    Parâmetros:
        palavra (str): palavra que o jogador adivinhou.
        erros   (int): total de erros cometidos na partida.
    """
    limpar_tela()
    imprimir_cabecalho()
    print()
    print(linha_separadora("*"))
    print()
    print(centralizar("PARABENS! VOCE GANHOU! :)"))
    print()
    print(centralizar(f"A palavra era: {palavra}"))
    print()
    erros_txt = f"{erros} erro{'s' if erros != 1 else ''} cometido{'s' if erros != 1 else ''}"
    print(centralizar(erros_txt))
    print()
    print(linha_separadora("*"))
    print()
    input("  Pressione ENTER para continuar...")


def exibir_tela_derrota(palavra):
    """
    Exibe a tela de derrota com o boneco completo e a palavra revelada.

    Parâmetros:
        palavra (str): palavra que o jogador não conseguiu adivinhar.
    """
    limpar_tela()
    imprimir_cabecalho()

    # Exibe o boneco completo (estágio 6)
    exibir_forca(6)

    print(linha_separadora("*"))
    print()
    print(centralizar("VOCE PERDEU!"))
    print()
    print(centralizar(f"A palavra era: {palavra}"))
    print()
    print(linha_separadora("*"))
    print()
    input("  Pressione ENTER para continuar...")


def exibir_tela_saida():
    """Exibe mensagem de encerramento ao sair do jogo."""
    limpar_tela()
    imprimir_cabecalho()
    print()
    print(centralizar("Obrigado por jogar!"))
    print(centralizar("Até a próxima."))
    print()
    print(linha_separadora("="))
    print()


def perguntar_continuar():
    """
    Pergunta se o jogador quer continuar jogando.
    
    Retorna:
        bool: True se quer continuar, False caso contrário
    """
    print()
    print(linha_separadora())
    print(centralizar("MENU PRINCIPAL"))
    print(linha_separadora())
    print("  S - Continuar jogando")
    print("  N - Sair do jogo")
    print(linha_separadora())
    print()
    
    while True:
        opcao = input("  Deseja continuar? (S/N): ").strip().upper()
        if opcao in ['S', 'N']:
            return opcao == 'S'
        print("  Opção inválida! Digite S ou N.")
