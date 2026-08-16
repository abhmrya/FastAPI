from tables import create_tables
from services import *

# Create Tables
create_tables()

# Create Data 
# create_user("abhay",'abhay@example.com')
# create_user("kush",'kush@example.com')

# create_post(1,"Hello World", "This is abhay first post")

# Read data
# print(get_user_by_id(1))
print(get_all_user())