# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_vault_security.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: skarayil <skarayil@student.42kocaeli>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/08/17 22:14:23 by skarayil          #+#    #+#              #
#    Updated: 2026/08/17 22:14:24 by skarayil         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!/usr/bin/env python3

def secure_archive(
    filename: str,
    action: str = "read",
    content: str = ""
) -> tuple[bool, str]:
    if action == "read":
        try:
            with open(filename, "r") as f:
                data: str = f.read()
            return (True, data)
        except Exception as e:
            return (False, str(e))
    else:
        try:
            with open(filename, "w") as f:
                f.write(content)
            return (True, "Content successfully written to file")
        except Exception as e:
            return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"))

    print("Using 'secure_archive' to read from a regular file:")
    result: tuple[bool, str] = secure_archive("ancient_fragment.txt")
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    content: str = result[1] if result[0] else ""
    print(secure_archive("vault_copy.txt", "write", content))


if __name__ == "__main__":
    main()
