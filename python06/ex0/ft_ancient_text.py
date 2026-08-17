# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_ancient_text.py                                 :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:15:08 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:15:09 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys
import typing

def project(filename: str) -> None:
    f: typing.IO[str]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        data: str = f.read()
        print("---")
        print(data, end="")
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
    else:
        project(sys.argv[1])


if __name__ == "__main__":
    main()
