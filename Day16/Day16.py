import re
from functools import reduce
from math import prod
from operator import gt, eq, lt, mul

translation = """0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111"""
pat = re.compile(r"(.) = (\d{4})")
t = {k: v for k, v in pat.findall(translation)}


def packet_version_tid(packet):
    version = packet.read_int(3)
    type_id = packet.read_int(3)
    return version, type_id


class Buffer:
    def __init__(self, bits):
        self.arr = bits
        self.ptr = 0
        self.it = iter(self.arr)

    def read_int(self, n):
        return int(self.read_str(n), 2)

    def read_str(self, n):
        self.ptr += n
        return "".join(next(self.it) for _ in range(n))


def parse_literal_packet(packet):
    """

    :param packet: str packet string, could be sub_packets
    :return: int
    """
    bit_group_literal = ""
    for i in range(0, len(packet), 5):
        bit_group = packet[i : i + 5]
        bit_group_literal += bit_group[1:]
        if bit_group[0] == "0":
            break
    return int(bit_group_literal, 2), packet[i+5:], i+5


def parse_packet(packet):
    version, t_id = packet_version_tid(packet)

    if t_id == 4:
        value = ""
        while packet.read_int(1) != 0:
            value += packet.read_str(4)
        value += packet.read_str(4)
        return version, t_id, int(value, 2)

    length_type = packet.read_int(1)
    if length_type == 0:
        target = packet.read_int(15) + packet.ptr  # order matters!
        subs = []
        while packet.ptr < target:
            subs.append(parse_packet(packet))
        return version, t_id, subs
    elif length_type == 1:
        subpackets = packet.read_int(11)
        subs = []
        for _ in range(subpackets):
            subs.append(parse_packet(packet))
        return version, t_id, subs


def version_sum(packet):
    version, op, subpackets = packet
    if op == 4:
        return version
    else:
        return version + sum([version_sum(p) for p in subpackets])


operators = [
    sum,
    lambda s: reduce(mul, s),
    min,
    max,
    lambda s: s,
    lambda s: int(gt(*s)),
    lambda s: int(lt(*s)),
    lambda s: int(eq(*s)),
]


def eval_packet(packet):
    version, op, subpackets = packet
    if isinstance(subpackets, list):
        subpackets = list(map(eval_packet, subpackets))
    return operators[op](subpackets)

with open("input") as fh:
    bits = fh.read().strip()

bits = "".join(t[char] for char in bits)
packets = parse_packet(Buffer(bits))
print("Part 1:", version_sum(packets))
print("Part 2:", eval_packet(packets))





