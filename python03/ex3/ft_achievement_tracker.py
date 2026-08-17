# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_achievement_tracker.py                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:32 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:33 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import random


def gen_player_achievements() -> set:
    achievements = [
        "First Blood", "Sharpshooter", "Explorer", "Collector",
        "Pacifist", "Speedrunner", "Boss Slayer", "Secret Finder",
        "Master Crafter", "Completionist"
    ]
    count = random.randint(3, 7)
    return set(random.sample(achievements, count))


def main() -> None:
    print("=== Achievement Tracker ===")

    p1 = gen_player_achievements()
    p2 = gen_player_achievements()
    p3 = gen_player_achievements()
    p4 = gen_player_achievements()

    players = [p1, p2, p3, p4]

    print(f"Player 1 achievements: {p1}")
    print(f"Player 2 achievements: {p2}")
    print(f"Player 3 achievements: {p3}")
    print(f"Player 4 achievements: {p4}")

    all_achievements = p1.union(p2).union(p3).union(p4)
    print(f"\nTotal unique achievements unlocked: {all_achievements}")

    shared = p1.intersection(p2).intersection(p3).intersection(p4)
    print(f"Achievements shared by all players: {shared}")

    i = 0
    while i < len(players):
        others: set[str] = set()
        j = 0
        while j < len(players):
            if i != j:
                others = others.union(players[j])
            j += 1
        exclusive = players[i].difference(others)
        print(f"Player {i+1} exclusive achievements: {exclusive}")
        i += 1

    i = 0
    while i < len(players):
        missing = all_achievements.difference(players[i])
        print(f"Player {i+1} is missing: {missing}")
        i += 1


if locals().get("__name__") == "__main__":
    main()
