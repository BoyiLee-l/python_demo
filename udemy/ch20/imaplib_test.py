import imaplib
import email as em

M = imaplib.IMAP4_SSL("imap.gmail.com")

email = "p396520@gmail.com"
password = "zxjthudpmyhqirwy"

M.login(email, password)
M.select("inbox")
result, ids = M.search(None, "FROM noreply@gdg.community.dev")
# print(ids)
myString = ids[0].decode("utf-8") # 先將ids[0]做decode，從bytes變成string
myEmailList = myString.split(" ") # 將string內部的數字分開

rese, content = M.fetch(myEmailList[0], "(RFC822)")

raw_content = content[0][1]
email_content = raw_content.decode("utf-8")
email_message = em.message_from_string(email_content)

for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)