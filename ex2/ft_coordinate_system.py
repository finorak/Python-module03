import sys
import math


def parse_input(argv: list[str]) -> list[int] | bool:
    argv_cpy = []
    parsing = False
    if len(argv) == 1:
        print(f"Parsing coordinates: \"{argv[0]}\"")
        argv = argv[0].split(",")
        parsing = True
    for arg in argv:
        try:
            argv_cpy += [int(arg)]
        except ValueError as e:
            print("Error parsing coordinates: invlaid literal:", e)
            print(f"Error details - Type: {e.__class__.__name__}", end=" ")
            print(f"Args: (\"{e}\"")
            return False
    if parsing:
        print(f"Parsed position: {tuple(argv_cpy)}")
    else:
        print(f"Created position: {tuple(argv_cpy)}")
    return argv_cpy


def coorinate_calculation(pos1: tuple, pos2: tuple) -> float:
    x = (pos2[0] - pos1[0]) ** 2
    y = (pos2[1] - pos1[1]) ** 2
    z = (pos2[2] - pos1[2]) ** 2
    distance = math.sqrt(x + y + z)
    return distance


def main(argc: int, argv: list[str]) -> None:
    if argc == 1 and argc != 2 and argc != 4:
        return
    argv_cpy = parse_input(argv[1:])
    if not argv_cpy:
        return
    original = (0, 0, 0)
    pos = tuple(argv_cpy)
    distance = coorinate_calculation(original, pos)
    print(f"Distance between {original} and {pos}", end=": ")
    print("{:.2f}\n".format(distance))
    print("\nUnpacking demonstration:")
    print(f"Player at x={pos[0]}, y={pos[1]}, z={pos[2]}")
    print(f"Coordinate: X={pos[0]}, Y={pos[1]}, Z={pos[2]}")


def test() -> None:
    argv = ["program", "5", "6", "7"]
    main(len(argv), argv)
    argv = ["program", "abc,efg,hig"]
    main(len(argv), argv)


if __name__ == "__main__":
    print("=== Game Coordinate System ===\n")
    if len(sys.argv) == 1:
        test()
    else:
        main(len(sys.argv), sys.argv)
