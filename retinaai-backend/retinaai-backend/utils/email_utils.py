import smtplib
from email.mime.text import MIMEText

EMAIL_ADDRESS = "retinaai08@gmail.com"
EMAIL_PASSWORD = "nlsvhygisxtvdryo"


def send_otp_email(to_email, otp, user_role="Patient", purpose="verify"):

    print("Sending OTP to:", to_email)
    print("OTP:", otp)

    # =============================
    # SUBJECT
    # =============================

    if purpose == "verify":
        subject = "RetinaAI Account Verification Code"
    else:
        subject = "RetinaAI Password Reset Code"

    # =============================
    # EMAIL BODY
    # =============================

    if purpose == "verify":

        if user_role.lower() == "doctor":

            body = f"""
Dear Doctor,

Welcome to RetinaAI — AI-powered retinal diagnostic platform.

To complete your doctor account verification, please use the verification code below.

Verification Code:
{otp}

This code will expire in 5 minutes.

For security reasons:
• Do not share this code with anyone.
• RetinaAI staff will never ask for your OTP.

Once verified, you will gain access to the RetinaAI Doctor Dashboard for patient retinal analysis and AI diagnostics.

If you did not request this verification, please ignore this email.

Regards,
RetinaAI Security Team
"""

        else:

            body = f"""
Dear Patient,

Welcome to RetinaAI — AI-powered retinal health monitoring.

To activate your patient account, please use the verification code below.

Verification Code:
{otp}

This code will expire in 5 minutes.

Security Notice:
• Never share this code with anyone.
• RetinaAI will never ask for your OTP.

Once verified, you will be able to upload retinal scans and track your eye health using AI analysis.

If this request was not made by you, please ignore this email.

Regards,
RetinaAI Security Team
"""

    else:

        body = f"""
RetinaAI Password Recovery Request

We received a request to reset your RetinaAI account password.

Your password reset code is:

{otp}

This code will expire in 5 minutes.

Security Notice:
• Do NOT share this code with anyone.
• RetinaAI support will never ask for your reset code.
• If you did not request a password reset, please ignore this email.

Stay secure,
RetinaAI Security Team
"""

    # =============================
    # EMAIL MESSAGE
    # =============================

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email

    try:

        print("Connecting to Gmail SMTP...")

        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=10)

        server.starttls()

        print("Logging in...")

        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        print("Sending email...")

        server.sendmail(
            EMAIL_ADDRESS,
            to_email,
            msg.as_string()
        )

        server.quit()

        print("✅ Email sent successfully")

    except Exception as e:

        print("❌ EMAIL ERROR:", str(e))

