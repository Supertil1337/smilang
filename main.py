import sys
# REMOVE LATER
sys.setrecursionlimit(50)


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
        return f"Access: {self.name}"


class VarAssignNode:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}: {self.value}"


class PrintNode:
    def __init__(self, child_node):
        self.child_node = child_node

    def __repr__(self):
        return f"print({self.child_node})"


class LoopNode:
    def __init__(self, child_nodes, iterations):
        self.child_nodes = child_nodes
        self.iterations = iterations

    def __repr__(self):
        return f"Loop({self.iterations})({self.child_nodes})"

class IfNode:
    def __init__(self, condition, child_nodes):
        self.condition = condition
        self.child_nodes = child_nodes
        
    def __repr__(self):
        return f"If({self.condition})Then({self.child_nodes})"

# Comparison(Boolean)    
class ComNode:
    def __init__(self, equality_operator, left_node, right_node):
        self.equality_operator = equality_operator
        self.left_node = left_node
        self.right_node = right_node
        
    def __repr__(self):
        return f"{self.left_node} {self.equality_operator} {self.right_node}"
        
        
# maybe add to token for better errors?
# class Position:


def error(message, code_snippet=None):
    if not code_snippet:
        print(f"\033[91mERROR\n{message} \033[0m")
    else:
        print(f"\033[91mERROR\n{message}\nYour code: {code_snippet} \033[0m")
    exit()


#############################
#       Lexer
#############################

# print("\033[91m test \033[0m")

# code = input("Emocode: ")
file = open("program 2.txt", "r")
code = file.readlines()
tokens = []

for tokens_raw in code:
    tokens_raw = tokens_raw.split(" ")
    for i in range(len(tokens_raw)):
        tokens_raw[i] = tokens_raw[i].strip()
    for i in range(len(tokens_raw)):

        if len(tokens_raw) == 0:
            break
        if not tokens_raw[0]:
            tokens_raw.remove(tokens_raw[0])
            continue
        if tokens_raw[0] == ":-)":
            tokens.append(Token("OP", "PLUS"))
        elif tokens_raw[0] == ":-(":
            tokens.append(Token("OP", "MINUS"))
        elif tokens_raw[0] == ":-*":
            tokens.append(Token("OP", "MUL"))
        elif tokens_raw[0] == ":-/":
            tokens.append(Token("OP", "DIV"))
        elif tokens_raw[0] == "<":
            tokens.append(Token("COM", "SMA"))
        elif tokens_raw[0] == ">":
            tokens.append(Token("COM", "BIG"))
        elif tokens_raw[0] == "==":
            tokens.append(Token("COM", "EQU"))
        elif tokens_raw[0] == "var":
            # tokens.append(Token("ASS", tokens_raw[
            #   1]))  # (DEC = Declaration) jetzt nich mehr, war vorher type     ASS für Variable Assign   im moment nur integers
            # if len(tokens_raw) < 4 or tokens_raw[2] != "=":
            # raise Exception("A variable cannot be declared without having a value assigned to it")
            #    error("A variable cannot be declared without having a value assigned to it",
            #          f"{tokens_raw[0]} {tokens_raw[1]}")

            # tokens_raw.remove(tokens_raw[1])
            # tokens_raw.remove(tokens_raw[1])
            tokens.append(Token("VAR", "VAR"))
        elif tokens_raw[0] == "=":
            tokens.append(Token("EQU", "EQU"))
        elif tokens_raw[0] == "print":
            tokens.append(Token("FUNC", "PRINT"))
        elif tokens_raw[0] == "LOOP":
            tokens.append(Token("LOOP", "START"))
        elif tokens_raw[0] == "IF":
            tokens.append(Token("IF", "START"))
        elif tokens_raw[0] == "END":
            tokens.append(Token("END", "END"))
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

            # if len(tokens_raw) > 2 and tokens_raw[1] == "=":
            # raise Exception("A variable cannot be declared without having a value assigned to it")
            #    tokens.append(Token("ASS", tokens_raw[0]))
            # error("A variable cannot be declared without having a value assigned to it",
            #        f"{tokens_raw[0]} {tokens_raw[1]}")
            # tokens_raw.remove(tokens_raw[1])
            # else:
            #    tokens.append(Token("ACC", tokens_raw[0]))  # ACC für Variable Access
            tokens.append(Token("IDE", tokens_raw[0]))

        tokens_raw.remove(tokens_raw[0])

    tokens.append(Token("BREAK", "BREAK"))

print(tokens)

################################
#        PARSER
################################


tok_index = 0


