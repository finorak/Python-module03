data = {
    "alice": [
        "first_blood",
        "pixel_perfect",
        "speed_runner",
        "first_blood",
        "first_blood",
    ],
    "bob": [
        "level_master",
        "boss_hunter",
        "treasure_seeker",
        "level_master",
        "level_master",
    ],
    "charlie": [
        "treasure_seeker",
        "boss_hunter",
        "combo_king",
        "first_blood",
        "boss_hunter",
        "first_blood",
        "boss_hunter",
        "first_blood",
    ],
    "diana": [
        "first_blood",
        "combo_king",
        "level_master",
        "treasure_seeker",
        "speed_runner",
        "combo_king",
        "combo_king",
        "level_master",
    ],
    "eve": [
        "level_master",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
        "first_blood",
        "treasure_seeker",
    ],
    "frank": [
        "explorer",
        "boss_hunter",
        "first_blood",
        "explorer",
        "first_blood",
        "boss_hunter",
    ],
}


def show_achievements(data: dict[str, list[str]]) -> dict[str, set]:
    new_data = dict()
    for player in data:
        achievement = set(data[player])
        new_data.update({f"{player}": achievement})
        print(f"Player {player} achievements:", achievement)
    return new_data


def get_unique_achievements(new_data: dict[str, set]) -> set[str]:
    data = []
    for player in new_data:
        for achievement in new_data[player]:
            data += [achievement]
    return set(data)


def get_common_achievements(data: dict) -> set | str:
    common = None
    for player in data:
        if common is None:
            common = data[player]
        else:
            common = common.intersection(data[player])
    return common if common else "None"


def is_duplicate(achievements: list[str], curr_achievement: str) -> bool:
    counter = 0
    for achievement in achievements:
        if curr_achievement == achievement:
            counter += 1
        if counter > 1:
            return True
    return False


def in_other_player(data: dict, curr_player: str, achievement: str) -> bool:
    for player in data:
        if player == curr_player:
            continue
        if achievement in data[player]:
            return True
    return False


def get_rare_achievements(data: dict[str, list[str]]) -> set | None:
    rare = []
    for player in data:
        for achievement in data[player]:
            if is_duplicate(data[player], achievement):
                break
            if in_other_player(data, player, achievement):
                break
            rare += [achievement]
    return set(rare) if rare else None


def get_common_to_player(data: dict, name1: str, name2: str) -> set | None:
    common = []
    for achievement in data[name1]:
        if achievement in data[name2]:
            common += [achievement]
    return set(common) if common else None


def get_unique_to_player(achievements: list[str]) -> set | None:
    unique = []
    for achievement in achievements:
        if not is_duplicate(achievements, achievement):
            unique += [achievement]
    return set(unique) if unique else None


def player_analyse(data:  dict, name1: str, name2: str) -> None:
    common = get_common_to_player(data, name1, name2)
    print(f"{name1} vs {name2} common: {common}")
    name1_unique = get_unique_to_player(data[name1])
    print(f"{name1} unique: {name1_unique}")
    name2_unique = get_unique_to_player(data[name2])
    print(f"{name2} unique: {name2_unique}")


def achievement_analytics(old_data: dict,
                          new_data: dict[str, set[str]]) -> None:
    print("\n=== Achievement Analytics ===")
    unique_achievement = get_unique_achievements(new_data)
    print("All unique achievements:", unique_achievement)
    unique_achievement_count = len(unique_achievement)
    print("Total unique achievements:", unique_achievement_count)
    common_achievements = get_common_achievements(new_data)
    print("\nCommon to all players:", common_achievements)
    rare_achievement = get_rare_achievements(old_data)
    print("Rare achievements (1 player): ", rare_achievement)


def main(data: dict[str, list[str]]) -> None:
    print("=== Achievements Tracker System ===\n")
    new_data = show_achievements(data)
    achievement_analytics(data, new_data)
    player_analyse(data, "alice", "bob")


if __name__ == "__main__":
    main(data)
