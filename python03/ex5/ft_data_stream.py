# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_data_stream.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:13:43 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:13:44 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

import random
import typing


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    players = ["alice", "bob", "charlie", "dylan"]
    actions = [
        "run", "eat", "sleep",
        "grab", "move", "climb",
        "swim", "use", "release"
    ]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(lst: list) -> typing.Generator[tuple[str, str], None, None]:
    while len(lst) > 0:
        idx = random.randint(0, len(lst) - 1)
        item = lst[idx]
        del lst[idx]
        yield item


def main() -> None:
    print("=== Game Data Stream Processor ===")

    stream = gen_event()

    for i in range(1000):
        event = next(stream)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    print("[...]")

    event_list = []
    for _ in range(10):
        event_list += [next(stream)]

    print(f"Built list of 10 events: {event_list}")

    for event in consume_event(event_list):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
