from argparse import ArgumentParser
from user_functions import save_user, get_all_users, get_user_by_id, update_user, delete_user


parser = ArgumentParser()

parser.add_argument("-o", "--operation", required=True)
parser.add_argument("-f", "--first_name")
parser.add_argument("-l", "--last_name")
parser.add_argument("-e", "--email")
parser.add_argument("-id", "--identifier")

args = parser.parse_args()

if int(args.operation) == 1:
    # add user to the database
    save_user(args.first_name, args.last_name, args.email)
elif int(args.operation) == 2:
    # print all users data from database
    get_all_users()
elif int(args.operation) == 3:
    # print specific user data from database
    get_user_by_id(int(args.identifier))
elif int(args.operation) == 4:
    # update specific user data in database
    update_user(int(args.identifier), args.first_name, args.last_name, args.email)
elif int(args.operation) == 5:
    # remove specific user from database
    delete_user(int(args.identifier))
