# Pseudocodigo
#
#   While there are tokens to be read:
#       Read a token
#
#       If it's a number
#           add it to queue
#
#       If it's an operator
#           While there's an operator on the top of the stack with greater precedence:
#               Pop operators from the stack onto the output queue
#           Push the current operator onto the stack
#
#       If it's a left bracket
#           push it onto the stack
#
#       If it's a right bracket
#           While there's not a left bracket at the top of the stack:
#               Pop operators from the stack onto the output queue.
#           Pop the left bracket from the stack and discard it
#
#   While there are operators on the stack, pop them to the queue


NUMBER = "0123456789"
OPERATOR = "+-*/()"


def precedence(token: str, stack_top: str) -> bool:
    """Retorna True se a precedencia to token for menor que a precedencia do primeiro elemento da stack"""

    precedence = {"+": 1, "-": 1, "/": 2, "*": 2, "(": 0}

    return precedence[token] <= precedence[stack_top]


def lexer(input_string: str) -> list:
    tokens = []

    input_list = input_string.split(" ")

    """
    São 3 casos, em cada um deles é necessário fazer uma coisa diferente:
    - Se for um espaço ' '  -> descartar o valor
    - Se for um operador    -> copiar o valor pra lista final
    - Se for um numero      -> verificar se os próximos characters são numeros também 
    """

    for i in input_list:
        if "(" in i:
            tokens.append("(")
            tokens.append(i.split("(")[1])
        elif ")" in i:
            tokens.append(i.split(")")[0])
            tokens.append(")")
        else:
            tokens.append(i)
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

    if number_buffer:
        tokens.append(number_buffer)

    """
    return tokens


def shunting_yard(infix: list) -> list:
    output = []
    stack = []

    for token in infix:
        # print(token)

        if token.isnumeric():
            output.append(token)

        elif token in ["+", "-", "/", "*", "^"]:
            # a verificação do valor de stack é resolvido primeiro, caso a lista esteja vazia
            # o valor retornado será False resolvendo o operador lógico AND sem que o valor
            # de stack[0] seja testado
            while stack and precedence(token, stack[0]):
                output.append(stack.pop(0))
            stack.insert(0, token)

        elif token == "(":
            stack.insert(0, token)

        elif token == ")":
            while stack[0] != "(":
                output.append(stack.pop(0))
            stack.pop(0)

        # Gambiarra, se tiver um sinal de menos o isnumeric() retorna falso
        # Se o primeiro valor do token for '-' testa o segundo valor
        elif len(token) > 1 and token[1].isnumeric():
            output.append(token)

        else:
            print("An error occured")

    while stack:
        op = stack.pop(0)

        if op != "(":
            output.append(op)

    return output


def eval_step(tokens: list):
    """
    1. Percorrer a lista
    2. Verificar se o token é NUMBER ou OPERATOR
        - Se for NUMBER salvar em uma pilhas
        - Se for OPERATO ftR remover dois numeros do topo da pilha,
          realizar a operação e add o resultado no topo da pilha
    3. Repetir até chegar ao final da lista de tokens
    4. Se nenhum erro ocorreu, a pilha deverá conter somente um numero, retornar a resposta

    Deve ser possivel fazer recursivamente, mas não sei como...
    """
    number_stack = []

    for token in tokens:
        print(f"{token} - {number_stack}")

        if token in OPERATOR:
            right_num = number_stack.pop(0)
            left_num = number_stack.pop(0)

            if token == "+":
                number_stack.insert(0, left_num + right_num)
            elif token == "-":
                number_stack.insert(0, left_num - right_num)
            elif token == "*":
                number_stack.insert(0, left_num * right_num)
            elif token == "/":
                number_stack.insert(0, left_num // right_num)

        else:
            number_stack.insert(0, int(token))

    return number_stack[0]


def testes():
    caso1 = ["31", "*", "(", "4", "+", "10", ")"]
    caso2 = ["1", "+", "3"]

    assert shunting_yard(caso1) == ["31", "4", "10", "*", "+"]
    assert shunting_yard(caso2) == ["1", "3", "+"]


if __name__ == "__main__":
    """
    i = 9 + 24 / ( 7 - 3 )
    i = 9 + 24 / 4
    i = 9 + 6
    i = 15

    RPN
    9 24 7 3 - / +
    9 24 4 / +
    9 6 +
    15
    # testes()
    """
    # input_string = input("Digite uma expressão matemática: ")
    test_list = [
        "9 + 24 / ( 7 - 3 )",
        "1 + 3",
        "1 + 6",
        "4 / 2 + 7",
        "55 * 48 * -44 - -32 + 1 * -80 * -94 - 74 * -53 + -30 + -61",
        "(2 - 65 - (-24 + -97) * -5 * -61) * (-41 + 85 * 9 * -92 * (75 - 18))",
        "-20 + -51 + 20 + -68 * -11 + -35 * -14 - 95 - 32 + -52 * -23 - -90 * -42",
    ]

    for input_string in test_list:
        print()
        token_list = lexer(input_string)
        print(f"token list{token_list}")
        rpn = shunting_yard(token_list)
        print(rpn)
        result = eval_step(rpn)
        print(result)
    # print(solve_step(9, 2, "/"))
