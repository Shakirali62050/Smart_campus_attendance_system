import os

USER_FILE = 'Database/users.txt'


def validate_user(uname, pwd):

    print("Checking Login For:", uname, pwd)

    try:
        with open(USER_FILE, 'r') as f:

            for line in f:

                print("RAW LINE:", line)

                parts = line.strip().split(',')

                print("PARTS:", parts)

                if len(parts) != 4:
                    print("INVALID FORMAT")
                    continue

                uid, username, password, role = parts

                username = username.strip()
                password = password.strip()
                role = role.strip()

                print("FILE DATA:", username, password, role)

                if username == uname and password == pwd:
                    print("LOGIN SUCCESS")
                    return True, role

    except Exception as e:
        print("ERROR:", e)

    print("LOGIN FAILED")
    return False, None