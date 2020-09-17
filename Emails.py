
import smtplib
from email.message import EmailMessage


Email_Address = "Enter Your email Address"
Email_Password = "Enter Your Password here"

msg = EmailMessage()
msg['Subject'] = "Enter the Subject of Email"
msg['From'] = Email_Address
msg['To'] = "Enter the receivers email address"
msg.set_content('Enter Your Message Here')

# You Can use below code to attach a image to your mail
#with open('img.jpg', 'rb') as f: 
#     file_data = f.read()
#     file_name = f.name
# msg.add_attachment(file_data, maintype='application', subtype = 'octect-stream', filename=  file_name )


with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(Email_Address, Email_Password)

    smtp.send_message(msg)







