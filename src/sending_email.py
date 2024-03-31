import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import matplotlib.pyplot as plt


def send_email(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    # Attach the report
    with open(attachment_path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_path}",
    )

    msg.attach(part)

    # Connect to the SMTP server and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.sendmail(sender_email, receiver_email, msg.as_string())

def main():

    # Email settings
    sender_email = "sender@example.com"
    receiver_email = "recipient@example.com"
    subject = "Daily Report"
    body = "Please find the attached daily report."
    attachment_path = "C:/Users/thoma/Desktop/Alpha/2024/Task/src/experiments/yearly_count_trends.png"

    # Temporary email service SMTP details
    smtp_server = "temporary_email_smtp_server"
    smtp_port = 25  # or the appropriate port provided by the service

    # Send the email with the report
    send_email(sender_email, receiver_email, subject, body, attachment_path, smtp_server, smtp_port)

if __name__ == "__main__":
    main()
