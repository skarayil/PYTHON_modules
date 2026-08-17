# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_water_reminder.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:04:56 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:04:57 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def  ft_water_reminder():
    water_reminder = int(input("Days since last watering: "))
    if  water_reminder <= 2:
        print("Plants are fine")
    else:
        print("Water the plants!")