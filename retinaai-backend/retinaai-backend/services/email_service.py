from utils.email_utils import send_otp_email

def send_verification_email(email, otp):
    send_otp_email(email, otp)