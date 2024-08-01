# Pseudocodigo
#
#   Separar cada char da entrada em uma lista, onde cada char é um elemento diferente
#
#   Eliminar espaços
#   Unir numeros maiores que 10 novamente
import re


def lexer(input_string: str) -> list:
    NUMBER = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    OPERATOR = ["+", "-", "*", "/", "(", ")"]

    tokens = []

    """
    São 3 casos, em cada um deles é necessário fazer uma coisa diferente:
    - Se for um espaço ' '  -> descartar o valor
    - Se for um operador    -> copiar o valor pra lista final
    - Se for um numero      -> verificar se os próximos characters são numeros também 
    """
    number_buffer = ""
    for i in input_string:
        if i == " ":
            if number_buffer:
                tokens.append(number_buffer)
                number_buffer = ""

        if i in OPERATOR:
            if number_buffer:
                tokens.append(number_buffer)
                number_buffer = ""
            tokens.append(i)

        if i in NUMBER:
            number_buffer = number_buffer + i

    return tokens


def lexer_antigo(input_string):
    # Define os padrões para diferentes tipos de tokens
    token_specification = [
        ("NUMBER", r"\d+"),  # Números inteiros
        ("OP", r"[+\-*\/]"),  # Operadores (+, -, *, /)
        ("LPAREN", r"\("),  # Parêntese esquerdo
        ("RPAREN", r"\)"),  # Parêntese direito
        ("SKIP", r"[ \t]+"),  # Espaços e tabulações (serão ignorados)
    ]
    tokens = []

    """
    Acho que o problema aqui é que o primeiro FOR busca primeiro os tipos de token, 
    ai primeiro ele pega os numeros, depois os operadores e depois parenteses
    
    Eu acho que não precisa se preocupar com qual tipo o token é por enquanto, só
    dar um jeito de separar eles do jeito certo, dai o primeiro FOR pode ser sobre
    a própria input_string
    """
    for pattern in token_specification:
        # Encontra todos os tokens que correspondem ao padrão
        matches = re.findall(pattern[1], input_string)
        for match in matches:
            if pattern[0] != "SKIP":  # Ignora espaços e tabulações
                if pattern[0] == "NUMBER":
                    tokens.append(int(match))  # Converte números para inteiros
                else:
                    tokens.append(match)
    return tokens


if __name__ == "__main__":
    # exemplo sem permissão de usuario

    """
    input_string = "31 * (4 + 10)"
    input_string = "50+200+49(39/2)"
    tokens = lexer(input_string)
    print(tokens)  # Output: [31, '*', '(', 4, '+', 10, ')']
    """

    # exemplo com o usuario digitando a expressão
    input_string = input("Digite uma expressão matemática: ")
    tokens = lexer(input_string)
    print(tokens)
