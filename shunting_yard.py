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


def precedence(token: str, stack_top: str) -> bool:
    """Retorna True se a precedencia to token for menor que a precedencia do primeiro elemento da stack"""

    precedence = {"+": 0, "-": 0, "/": 1, "*": 1, "^": 2, "(": 0}

    return precedence[token] < precedence[stack_top]


def shunting_yard(infix: list) -> list:
    output = []
    stack = []

    for token in infix:
        print(f"\nToken: {token}")

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

        else:
            print("An error occured")

        print(f"Stack:  {stack}")
        print(f"Output: {output}")

    while stack:
        output.append(stack.pop(0))

    return output


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
    """
    # testes()
    infix = ["9", "+", "24", "/", "(", "7", "-", "3", ")"]

    result = shunting_yard(infix)
    print(result)
