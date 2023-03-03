import os
from dotenv import load_dotenv
load_dotenv()

username = os.getenv("STANDARD_USER")
password = os.getenv("PASSWORD")

USERS = {
    "USERNAME": username,
    "PASSWORD": password
}