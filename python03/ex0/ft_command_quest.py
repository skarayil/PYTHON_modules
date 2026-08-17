# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_command_quest.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:12 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:13 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    args_count = len(sys.argv)
    if args_count == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {args_count - 1}")
        i = 1
        while i < args_count:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1

    print(f"Total arguments: {args_count}")


if locals().get("__name__") == "__main__":
    main()
