import psutil
import time
import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80.0
MEMORY_THRESHOLD = 90.0

# Email config
sender = "youremail@gmail.com"
recipient = "youremail@gmail.com"
password = "your_app_password"

def send_email_alert(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {e}")

while True:
    cpu = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory().percent
    log = f"{datetime.now()} - CPU Usage: {cpu}%, Memory Usage: {mem}%\n"

    with open("logs/system_health.log", "a") as f:
        f.write(log)

    if cpu > CPU_THRESHOLD:
        print("⚠️ High CPU usage detected.")
        send_email_alert("High CPU Alert", f"CPU usage is at {cpu}%")

    if mem > MEMORY_THRESHOLD:
        print("⚠️ High Memory usage detected.")
        send_email_alert("High Memory Alert", f"Memory usage is at {mem}%")

    time.sleep(10)
