import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, app_password, recipient_email, subject, body):
    try:
        # Set up the server and login
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, app_password)

        # Create the email
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject

        # Attach the message body
        message.attach(MIMEText(body, 'plain'))

        # Send the email
        server.sendmail(sender_email, recipient_email, message.as_string())
        print(f"Email sent successfully to {recipient_email}!")

        # Close the connection
        server.quit()
    except Exception as e:
        print(f"Failed to send email: {e}")

# Usage
sender_email = "chanj1421@gmail.com"
app_password = "gevf oivt iqcu nrib"
recipient_email = "jychan@umass.edu"
subject = "Danger!"
body = "Your pot is boiling over! Turn down the stove!"

def email_alert(sender_email, app_password, recipient_email, subject, body):
  danger = photo_analysis()
  print(danger)
  for statement in danger:

    if statement == "YES":
        send_email(sender_email, app_password, recipient_email, subject, body)
    else:
      print("do nothing")

email_alert(sender_email, app_password, recipient_email, subject, body)
