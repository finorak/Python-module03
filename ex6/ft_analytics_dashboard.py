data = {
    "players": {
        "alice": {
            "level": 41,
            "total_score": 2824,
            "sessions_played": 13,
            "favorite_mode": "ranked",
            "achievements_count": 5,
        },
        "bob": {
            "level": 16,
            "total_score": 4657,
            "sessions_played": 27,
            "favorite_mode": "ranked",
            "achievements_count": 2,
        },
        "charlie": {
            "level": 44,
            "total_score": 9935,
            "sessions_played": 21,
            "favorite_mode": "ranked",
            "achievements_count": 7,
        },
        "diana": {
            "level": 3,
            "total_score": 1488,
            "sessions_played": 21,
            "favorite_mode": "casual",
            "achievements_count": 4,
        },
        "eve": {
            "level": 33,
            "total_score": 1434,
            "sessions_played": 81,
            "favorite_mode": "casual",
            "achievements_count": 7,
        },
        "frank": {
            "level": 15,
            "total_score": 8359,
            "sessions_played": 85,
            "favorite_mode": "competitive",
            "achievements_count": 1,
        },
    },
    "sessions": [
        {
            "player": "bob",
            "duration_minutes": 94,
            "score": 1831,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 32,
            "score": 1478,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 17,
            "score": 1570,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 98,
            "score": 1981,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 15,
            "score": 2361,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 29,
            "score": 2985,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 34,
            "score": 1285,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "alice",
            "duration_minutes": 53,
            "score": 1238,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 1555,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 92,
            "score": 2754,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 98,
            "score": 1102,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 39,
            "score": 2721,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 46,
            "score": 329,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 56,
            "score": 1196,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 117,
            "score": 1388,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "diana",
            "duration_minutes": 118,
            "score": 2733,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 22,
            "score": 1110,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "frank",
            "duration_minutes": 79,
            "score": 1854,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "charlie",
            "duration_minutes": 33,
            "score": 666,
            "mode": "ranked",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 101,
            "score": 292,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 25,
            "score": 2887,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "diana",
            "duration_minutes": 53,
            "score": 2540,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "eve",
            "duration_minutes": 115,
            "score": 147,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "frank",
            "duration_minutes": 118,
            "score": 2299,
            "mode": "competitive",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 42,
            "score": 1880,
            "mode": "casual",
            "completed": False,
        },
        {
            "player": "alice",
            "duration_minutes": 97,
            "score": 1178,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 18,
            "score": 2661,
            "mode": "competitive",
            "completed": True,
        },
        {
            "player": "bob",
            "duration_minutes": 52,
            "score": 761,
            "mode": "ranked",
            "completed": True,
        },
        {
            "player": "eve",
            "duration_minutes": 46,
            "score": 2101,
            "mode": "casual",
            "completed": True,
        },
        {
            "player": "charlie",
            "duration_minutes": 117,
            "score": 1359,
            "mode": "casual",
            "completed": True,
        },
    ],
    "game_modes": ["casual", "competitive", "ranked"],
    "achievements": [
        "first_blood",
        "level_master",
        "speed_runner",
        "treasure_seeker",
        "boss_hunter",
        "pixel_perfect",
        "combo_king",
        "explorer",
    ],
}


def list_comprehension(data: dict) -> None:
    print("\n=== List Comprehension Exemples ===")

    def get_heigh_score(players: dict) -> list:
        heigh = []
        for player in players:
            if players[player]["total_score"] > 2000:
                heigh += [player]
        return heigh

    def get_active_players(sessions: dict) -> list:
        active = []
        for session in sessions:
            if not session["completed"] and session['player'] not in active:
                active += [session["player"]]
        return active

    def get_double_socore(data: dict) -> list:
        double = []
        players = data['players']
        for player in players:
            double += [players[player]['total_score'] * 2]
        return double

    players = data["players"]
    high_score = get_heigh_score(players)
    print(f"Heigh scroes (>2000): {high_score}")
    score_double = get_double_socore(data)
    print(f"Doubled Score: {score_double}")
    active_player = get_active_players(data["sessions"])
    print(f"Active players: {active_player}")


def dict_comprehension(data: dict) -> None:
    print("\n=== Dict Comprehension Exemples ===")

    def get_player_score(data: dict) -> dict | None:
        player_score = dict()
        players = data['players']
        for player in players:
            player_score.update({player: players[player]['total_score']})
        return player_score if player_score else None

    def get_score_categories(data: dict) -> dict | None:
        categories = dict()
        return categories if categories else None

    def get_achievements_count(data: dict) -> dict | None:
        achievements_count = dict()
        players = data['players']
        for player in players:
            achievements_count.update({
                player: players[player]['achievements_count']
                })
        return achievements_count if achievements_count else None

    player_score = get_player_score(data)
    print(f"Player scores: {player_score}")
    score_categories = get_score_categories(data)
    print(f"Score categories: {score_categories}")
    achievements_count = get_achievements_count(data)
    print(f"Achievemnts Count: {achievements_count}")


def set_comprehension(data: dict) -> list:
    print("\n=== Set Comprehension ===")
    new_data = []

    def get_unique_players(data: dict) -> set | None:
        unique = set(data['players'])
        return unique if unique else None

    def get_unique_achievements(data: dict) -> set | None:
        achievements = data['achievements']
        return set(achievements) if achievements else None

    def get_active_modes(data: dict) -> set | None:
        sessions = data['sessions']
        active_modes = []
        for session in sessions:
            if session['completed']:
                active_modes += [session['mode']]
        return set(active_modes) if active_modes else None

    unique_players = get_unique_players(data)
    print(f"Unique players: {unique_players}")
    unique_achievements = get_unique_achievements(data)
    print(f"Unique achievements: {unique_achievements}")
    active_modes = get_active_modes(data)
    print(f"Active modes: {active_modes}")
    new_data += [len(unique_players) if unique_players else 0]
    new_data += [len(unique_achievements) if unique_achievements else 0]
    return new_data


def combined_analysis(data: dict, new_data: list) -> None:
    print("\n=== Combined Analysis ===")
    print(f"Total players: {new_data[0]}")
    print(f"Total uniaue achievements: {new_data[1]}")

    def get_average_score(players: dict) -> float:
        scores = []
        for player in players:
            scores += [players[player]['total_score']]
        return sum(scores) / len(players)

    def get_top_performer(data: dict) -> list | None:
        top_performer = None
        players = data['players']
        max_score = 0
        for player in players:
            if max_score <= players[player]['total_score']:
                top_performer = player
                players[player]['total_score']
        return top_performer

    print("Average score: {:.1f}".format(get_average_score(data["players"])))
    player = get_top_performer(data)
    if player is None:
        return
    print(f"Top perfomer: {player}", end=" ")
    print(f"({data['players'][player]['total_score']}", end="")
    print("points", end=", ")
    print(f"{data['players'][player]['achievements_count']} achievements)")


def main(data: dict) -> None:
    list_comprehension(data)
    dict_comprehension(data)
    new_data = set_comprehension(data)
    combined_analysis(data, new_data)


if __name__ == "__main__":
    print("=== Game Analytics Dashboard ===")
    main(data)
