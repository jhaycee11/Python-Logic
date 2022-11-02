import smtplib
import sys
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "myname"
email["to"] = "email@gmail.com"
email["subject"] = "100 Days of saying I Love You"

email.set_content(f"{sys.argv[1]}day of I Love You")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sendmail@gmail.com", "pass")
    smtp.send_message(email)
    print("Message Sent <3")



"""
import smtplib
from pathlib import Path
from email.message import EmailMessage
from string import Template

html = Template(Path("index.html").read_text())
email = EmailMessage()
email["from"] = "name"
email["to"] = "mail@gmail.com"
email["subject"] = "I love you"

email.set_content(html.substitute(name="Hoa"), "html")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("sendmail@gmail.com", "pass")
    smtp.send_message(email)
"""