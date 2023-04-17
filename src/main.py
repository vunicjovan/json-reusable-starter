from pprint import pprint

from src.utils.data_utils import DataUtils
from src.utils.json_utils import JsonUtils

USERS_JSON_PATH = "data/users.json"

users_to_be_created = [user.__dict__ for user in DataUtils.generate_users(10)]
JsonUtils.create(users_to_be_created, USERS_JSON_PATH)

users = JsonUtils.load(USERS_JSON_PATH)
pprint(users)

new_user = DataUtils.generate_users(1)
pprint(new_user)
