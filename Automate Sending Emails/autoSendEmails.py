import os
import smtplib
from email.message import EmailMessage
email_id = 'kumarraunak077@gmail.com'
pswd = os.environ.get('password')
email = EmailMessage()
email['Subject'] = 'Images converted to PDF by Raunak Mishra'
email['From'] = email_id
email['To'] = 'raunakraunak077@gmail.com'
email.set_content('Check the file attached with this mail !!')
with open('filename.extension','rb') as f:
    file_data = f.read()
    file_type = 'extension-type'
    file_name = f.name
    email.add_attachment(file_data, maintype = 'depending on file type', subtype = 'depending on file type', filename = file_name)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(email_id ,pswd)
    smtp.send_message(email)
    print("Email Sent!!")
