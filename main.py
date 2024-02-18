import sys
import subprocess
from termcolor import colored
from math import floor


def handler(type, value, tb):
    print("An unknown exception occured while executing the program""\n"
          f"Python Output: {type, value, tb}")
    subprocess.run(["pause"], shell=True)


# sys.excepthook = handler


class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type}: {self.value} ({self.line})"


class BasicOpNode:
    def __init__(self, token, left_node, right_node, line):
        self.line = line
        self.token = token
        self.left_node = left_node
        self.right_node = right_node

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
    def __init__(self, sign, value, line):
        self.line = line
        self.sign = sign
        self.value = value

    def __repr__(self):
        return f"{self.get_tok_char()}{self.value}"

    def get_tok_char(self):
        if self.sign == "PLUS":
            return "+"
        elif self.sign == "MINUS":
            return "-"


class StringNode:
    def __init__(self, value, line):
        self.value = value
        self.line = line

    def __repr__(self):
        return f'"{self.value}"'


class VarAccessNode:
    def __init__(self, name, line):
        self.line = line
        self.name = name

    def __repr__(self):
        return f"Access: {self.name}"


class VarAssignNode:
    def __init__(self, name, value, line):
        self.line = line
        self.name = name
        self.value = value

    def __repr__(self):
        return f"{self.name}: {self.value}"


class PrintNode:
    def __init__(self, child_node, line):
        self.line = line
        self.child_node = child_node

    def __repr__(self):
        return f"print({self.child_node})"


class LoopNode:
    def __init__(self, child_nodes, iterations, line):
        self.line = line
        self.child_nodes = child_nodes
        self.iterations = iterations

    def __repr__(self):
        return f"Loop({self.iterations})({self.child_nodes})"


class IfNode:
    def __init__(self, condition, child_nodes, else_nodes, line):
        self.line = line
        self.condition = condition
        self.child_nodes = child_nodes
        self.else_nodes = else_nodes

    def __repr__(self):
        return f"If({self.condition})Then({self.child_nodes})Else({self.else_nodes})"


class ElseNode:
    def __init__(self, child_nodes, line):
        self.child_nodes = child_nodes
        self.line = line

    def __repr__(self):
        return f"{self.child_nodes}"


# Comparison(Boolean)
class ComNode:
    def __init__(self, equality_operator, left_node, right_node, line):
        self.line = line
        self.equality_operator = equality_operator
        self.left_node = left_node
        self.right_node = right_node

    def __repr__(self):
        return f"{self.left_node} {self.equality_operator} {self.right_node}"


def error(message, line):
    if line:
        print(colored(f"ERROR\n{message}\nYour code (Line {line}): {code[line - 1]}", "red", force_color=True))
    else:
        print(colored(f"ERROR\n{message}", "red", force_color=True))
    subprocess.run(["pause"], shell=True)
    exit()


chars = [["a", "b", "c", "d", "e"], ["f", "g", "h", "i", "j"], ["k", "l", "m", "n", "o"], ["p", "q", "r", "s", "t"],
         ["u", "v", "w", "x", "y"], "z"]

token_dict = {
    ":-)": ["OP", "PLUS"],
    ":-(": ["OP", "MINUS"],
    ":-*": ["OP", "MUL"],
    ":-/": ["OP", "DIV"],
    ":<": ["COM", "SMA"],
    ":>": ["COM", "BIG"],
    ":=)": ["COM", "EQU"],
    ":=(": ["COM", "UNEQU"],
    "=)": ["ASS", "EQU"],
    ":p": ["FUNC", "PRINT"],
    "8-)": ["LOOP", "START"],
    "xD": ["IF", "STATEMENT"],
    "XD": ["ELSE", "STATEMENT"],
    ";-]": ["END", "END"],
    ":^)": ["STRING", "1"],
    ":-]": ["STRING", "2"],
    "=]": ["STRING", "3"],
    ":]": ["STRING", "4"],
    ":D": ["STRING", "5"],
    ":-D": ["STRING", "6"],
    ":))": ["STRING", "UPPER"],
    ":)": ["NUM", "1"],
    ":(": ["NUM", "0"],
    ";)": ["NAME", "1"],
    ";-)": ["NAME", "2"],
    ";D": ["NAME", "3"],
    ":P": ["NAME", "4"],
    ":-o": ["NAME", "5"],
    "://": ["COMM", "COMM"]
}