def get_value(start, end):
    global tok_index
    # print(start, end)
    # print(tokens[start:end+1])
    if start == end:
        if tokens[start].type == "NUM":
            return NumberNode(tokens[start].value)
        elif tokens[start].type == "IDE":
            return VarAccessNode(tokens[start].value)
    elif (end - start) == 1 and tokens[start].type == "SIGN":
        return UnaryOpNode(tokens[start].value, NumberNode(tokens[end].value))

    tok_index = start

    def find_op(type, operators):
        global tok_index
        # print(tok_index, end)
        if tok_index == end:
            return None
        if tokens[tok_index].type == type and tokens[tok_index].value in operators:

            return tok_index
        tok_index += 1
        return find_op(type, operators)

    op_index = find_op("OP", ("PLUS", "MINUS"))
    # print(op_index)
    if not op_index:
        tok_index = start
        op_index = find_op("OP", ("MUL", "DIV"))

    if not op_index:
        tok_index = start
        com_index = find_op("COM", ("EQU", "SMA", "BIG"))
        if not com_index:
            error("No value could be parsed!", tokens[start:end+1])
            
        left_node = get_value(start, com_index - 1)
        right_node = get_value(com_index + 1, end)
        return ComNode(tokens[com_index].value, left_node, right_node)

    left_node = get_value(start, op_index - 1)
    right_node = get_value(op_index + 1, end)
    return BinOpNode(tokens[op_index], left_node, right_node)
    


def return_nodes(start_, end_):
    nodes = []

    def create_nodes(start, end):
        global tok_index

        def find_line_break(_start):
            if tokens[_start].type == "BREAK":
                return _start - 1
            else:
                return find_line_break(_start + 1)

        break_ = start
        if tokens[start].type == "FUNC":
            if tokens[start].value == "PRINT":
                break_ = find_line_break(start)
                nodes.append(PrintNode(get_value(start + 1, break_)))
        elif tokens[start].type == "VAR":
            if tokens[start + 1].type != "IDE" or tokens[start + 2].type != "EQU":
                error("You didn't declare a variable correctly", tokens[start:(start + 2)])
            break_ = find_line_break(start)
            nodes.append(VarAssignNode(tokens[start + 1].value, get_value(start + 3, break_)))
        elif tokens[start].type == "IDE":
            if tokens[start + 1].type != "EQU":
                error("Unknown Error", tokens[start:start+1])
            break_ = find_line_break(start)
            nodes.append(VarAssignNode(tokens[start].value, get_value(start + 2, break_)))
        elif tokens[start].type == "LOOP":
            break_ = find_line_break(start)
            end_key = None
            for tok in tokens:
                if tok.type == "END":
                    end_key = tokens.index(tok)
            if not end_key:
                error("No END keyword was found for a loop!")
            nodes.append(LoopNode(return_nodes(break_ + 1, end_key - 1), get_value(start + 1, break_)))
            break_ = end_key

        elif tokens[start].type == "IF":
            break_ = find_line_break(start)
            end_key = None
            for tok in tokens:
                if tok.type == "END":
                    end_key = tokens.index(tok)
            if not end_key:
                error("No END keyword was found for an if statement!")
            nodes.append(IfNode(get_value(start + 1, break_), return_nodes(break_ + 1, end_key - 1)))
            break_ = end_key

        elif start == 0:
            error("An expression must contain a function call or an assignment", f"{tokens[start]}")

        if break_ != end:
            # print(tokens)
            create_nodes(break_ + 1, end)

    create_nodes(start_, end_)
    return nodes


start_nodes = return_nodes(0, len(tokens) - 1)
print(start_nodes)

#####################################
#          INTERPRETER
#####################################


# Maybe Context Class?

variables = {}


def traverse_ast(node):
    type_ = type(node).__name__
    if type_ == "BinOpNode":
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
    elif type_ == "NumberNode":
        return node.value

    elif type_ == "UnaryOpNode":
        number = node.node.value
        if node.value == "MINUS":
            number *= -1

        return number

    elif type_ == "VarAssignNode":
        variables[node.name] = traverse_ast(node.value)
        # print(f"Assigned {node.value} to {node.name}")
        return None

    elif type_ == "VarAccessNode":
        if not variables.get(node.name):
            error("Unknown Error, did you spell something wrong?")
        return variables[node.name]

    elif type_ == "PrintNode":
        print(traverse_ast(node.child_node))

    elif type_ == "LoopNode":
        for _ in range(traverse_ast(node.iterations)):
            for node_ in node.child_nodes:
                traverse_ast(node_)
                
    elif type_ == "IfNode":
        op = node.condition.equality_operator
        condition = False
        left_node = node.condition.left_node
        right_node = node.condition.right_node
        if op == "SMA":
            condition = traverse_ast(left_node) < traverse_ast(right_node)
        elif op == "BIG":
            condition = traverse_ast(left_node) > traverse_ast(right_node)
        elif op == "EQU":
            condition = traverse_ast(left_node) == traverse_ast(right_node)
        if condition:
            for node_ in node.child_nodes:
                traverse_ast(node_)


for node in start_nodes:
    traverse_ast(node)
