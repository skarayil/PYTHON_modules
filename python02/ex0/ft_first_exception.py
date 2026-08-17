# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:33 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:34 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===")
    print("")
    print("Input data is '25'")
    try:
        t_s = input_temperature("25")
        print(f"Temperature is now {t_s} °C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nInput data is 'abc'")
    try:
        t_s = input_temperature("abc")
        print(f"Temperature is now {t_s} °C")
    except Exception as e:
        print(f"Caught input_temperature error: {e}")

    print("\nAll tests completed - program didn't crash!")


if globals().get("__name__", "") == "__main__":
    test_temperature()
