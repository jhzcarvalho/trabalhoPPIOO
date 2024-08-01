# Pseudocodigo
#
#   Separar cada char da entrada em uma lista, onde cada char é um elemento diferente
#
#   Eliminar espaços
#   Unir numeros maiores que 10 novamente


def lexer(input_string):
    # Define os padrões para diferentes tipos de tokens
    token_specification = [
        ('NUMBER',   r'\d+'),         # Números inteiros
        ('OP',       r'[+\-*\/]'),    # Operadores (+, -, *, /)
        ('LPAREN',   r'\('),          # Parêntese esquerdo
        ('RPAREN',   r'\)'),          # Parêntese direito
        ('SKIP',     r'[ \t]+'),      # Espaços e tabulações (serão ignorados)
    ]
    tokens = []
    for pattern in token_specification:
        # Encontra todos os tokens que correspondem ao padrão
        matches = re.findall(pattern[1], input_string)
        for match in matches:
            if pattern[0] != 'SKIP':  # Ignora espaços e tabulações
                if pattern[0] == 'NUMBER':
                    tokens.append(int(match))  # Converte números para inteiros
                else:
                    tokens.append(match)
    return tokens


if __name__ == "__main__":
    # exemplo sem permissão de usuario
    
    input_string = "31 * (4 + 10)"
    input_string = "50+200+49(39/2)"
    tokens = lexer(input_string)
    print(tokens)  # Output: [31, '*', '(', 4, '+', 10, ')']


    # exemplo com o usuario digitando a expressão
    """
    input_string = input("Digite uma expressão matemática: ")
    tokens = lexer(input_string)
    print(tokens)
    """
