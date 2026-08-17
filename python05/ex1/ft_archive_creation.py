# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_archive_creation.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:14:41 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:14:42 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import sys
import typing


def project(filename: str) -> typing.Optional[str]:
    f: typing.IO[str]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")

    try:
        f = open(filename, "r")
        data: str = f.read()
        print("---")
        print(data, end="")
        print("---")
        f.close()
        print(f"File '{filename}' closed.")
        return data
    except Exception as e:
        print(f"Error opening file '{filename}': {e}")
        return None


def transform(data: str) -> str:
    lines: list[str] = data.splitlines()
    transformed: list[str] = [line + "#" for line in lines]
    return "\n".join(transformed) + "\n"


def save_data(new_data: str) -> None:
    new_filename: str = input("Enter new file name (or empty): ")

    if not new_filename:
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")
    try:
        f: typing.IO[str] = open(new_filename, "w")
        f.write(new_data)
        f.close()
        print(f"Data saved in file '{new_filename}'.")
    except Exception as e:
        print(f"Error opening file '{new_filename}': {e}")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return

    data: typing.Optional[str] = project(sys.argv[1])

    if data is None:
        return

    new_data: str = transform(data)
    print("Transform data:")
    print("---")
    print(new_data, end="")
    print("---")

    save_data(new_data)


if __name__ == "__main__":
    main()