debug = False

#############################
#       Lexer
#############################


try:
    file = open(sys.argv[1], "r")
except (OSError, IndexError):
    error("Something went wrong while trying to read the file", None)
print(f"Executing {sys.argv[1]}")
code = file.readlines()
file.close()
tokens = []
line = 1

for tokens_raw in code:
    tokens_raw = tokens_raw.split(" ")

    for i in range(len(tokens_raw)):
        tokens_raw[i] = tokens_raw[i].strip()

    for i in range(len(tokens_raw)):
        if len(tokens_raw) == 0:
            break

        tok = tokens_raw[0]

        if not tok:
            del tokens_raw[0]
            continue

        token = token_dict.get(tok)
        if token:
            if token[0] == "COMM":
                break
            tokens.append(Token(token[0], token[1], line))
        else:
            error("An error occured while tokenizing this line", line)

        del tokens_raw[0]

    tokens.append(Token("BREAK", "BREAK", line))
    line += 1

if debug:
    print(tokens)

################################
#        PARSER
################################


def parse_number(start, end):
    num = ""
    sign = tokens[start].value
    for token in tokens[start + 1:end + 1]:
        num += token.value

    try:
        num = int(num, 2)
    except Exception:
        error("No value could be parsed", tokens[start].line)

    if sign == "1":
        return NumberNode("MINUS", num, tokens[start].line)
    elif sign == "0":
        return NumberNode("PLUS", num, tokens[start].line)
    else:
        error("Something went wrong while parsing this line (and I have no idea what did)", tokens[start].line)


def parse_string(start, end):
    cur_tok = start

    def get_char():
        nonlocal cur_tok

        if tokens[cur_tok].type != "STRING":
            error("No value could be parsed", tokens[cur_tok].line)

        if tokens[cur_tok].value == "UPPER":
            cur_tok += 1
            return get_char().upper()
        elif tokens[cur_tok].value == 6:
            cur_tok -= 1
            return chars[5]
        else:
            return chars[int(tokens[cur_tok].value) - 1][int(tokens[cur_tok + 1].value) - 1]

    string = ""
    while cur_tok <= end:
        string += get_char()
        cur_tok += 2

    return StringNode(string, tokens[start].line)


def parse_name(start):
    name = ""
    for tok in tokens[start:start + 5]:
        if tok.type == "NAME":
            name += tok.value
        else:
            break
    return name


def find_op(type, operators, tok_index, end):
    if tok_index == end:
        return None

    if tokens[tok_index].type == type and tokens[tok_index].value in operators:
        return tok_index

    tok_index += 1
    return find_op(type, operators, tok_index, end)


def get_condition(start, end):
    com_index = find_op("COM", ("EQU", "SMA", "BIG", "UNEQU"), start, end)
    if not com_index:
        error("No comparison operator was found within the condition of an if statement", tokens[start].line)

    left_node = get_value(start, com_index - 1)
    right_node = get_value(com_index + 1, end)
    return ComNode(tokens[com_index].value, left_node, right_node, tokens[com_index].line)


def get_basic_op_node(start, end):
    op_index = find_op("OP", ("PLUS", "MINUS"), start, end)

    if not op_index:
        op_index = find_op("OP", ("MUL", "DIV"), start, end)

    if not op_index:
        return None

    left_node = get_value(start, op_index - 1)
    right_node = get_value(op_index + 1, end)
    return BasicOpNode(tokens[op_index], left_node, right_node, tokens[op_index].line)


def get_value(start, end):
    basic_op = get_basic_op_node(start, end)
    if not basic_op:
        if tokens[start].type == "STRING":
            return parse_string(start, end)
        elif tokens[start].type == "NUM":
            return parse_number(start, end)
        elif tokens[start].type == "NAME":
            return VarAccessNode(parse_name(start), tokens[start].line)
        else:
            error("No value could be parsed", tokens[start].line)
    return basic_op


