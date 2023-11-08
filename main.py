class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        return f"{self.type}: {self.value}"


class BinOpNode:
    def __init__(self, token, left_node, right_node):
        self.token = token
        self.left_node = left_node
        self.right_node = right_node

    # def __repr__(self):
    #    return f"Binary Operation: {self.left_node} {self.token} {self.right_node}"
    def __repr__(self):
        return f"({self.left_node} {self.get_tok_char()} {self.right_node})"

    def get_tok_char(self):
        value = self.token.value
        if value == "PLUS":
            return "+"
        elif value == "MINUS":
            return "-"
        elif value == "MUL":
            return "*"
        elif value == "DIV":
            return "/"


class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"


class UnaryOpNode:
    def __init__(self, value, node):
        self.value = value
        self.node = node

    def __repr__(self):
        return f"{self.get_tok_char()}{self.node}"

    def get_tok_char(self):
        if self.value == "PLUS":
            return "+"
        elif self.value == "MINUS":
            return "-"


class VarAccessNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"{self.name}: {self.value}"


class VarAssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}: {self.value}"

class PrintNode:
    def __init__(self, message):
        self.message = message

    def __repr__(self):
        return f"print({self.message})"

def error(message):
    print(f"\033[91mERROR\n{message} \033[0m")
    exit()


#Maybe Context Class?

variables = {}


#############################
#       Lexer
#############################

# print("\033[91m test \033[0m")

#code = input("Emocode: ")
file = open("program.txt", "r")
code = file.readlines()
print(code)
tokens = []

for tokens_raw in code:
    tokens_raw = tokens_raw.split(" ")

    for i in range(len(tokens_raw)):
        if len(tokens_raw) == 0:
            break
        if tokens_raw[0] == ":-)":
            tokens.append(Token("OP", "PLUS"))
        elif tokens_raw[0] == ":-(":
            tokens.append(Token("OP", "MINUS"))
        elif tokens_raw[0] == ":-*":
            tokens.append(Token("OP", "MUL"))
        elif tokens_raw[0] == ":-/":
            tokens.append(Token("OP", "DIV"))
        elif tokens_raw[0] == "var":
            tokens.append(Token("ASS", tokens_raw[1]))  # (DEC = Declaration) jetzt nich mehr, war vorher type     ASS für Variable Assign   im moment nur integers
            if len(tokens_raw) < 4 or tokens_raw[2] != "=":
                # raise Exception("A variable cannot be declared without having a value assigned to it")
                error(f"Your code: {tokens_raw[0]} {tokens_raw[1]}\nA variable cannot be declared without having a value assigned to it")

            tokens_raw.remove(tokens_raw[1])
            tokens_raw.remove(tokens_raw[1])
        elif tokens_raw[0] == "print":
            if tokens_raw[1] == ":)" or tokens_raw[1] == ":(":
                tokens.append(Token("FUNC", "PRINT"))
            else:
                error(f"Your code: {tokens_raw[0]} {tokens_raw[1]}\nA print statement must be followed by a number!")
        elif tokens_raw[0] == ":)" or tokens_raw[0] == ":(":
            binaryNumbers = [tokens_raw[0]]


            def collect_binary_values():
                if len(tokens_raw) < 2:
                    return
                if tokens_raw[1] == ":)" or tokens_raw[1] == ":(":
                    binaryNumbers.append(tokens_raw[1])
                    tokens_raw.remove(tokens_raw[1])
                    collect_binary_values()


            collect_binary_values()

            # Calculate final number from binary values
            finalNumber = 0
            counter = 1

            sign = binaryNumbers[0]
            binaryNumbers.remove(binaryNumbers[0])


            def calc_number():
                global finalNumber
                global counter
                if len(binaryNumbers) - 1 < 0:
                    return
                else:
                    if binaryNumbers[len(binaryNumbers) - 1] == ":)":
                        # 2 hoch counter - 1 wird zu final number addiert
                        # print(2 ** (counter - 1))
                        finalNumber += 2 ** (counter - 1)
                    counter += 1
                    binaryNumbers.remove(binaryNumbers[len(binaryNumbers) - 1])
                    calc_number()


            calc_number()

            if sign == ":)":
                tokens.append(Token("SIGN", "MINUS"))
            else:
                tokens.append(Token("SIGN", "PLUS"))

            tokens.append(Token("NUM", finalNumber))

        else:
            tokens.append(Token("ACC", tokens_raw[0])) # ACC für Variable Access
        tokens_raw.remove(tokens_raw[0])

    tokens.append(Token("BREAK", "BREAK"))

print(tokens)

################################
#        PARSER
################################


tok_index = 0



def get_value(start, end):
    if start == end:
        if tokens[start].type == "NUM":
            return NumberNode(tokens[start].value)
        elif tokens[start].type == "ACC":
            return VarAccessNode(tokens[start].value)
    elif (end - start) == 1 and tokens[start].type == "SIGN":
        return UnaryOpNode(tokens[start].value, NumberNode(tokens[end].value))

    tok_index = start

    def find_op(operators):
        global tok_index
        print(tok_index, end)
        if tok_index == end:
            return None
        if tokens[tok_index].type == "OP" and tokens[tok_index].value in operators:
            return tok_index
        tok_index += 1
        return find_op(operators)

    op_index = find_op(("PLUS", "MINUS"))
    # print(op_index)
    if op_index is None:
        tok_index = start
        op_index = find_op(("MUL", "DIV"))

    print(tokens[start:end])

    left_node = get_value(start, op_index - 1)
    right_node = get_value(op_index + 1, end)
    return BinOpNode(tokens[op_index], left_node, right_node)

def create_nodes(start, end):
    global tok_index
    nodes = []

    def find_line_break(start_):
        if tokens[start_].type == "BREAK":
            return start_
        else:
            return find_line_break(start_ + 1)

    break_ = start
    if tokens[start].type == "FUNC":
        if tokens[start].value == "PRINT":
            break_ = find_line_break(start)
            nodes.append(PrintNode(str(get_value(start + 1, break_))))
    if tokens[start].type == "ASS":
        break_ = find_line_break(start)
        nodes.append(VarAssignNode(tokens[start].value, get_value(start + 1, break_)))

    elif start == 0:
        error(f"Your code: {tokens[start]}\nAn expression must contain a function call or an assignment")

    if break_ != end:
        nodes.append(create_nodes(break_ + 1, end))
    return nodes





start_nodes = create_nodes(0, len(tokens) - 1)
print(start_nodes)


#####################################
#          INTERPRETER
#####################################


def traverse_ast(node):
    if type(node).__name__ == "BinOpNode":
        left_value = traverse_ast(node.left_node)
        right_value = traverse_ast(node.right_node)
        op = node.token.value
        if op == "PLUS":
            return left_value + right_value
        elif op == "MINUS":
            return left_value - right_value
        elif op == "MUL":
            return left_value * right_value
        elif op == "DIV":
            return left_value / right_value

    # Brauch ich das eigentlich??
    elif type(node).__name__ == "NumberNode":
        return node.value

    elif type(node).__name__ == "UnaryOpNode":
        number = node.node.value
        if node.value == "MINUS":
            number *= -1

        return number


print(traverse_ast(start_node))
