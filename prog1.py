class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


def parse_input_string(input_string):
    # Parsing table
    parsing_table = {
        'E': {'a': 'TQ', '(': 'TQ'},
        'Q': {'+': '+TQ', '-': '-TQ', ')': 'ɛ', '$': 'ɛ'},
        'T': {'a': 'FR', '(': 'FR'},
        'R': {'+': 'ɛ', '-': 'ɛ', '*': '*FR', '/': '/FR', ')': 'ɛ', '$': 'ɛ'},
        'F': {'(': '(E)', 'a': 'a'}
    }

    # Stack and input string initialization
    stack = Stack()
    stack.push('$')
    stack.push('E')
    input_string += '$'
    input_index = 0

    # Parsing loop
    while not stack.is_empty():
        current_symbol = stack.pop()
        if current_symbol == input_string[input_index]:
            input_index += 1
        elif current_symbol in parsing_table and input_string[input_index] in parsing_table[current_symbol]:
            production = parsing_table[current_symbol][input_string[input_index]]
            if production != 'ɛ':
                for symbol in reversed(production):
                    stack.push(symbol)
        else:
            print("String is not accepted/invalid")
            return

        # Display stack content after each match
        print("Stack:", stack)

    print("String is accepted/valid")


# Test cases
input_strings = [
    "(a+a)*a$",
    "a*(a/a)$",
    "a(a+a)$"
]

for input_str in input_strings:
    print("Input:", input_str)
    parse_input_string(input_str)
    print()
