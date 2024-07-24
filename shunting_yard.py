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


def compare_precedence(token: str, stack: list) -> bool:
    """Retorna True se a precedencia to token for menor que a precedencia do primeiro elemento da stack"""

    precedence = {"+": 0, "-": 0, "/": 1, "*": 1, "**": 2}

    if stack[0] in precedence:
        return precedence[token] < precedence[stack[0]]
    else:
        return False


def shunting_yard(infix: str) -> list:
    output = []
    stack = []

    while infix:
        token = infix.pop(0)  # pop(0) remove o primeiro elemento de uma lista
        print(f"\nToken: {token}")
        if token.is_numeric():
            print("Token is numeric.")
            output.append(token)

        elif token.is_operator():
            print("Token is operator.")
            while compare_precedence(token, stack):
                output.append(stack.pop(0))

            stack.insert(0, token)

        elif token == "(":
            print("Push bracket into stack.")
            stack.insert(0, token)

        elif token == ")":
            print("Pop operators from the stack until a left bracket is found.")
            operator = stack.pop(0)
            print(f"Operator {operator} poped from stack.")
        else:
            print("An error ocurred.")

    """
    # Essa parte pode não ser necessária
    while stack:
        output.append(stack.pop(0))

    return output
    """


if __name__ == "__main__":
    """
    i = 9 + 24 / ( 7 - 3 )
    i = 9 + 24 / 4
    i = 9 + 6
    i = 15

    RPN
    9 24 7 3 - / +
    """
    infix = "9 + 24  / ( 7 - 3 )"

    print(shunting_yard(infix.split()))
