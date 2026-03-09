import sys


def parse_input(argv: list[str]) -> list[int] | None:
    argv_cpy = []
    for arg in argv:
        try:
            arg = int(arg)
            argv_cpy += [arg]
        except ValueError:
            print("oops, I typed 'banana' instead of '1000'")
            return None
    return argv_cpy


def main(argc: int, argv: list[str], file_name: str) -> None:
    print("=== Player Score Analytics ===")
    if argc == 1:
        print(f"No scores provided. Usage: python3 {file_name}", end=" ")
        print("<score1> <score2> ...")
        return
    argv_cpy = parse_input(argv[1:])
    if argv_cpy is None:
        return
    print(f"Scores processed: {argv_cpy}")
    total_score = sum(argv_cpy)
    player_count = len(argv_cpy)
    min_score = min(argv_cpy)
    max_score = max(argv_cpy)
    average_score = total_score / player_count
    print(f"Total players: {player_count}")
    print(f"Total score: {total_score}")
    print(f"Average score: {average_score}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {max_score - min_score}")


if __name__ == "__main__":
    file_name = "ft_score_analytics.py"
    main(len(sys.argv), sys.argv, file_name)
