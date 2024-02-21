import re


regex = r"\b[A-Za-z0-9._+%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
regex2 = r"[^@]+@[^@]+\.[^@]+"


def check_email(email):
    if re.fullmatch(regex2, email):
        print(f"{email} is a valid email!!")
    else:
        print(f"{email} is not valid.")


email1 = "anktierail326@gmail.com"
email2 = "myown.site@our-earth.org"
email3 = "hahah.com"

check_email(email1)
check_email(email2)
check_email(email3)

