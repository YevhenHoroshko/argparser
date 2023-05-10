from system_helpers import get_data_from_file, write_to_file

USERS_FILE_PATH = "database/users.json"


def save_user(first_name, last_name, email):
    data = get_data_from_file(USERS_FILE_PATH)
    new_obj = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    if len(data) >= 1:
        new_obj["id"] = len(data) + 1
    else:
        new_obj["id"] = 1
    data.append(new_obj)
    write_to_file(USERS_FILE_PATH, data)


def get_all_users():
    data = get_data_from_file(USERS_FILE_PATH)
    for obj in data:
        print(obj["id"])
        print(obj["first_name"])
        print(obj["last_name"])
        print(obj["email"])
        print("================================")


def get_user_by_id(user_id):
    data = get_data_from_file(USERS_FILE_PATH)
    for obj in data:
        if obj["id"] == user_id:
            print(obj["id"])
            print(obj["first_name"])
            print(obj["last_name"])
            print(obj["email"])


def update_user(user_id=None, first_name=None, last_name=None, email=None):
    data = get_data_from_file(USERS_FILE_PATH)
    for obj in data:
        if obj["id"] == user_id:
            obj["first_name"] = first_name or obj["first_name"]
            obj["last_name"] = last_name or obj["last_name"]
            obj["email"] = email or obj["email"]
            write_to_file(USERS_FILE_PATH, data)
            break
    else:
        save_user(first_name, last_name, email)


def delete_user(user_id):
    data = get_data_from_file(USERS_FILE_PATH)
    for i in range(len(data)):
        if data[i]["id"] == user_id:
            del data[i]
            break
    write_to_file(USERS_FILE_PATH, data)
