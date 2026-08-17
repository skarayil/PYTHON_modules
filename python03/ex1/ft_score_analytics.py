# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_score_analytics.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:20 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:21 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Player Score Analytics ===")

    scores = []

    args = sys.argv[1:]

    i = 0
    while i < len(args):
        try:
            score = int(args[i])
            scores.append(score)
        except ValueError:
            print(f"Invalid parameter: '{args[i]}'")
        i += 1

    if len(scores) == 0:
        print(
            "No scores provided. "
            "Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return

    total_players = len(scores)
    total_score = sum(scores)
    avg_score = total_score / total_players
    high_score = max(scores)
    low_score = min(scores)
    score_range = high_score - low_score

    print(f"Scores processed: {scores}")
    print(f"Total players: {total_players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {avg_score}")
    print(f"High score: {high_score}")
    print(f"Low score: {low_score}")
    print(f"Score range: {score_range}")


if globals().get("__name__") == "__main__":
    main()
