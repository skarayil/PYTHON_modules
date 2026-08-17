# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_coordinate_system.py                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:26 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:27 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        try:
            line = input("Enter new coordinates as floats in format 'x,y,z': ")
        except EOFError:
            raise SystemExit

        parts = line.split(',')
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        valid = True
        coords = []
        for p in parts:
            p_strip = p.strip()
            try:
                coords.append(float(p_strip))
            except ValueError as e:
                print(f"Error on parameter '{p_strip}': {e}")
                valid = False
                break

        if valid and len(coords) == 3:
            return (coords[0], coords[1], coords[2])


def main() -> None:
    print("=== Game Coordinate System ===")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    dist_center = math.sqrt(pos1[0]**2 + pos1[1]**2 + pos1[2]**2)
    print(f"Distance to center: {round(dist_center, 4)}")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()

    dist_2 = math.sqrt(
        (pos2[0] - pos1[0])**2 +
        (pos2[1] - pos1[1])**2 +
        (pos2[2] - pos1[2])**2
    )
    print(f"Distance between the 2 sets of coordinates: {round(dist_2, 4)}")


if __name__ == "__main__":
    main()
