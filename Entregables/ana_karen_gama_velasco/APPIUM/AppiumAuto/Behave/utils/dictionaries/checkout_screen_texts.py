import os
from dotenv import load_dotenv
load_dotenv()

fullname = os.getenv("FULL_NAME")
address = os.getenv("ADDRESS")
city = os.getenv("CITY")
zip_code = os.getenv("ZIP_CODE")
country = os.getenv("COUNTRY")
card = os.getenv("CARD")
exp_date = os.getenv("EXP_DATE")
sec_code = os.getenv("SEC_CODE")

FULL_NAME = {
    "FULL_NAME": fullname
}

ADDRESS = {
    "ADDRESS": address,
    "CITY": city,
    "ZIP_CODE": zip_code,
    "COUNTRY": country
}

CARD = {
    "CARD": card,
    "EXP_DATE": exp_date,
    "SEC_CODE": sec_code
}