def return_nodes(start_, end_):
    nodes = []

    def create_nodes(start, end):
        def find_line_break(_start):
            if tokens[_start].type == "BREAK":
                return _start - 1
            else:
                return find_line_break(_start + 1)

        def find_end_token(_start, name):
            toks = tokens[_start:len(tokens)]
            for tok in toks:
                if tok.type == "END":
                    return tokens.index(tok)

            error(f"No END keyword was found for a {name}!", tokens[start].line)

        break_ = start
        if tokens[start].type == "FUNC":
            if tokens[start].value == "PRINT":
                break_ = find_line_break(start)
                nodes.append(PrintNode(get_value(start + 1, break_), tokens[start].line))

        elif tokens[start].type == "NAME":
            name = parse_name(start)

            if tokens[start + len(name)].type != "ASS":
                error("Unknown Error", tokens[start].line)

            break_ = find_line_break(start)
            nodes.append(VarAssignNode(name, get_value(start + len(name) + 1, break_), tokens[start].line))

        elif tokens[start].type == "LOOP":
            break_ = find_line_break(start)
            end_key = find_end_token(start, "loop")

            nodes.append(LoopNode(return_nodes(break_ + 1, end_key - 1), get_value(start + 1, break_),
                                  tokens[start].line))
            break_ = end_key

        elif tokens[start].type == "IF":
            break_ = find_line_break(start)
            end_key = find_end_token(start, "if statement")

            con = get_condition(start + 1, break_)
            if type(con).__name__ != "ComNode":
                error("An if statement must be followed by a condition!", tokens[start].line)

            nodes.append(IfNode(con, return_nodes(break_ + 1, end_key - 1), None, tokens[start].line))
            break_ = end_key

        elif tokens[start].type == "ELSE":
            break_ = find_line_break(start)
            end_key = find_end_token(start, "else statement")
            if_node = None

            for i in reversed(nodes):
                if type(i).__name__ == "IfNode":
                    if_node = i
                    index = nodes.index(i)
                    break

            if not if_node:
                error("No if statements were found above an else statement", tokens[start].line)

            if_node.else_nodes = return_nodes(break_ + 1, end_key - 1)
            nodes[index] = if_node
            break_ = end_key

        elif start == 0:
            error("An expression must contain a function call, an assignment, am if statement or a loop", 0)

        if break_ != end:
            create_nodes(break_ + 1, end)

    create_nodes(start_, end_)
    return nodes


start_nodes = return_nodes(0, len(tokens) - 1)

if debug:
    print(start_nodes)

#####################################
#          INTERPRETER
#####################################


variables = {}


def traverse_ast(node):
    type_ = type(node).__name__
    if type_ == "BasicOpNode":
        if type(node.left_node).__name__ == "StringNode" or type(node.right_node).__name__ == "StringNode":
            error("Strings can't  be added to integers or concatenated with other strings", node.line)
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
            if right_value == 0:
                error("Division by Zero", node.line)

            s = left_value / right_value
            if type(s) != int:
                s = floor(s)

            return s

    elif type_ == "NumberNode":
        number = node.value
        if node.sign == "MINUS":
            number *= -1

        return number

    elif type_ == "StringNode":
        return node.value

    elif type_ == "VarAssignNode":
        variables[node.name] = traverse_ast(node.value)
        return None

    elif type_ == "VarAccessNode":
        if variables.get(node.name) is None:
            error(f"The variable {node.name} could not be found", node.line)
        return variables[node.name]

    elif type_ == "PrintNode":
        print(traverse_ast(node.child_node))

    elif type_ == "LoopNode":
        it = traverse_ast(node.iterations)
        if it < 1:
            error("The iterations of a loop can't be 0 or lower", node.line)
        for _ in range(traverse_ast(node.iterations)):
            for node_ in node.child_nodes:
                traverse_ast(node_)

    elif type_ == "ComNode":
        op = node.equality_operator
        condition = False
        left = traverse_ast(node.left_node)
        right = traverse_ast(node.right_node)
        if type(left) != type(right):
            error("You can't compare different types", node.line)

        if op == "EQU":
            condition = left == right
        elif op == "UNEQU":
            condition = left != right

        if type(right) != int or type(left) != int:
            error("Only numbers can be compared with < or >", node.line)

        if op == "SMA":
            condition = left < right
        elif op == "BIG":
            condition = left > right

        return condition
    elif type_ == "IfNode":
        condition = traverse_ast(node.condition)
        if condition:
            for node_ in node.child_nodes:
                traverse_ast(node_)

        elif node.else_nodes:
            for node_ in node.else_nodes:
                traverse_ast(node_)


for node in start_nodes:
    traverse_ast(node)

subprocess.run(["pause"], shell=True)
