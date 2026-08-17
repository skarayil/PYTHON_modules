# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_alchemist.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:48 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:49 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice", "bob", "Charlie",
        "dylan", "Emma", "Gregory",
        "john", "kevin", "Liam"
    ]

    print(f"Initial list of players: {players}")

    capitalized_all = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {capitalized_all}")

    only_capitalized = [name for name in players if name[0].isupper()]
    print(f"New list of capitalized names only: {only_capitalized}")

    score_dict = {name: random.randint(0, 1000) for name in capitalized_all}
    print(f"Score dict: {score_dict}")

    score_avg = sum(score_dict.values()) / len(score_dict)
    print(f"Score average is {round(score_avg, 2)}")

    high_scores = {
        name: score
        for name, score in score_dict.items()
        if score > score_avg
    }
    print(f"High scores: {high_scores}")


if locals().get("__name__") == "__main__":
    main()
