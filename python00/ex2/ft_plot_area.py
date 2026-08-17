# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plot_area.py                                    :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:04:38 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:04:39 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def ft_plot_area():
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    plot_area = length * width
    print("Plot area:", plot_area)