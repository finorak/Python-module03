import sys


def ft_join(data: list, char: str) -> None:
    count = len(data)
    for i in range(count):
        if i < count - 1:
            print(data[i], end=char)
        else:
            print(data[i])


def parse_input(argv: list[str]) -> dict | None:
    data = dict()
    for arg in argv:
        arg = arg.split(":")
        if len(arg) != 2:
            return None
        try:
            item_count = int(arg[1])
            data.update({arg[0]: item_count})
        except ValueError as e:
            print(f"Non numeric value for {arg[0]}")
            print("Error:", e)
            return None
    return data


def invontory_info(data: dict) -> list:
    items_count = 0
    item_count = len(data)
    for item in data:
        items_count += data[item]
    print(f"Total items in invontory: {items_count}")
    print(f"Total items types: {item_count}")
    return [items_count, item_count]


def get_current_invontory(data: dict, items_count: int) -> None:
    print("\n=== Current Invontory ===")
    for item in data:
        item_count = data.get(item)
        if item_count is None:
            continue
        rate = (item_count * 100) // items_count
        print(f"{item}: {item_count} units ({rate}%)")


def print_most_abundant(data: dict) -> None:
    count = len(data)
    counter = 0
    for item in data:
        if counter < count - 1:
            print(f"{item} ({data.get(item)})", end=", ")
        else:
            print(f"{item} ({data.get(item)})")
        counter += 1


def print_least_abundant(data: dict) -> None:
    count = len(data)
    counter = 0
    for item in data:
        if counter < count - 1:
            print(f"{item} ({data.get(item)})", end=", ")
        else:
            print(f"{item} ({data.get(item)})")
        counter += 1


def invontory_statistic(data: dict) -> None:
    print("\n=== Invontory Statistic ===")
    moderate = dict()
    scarce = dict()
    for item in data:
        item_count = data.get(item)
        if item_count is None:
            continue
        if item_count >= 5:
            moderate.update({item: item_count})
        elif item_count <= 1:
            scarce.update({item: item_count})
    print("Most abundant: ", end="")
    print_most_abundant(moderate)
    print("Least abundant: ", end="")
    print_least_abundant(scarce)


def management_suggestion(data: dict) -> set | None:
    print("\n=== Management Suggestion ===")
    suggestions = []
    for item in data:
        item_count = data.get(item)
        if item_count is None:
            continue
        if item_count <= 1:
            suggestions += [item]
    print("Restock: ", end="")
    ft_join(suggestions, ", ")
    return set(suggestions) if suggestions else None


def dictionary_propreties(data: dict, chr_value: str) -> None:
    keys = []
    values = []
    for key, value in data.items():
        keys += [key]
        values += [value]
    print("Dictionary keys: ", end="")
    ft_join(keys, ", ")
    print("Dictionary values: ", end="")
    ft_join(values, ", ")
    print(f"Sample lookup - '{chr_value}' in invontory: {chr_value in data}")


def main(argc: int, argv: list[str]) -> None:
    if argc == 1:
        return
    data = parse_input(argv[1:])
    if data is None:
        return
    count_info = invontory_info(data)
    get_current_invontory(data, count_info[0])
    invontory_statistic(data)
    management_suggestion(data)
    dictionary_propreties(data, "sword")


if __name__ == "__main__":
    print("=== Invontory System Analysys ===")
    main(len(sys.argv), sys.argv)
