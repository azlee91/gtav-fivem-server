import secrets
import string


def generate_password(length: int = 20) -> str:
    alphabet = string.ascii_letters + string.digits
    while True:
        password = "".join(secrets.choice(alphabet) for i in range(length))
        if (
            any(c.islower() for c in password)
            and any(c.isupper() for c in password)
            and sum(c.isdigit() for c in password) >= 3
        ):
            return password


def main() -> None:
    """ Generates an env_file to be used with docker compose containers """
    mysql_root_password = generate_password()
    mysql_user = input(
        "Enter a user to create for the MySQL db (default: fiveM_default): "
    )
    mysql_user_password = input("Enter a password (Leave blank to generate): ")
    my_sql_db = input("Enter the DB name to create (*Required*): ")

    if not my_sql_db:
        print("You must specify a mysql DB to init")
        exit(1)

    if not mysql_user:
        mysql_user = "fiveM_default"

    if not mysql_user_password:
        mysql_user_password = generate_password()

    env_string = f"""MYSQL_ROOT_PASSWORD={mysql_root_password}
MYSQL_DATABASE={my_sql_db}
MYSQL_USER={mysql_user}
MYSQL_PASSWORD={mysql_user_password}
    """

    with open("env_file", "w") as out_file:
        out_file.write(env_string)


if __name__ == "__main__":
    main()
