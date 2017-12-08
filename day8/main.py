from collections import namedtuple, defaultdict
import re

INSTRUCTION_FIELDS = namedtuple('instruction', ['update_arg0', 'update', 'update_arg1',
                                                'pred_arg0', 'pred', 'pred_arg1'])


class Instruction(INSTRUCTION_FIELDS):

    UPDATE_OP = {
        'inc': lambda x, y: x + y,
        'dec': lambda x, y: x - y,
    }

    BINARY_PREDICATE = {
        '>': lambda x, y: x > y,
        '<': lambda x, y: x < y,
        '>=': lambda x, y: x >= y,
        '<=': lambda x, y: x <= y,
        '==': lambda x, y: x == y,
        '!=': lambda x, y: x != y,
    }

    def __init__(self, *args, **kwargs):
        super(Instruction, self).__init__(args, kwargs)
        self.binary_predicate = self.BINARY_PREDICATE[self.pred]
        self.update_func = self.UPDATE_OP[self.update]
        self.test_value = int(self.pred_arg1)
        self.update_value = int(self.update_arg1)

    def process(self, registers):
        reg_value = registers[self.pred_arg0]
        test = self.binary_predicate(reg_value, self.test_value)
        if test:
            registers[self.update_arg0] = self.update_func(
                registers[self.update_arg0], self.update_value)


def read_input():
    with open('input.txt') as f:
        return f.read()


def parse_instruction(line):
    tokens = [token
              for token in line.split()
              if token != 'if']
    assert len(tokens) == 6
    instruction = Instruction(*tokens)
    return instruction


def main():
    _input = read_input()
    instructions = [parse_instruction(line)
                    for line in _input.split('\n')
                    if line]

    registers = defaultdict(lambda: 0)

    global_max = 0
    for i in instructions:
        i.process(registers)
        global_max = max(global_max, max(registers.values()))
    # pt1
    print max(registers.values())
    # pt2
    print global_max

if __name__ == '__main__':
    main()
