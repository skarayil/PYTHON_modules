# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_age.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:04:47 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:04:48 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age <= 60:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")  