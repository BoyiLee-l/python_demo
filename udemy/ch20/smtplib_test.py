import smtplib
import getpass

smtp_obj = smtplib.SMTP("smtp.gmail.com", 587)
smtp_obj.ehlo()
smtp_obj.starttls()

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
print(smtp_obj.login(email, password))

# vnqpamteaqwahutu
