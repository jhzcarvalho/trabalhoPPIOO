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

    return tokens


def parser():
    """
    1. num op ( num op num ) op  num
    2. existem 2 opções pro primeiro tokens
        - Pode ser um numero
          se for um numero, ler o proximo token (que deve ser um operador) e depois ler o proximo token (que pode ser um numero ou um '(')
        - Pode ser um (
    

        op1
       /   \   
    num1    op2
           /  \
        num2  num3
    

    num1 op1 ( num2 op2 num3 ) 

    """


def eval_step():
    pass


if __name__ == "__main__":
    input_string = "8 + 5 - 6 + -6"

    tokens = lexer(input_string)
    print(f"Resultado do Lexer: {tokens}")
