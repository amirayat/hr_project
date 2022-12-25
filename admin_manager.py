import argparse
from db.db_admin import create_admin, modify_admin
from schemas import Admin


parser = argparse.ArgumentParser(description="Admin creation using commandline")

parser.add_argument('--action', help='create or update admin', choices=["create", "update"], required=True)
parser.add_argument('--username', help='import username', required=True)
parser.add_argument('--password', help='import password', required=True)

args = parser.parse_args()

if args.action == "create":
    admin = Admin(username=args.username, password=args.password)
    res = create_admin(admin)
    print("Created:", res)
if args.action == "update":
    admin = Admin(username=args.username, password=args.password)
    res = modify_admin(admin)
    print("Updated:", res)
