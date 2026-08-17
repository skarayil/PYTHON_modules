# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_raise_exception.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:12:41 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:12:42 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def input_temperature(temp_str: str) -> int:
    _degree = int(temp_str)

    if not 0 <= _degree <= 40:
        if _degree > 40:
            raise Exception(f"{_degree}°C is too hot for plants (max 40°C)")
        else:
            raise Exception(f"{_degree}°C is too cold for plants (min 0°C)")

    return _degree


def test_temperature() -> None:
    print("=== Garden Temperature Checker ===")
    print("")
    _sensor_inputs = ["25", "abc", "100", "-50"]

    for val in _sensor_inputs:
        print(f"Input data is '{val}'")
        try:
            _degree = input_temperature(val)
            print(f"Temperature is now {_degree}°C")
            print("")
        except Exception as e:
            print(f"Caught input_temperature error: {e}")
            print("")

    print("All tests completed - program didn't crash!")


if globals().get("__name__", "") == "__main__":
    test_temperature()
