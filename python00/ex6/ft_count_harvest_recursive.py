# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_count_harvest_recursive.py                      :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:05:05 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:05:06 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def helper(day):
        if day > days:
            print("Harvest time!")
            return
        print(f"Day {day}")
        helper(day + 1)
    helper(1)