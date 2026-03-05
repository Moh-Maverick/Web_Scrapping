import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_csv_email(csv_file, sender_email, sender_password, recipient_email):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = "Stack Overflow Python Questions CSV"
    
    # Add body text
    body = "Hi,\n\nPlease find attached the Stack Overflow Python questions CSV file.\n\nBest regards"
    message.attach(MIMEText(body, 'plain'))
    
    # Attach CSV file
    try:
        with open(csv_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
        
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {csv_file}')
        message.attach(part)
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        print("Email sent successfully!")
        return True
        
    except FileNotFoundError:
        print(f"Error: {csv_file} not found")
        return False
    except Exception as e:
        print(f"Error sending email: {e}")
        return False


if __name__ == "__main__":
    pass
