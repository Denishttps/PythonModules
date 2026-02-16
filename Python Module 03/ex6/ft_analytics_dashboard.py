

def list_comprehension(users: list[dict]):
    print("=== List Comprehension Examples ===")
    usr_sort = sorted(users, key=lambda a: a["score"])
    print(
        "High scorers (>2000):",
        [i["name"] for i in usr_sort if i["score"] > 2000]
    )
    print("Scores doubled:", [i["score"]*2 for i in usr_sort])
    print(
        "Active players:",
        [i["name"] for i in users if i["active"]]
    )


def dict_comprehension(users: list[dict]):
    print("=== Dict Comprehension Examples ===")
    print(
        "Player scores:",
        {i["name"]: i["score"] for i in users}
    )
    grouped = {
        "high": [k["name"] for k in users if k["score"] > 2000],
        "medium": [k["name"] for k in users if 1500 <= k["score"] <= 2000],
        "low": [k["name"] for k in users if k["score"] < 1500]
    }
    print(
        "Score categories:",
        {k: len(v) for k, v in grouped.items()}
    )
    print(
        "Achievement counts:",
        {i["name"]: i["achiev_count"] for i in users}
    )


def set_comprehension(users: list[dict]):
    print("=== Set Comprehension Examples ===")
    print(
        "Unique players:",
        {user["name"] for user in users}
    )
    print(
        "Unique achievements:",
        {ach for u in users for ach in u["achievements"]}
    )
    print(
        "Active regions:",
        {u["region"] for u in users if u["region"]}
    )


def combiened_analysis(users: list[dict]):
    print("=== Combined Analysis ===")
    print("Total players:", len(users))
    print(
        "Total unique achievements:",
        len({ach for u in users for ach in u["achievements"]})
    )
    print(
        "Average score:",
        sum([i["score"] for i in users]) / len(users)
    )
    top_score = max([i["score"] for i in users])
    top_user = [
        (
            i["name"],
            i["score"],
            i["achiev_count"]
        ) for i in users if i["score"] == top_score
    ]
    print(
        f"Top performer: "
        f"{top_user[0][0]} ({top_user[0][1]} points, "
        f"{top_user[0][2]} achievements)"
    )


def main():
    print("=== Game Analytics Dashboard ===")
    print()
    users = [
        {
            "name": "alice",
            "score": 2300,
            "achiev_count": 5,
            "active": True,
            "achievements": ["first_kill", "level_10", "boss_slayer"],
            "region": "north"
        },
        {
            "name": "bob",
            "score": 1800,
            "achiev_count": 3,
            "active": True,
            "achievements": ["first_kill"],
            "region": "east"
        },
        {
            "name": "charlie",
            "score": 2150,
            "achiev_count": 7,
            "active": True,
            "achievements": ["level_10", "boss_slayer"],
            "region": "central"
        },
        {
            "name": "diana",
            "score": 2050,
            "achiev_count": 0,
            "active": False,
            "achievements": [],
            "region": None
        }
    ]
    list_comprehension(users)
    print()
    dict_comprehension(users)
    print()
    set_comprehension(users)
    print()
    combiened_analysis(users)


if __name__ == "__main__":
    main()
