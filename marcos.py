class Node:
    def __init__(self, value, left=None, right=None):
        # Inicializa um nó com o valor dado, e filhos esquerdo e direito opcionais
        self.value = value
        self.left = left
        self.right = right


def to_string(node):
    if not node:
        return ""
    # Se é uma folha (número), retorna o valor como string
    if not node.left and not node.right:
        return str(node.value)
    # Se é um operador, precisamos de parênteses para a expressão
    left_expr = to_string(node.left)
    right_expr = to_string(node.right)
    # Retorna a expressão no formato "(esquerda operador direita)"
    return f"({left_expr} {node.value} {right_expr})"


def parse_expression(expression):
    # Pilhas para nós e operadores
    nodes = []
    operators = []

    i = 0
    while i < len(expression):
        if expression[i].isdigit():
            # Constrói um número a partir de dígitos consecutivos
            num = 0
            while i < len(expression) and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            nodes.append(Node(num))  # Adiciona o número como um nó folha
            i -= 1  # Ajusta o índice após processamento do número
        elif expression[i] == "(":
            operators.append(
                expression[i]
            )  # Adiciona parênteses de abertura à pilha de operadores
        elif expression[i] == ")":
            # Processa até encontrar um parênteses de abertura
            while operators and operators[-1] != "(":
                right = nodes.pop()
                left = nodes.pop()
                op = operators.pop()
                nodes.append(Node(op, left, right))
            operators.pop()  # Remove o parênteses de abertura
        elif expression[i] in "+-*/":
            # Processa operadores de acordo com a precedência
            while (
                operators
                and operators[-1] != "("
                and precedence(operators[-1]) >= precedence(expression[i])
            ):
                right = nodes.pop()
                left = nodes.pop()
                op = operators.pop()
                nodes.append(Node(op, left, right))
            operators.append(expression[i])
        i += 1

    # Processa operadores restantes na pilha
    while operators:
        right = nodes.pop()
        left = nodes.pop()
        op = operators.pop()
        nodes.append(Node(op, left, right))

    # O último nó restante é a raiz da árvore de expressão
    return nodes[0]


def precedence(op):
    # Define a precedência dos operadores
    if op in "+-":
        return 1
    if op in "*/":
        return 2
    return 0


if __name__ == "__main__":
    # Construção manual de uma árvore de expressão para a expressão: 31 * (4 + 10)

    tree1 = Node("*", Node(31), Node("+", Node(4), Node(10)))

    # Recebe a expressão matemática do usuário
    user_input = input("Digite uma expressão matemática: ")
    # Constrói a árvore de expressão a partir da entrada do usuário
    tree = parse_expression(user_input)
    # Converte a árvore de expressão em uma string
    expression_str = to_string(tree)
    expression_str1 = to_string(tree1)
    # Imprime a expressão reconstruída da árvore gerada pelo usuário
    print("Expressão reconstruida:", expression_str1)
    print("Expressão reconstruída:", expression_str)
