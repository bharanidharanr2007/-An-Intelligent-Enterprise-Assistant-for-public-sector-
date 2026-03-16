import random
import smtplib

def generate_otp():
    return str(random.randint(100000,999999))

def send_otp(email, otp):

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()

    sender_email = "your_email@gmail.com"
    password = "your_password"

    server.login(sender_email,password)

    message = f"Your OTP for login is {otp}"

    server.sendmail(sender_email,email,message)

    server.quit()
