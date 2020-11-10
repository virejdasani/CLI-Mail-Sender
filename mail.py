# For email
import smtplib
# For getting password anonymously
import getpass

session = smtplib.SMTP('smtp.live.com', 587)

session.starttls()

# Get the required details
mailID = input("Enter your email address\n") 
password = getpass.getpass("Enter Password\n")
reciepient = input("Enter email of reciepient\n")
msg = input("Enter message\n")
# This is required for it to work
message = f"\n {msg}"

# Login
session.login(mailID, password)

# SEND
session.sendmail(mailID, reciepient, message)



session.quit()