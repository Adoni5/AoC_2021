import re
from math import prod
from operator import gt, eq, lt

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
    version = int(packet[:3], 2)
    type_id = int(packet[3:6], 2)
    return version, type_id, packet[6:]

ans = {}

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


instructions = {0: sum,
                1: prod,
                2: min,
                3: max,
                5: gt,
                6: lt,
                7: lambda x, y: x == y}


test1 = "A0016C880162017C3686B18A3D4780"
# with open("input") as fh:
#     test1 = fh.read().strip()
sans = "".join(t[char] for char in test1)
packet = "".join(t[char] for char in test1)


def parse_packet(packet, county=None, type_1=False):
    lits = []
    version_sum = 0
    booly = packet.count("1") if not county else county
    opy = []
    while booly:
        version, type_id, packet = packet_version_tid(packet)
        print(f"type id is {type_id}")
        version_sum += version
        if type_id == 4:
            lit_value, packet, removed = parse_literal_packet(packet)
            lits.append(lit_value)
        else:
            opy.append(instructions[type_id])
            if not int(packet[0]):
                print("op type 0")
                sub_packets_length = int(packet[1:16], 2)
                packet = packet[16:]
            else:
                print("op type 1")
                sub_packet_count = int(packet[1: 12], 2)
                # print(sub_packet_count)
                packet, vs, ls, opr = parse_packet(packet[12:], sub_packet_count)

                version_sum += vs
                lits.extend([ls])
                opy.extend(opr)
        if county and type_1:
            booly -= 1
        elif county and not type_1:
            booly = county
        else:
            booly = packet.count("1")
    return packet, version_sum, lits, opy


packet, version_sum, lits, opr = parse_packet(packet)
# a = [fun(vals) for vals, fun in list(zip(lits, opr[1:]))]
# if len(opr !)


