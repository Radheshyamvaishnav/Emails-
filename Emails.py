
import smtplib


sender_email = "Enter Sender's Email Here"
rec_email = "Enter Recevier's Email Here"
password = "Enter Sender's Password Here"  # It's always a best practice to use App Password over here which is generated after enabling 2 step verification in your google account.
msg = ""   # Enter the Message you want to Send  
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login(sender_email, password)
server.sendmail(sender_email, rec_email, msg)


print("EmailSent")


