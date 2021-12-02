from typing import Tuple


class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal = 0
        self.aim = 0

    def forward(self, amnt):
        self.horizontal += amnt
        self.depth += self.aim * amnt

    def down(self, amnt):
        self.aim += amnt

    def up(self, amnt):
        self.aim -= amnt

    def __getitem__(self, item):
        return getattr(self, item)

    def total_pt_1(self):
        return self.aim * self.horizontal

    def total_pt_2(self):
        return self.horizontal * self.depth

    def move(self, commands: str, part_1: bool) -> int:
        genny = ((instruction.split()) for instruction in commands.splitlines())
        for instruction, amnt in genny:
            self[instruction](int(amnt))
        answer = self.total_pt_1() if part_1 else self.total_pt_2()
        return answer


test_input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""


if __name__ == "__main__":
    submarine = Submarine()
    assert submarine.move(test_input, True) == 150, "test part 1"
    submarine = Submarine()
    assert submarine.move(test_input, False) == 900, "test part 2"
    submarine = Submarine()
    with open("input", "r") as fh:
        print(submarine.move(fh.read(), True))
        print(submarine.move(fh.read(), False))
    # part02
