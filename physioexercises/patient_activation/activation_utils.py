import pandas as pd
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def get_addresses(f):
    try:
        f.seek(0)
        df = pd.read_csv(f)
    except Exception as e:
        return f"An error occurred: {str(e)}"
    filtered_df = df[~df["Location"].str.contains("Hydrotherapy", case=False)]
    name_email_dict = dict(zip(filtered_df["Client"], filtered_df["Email"]))
    return {name.split()[0]: email for name, email in name_email_dict.items()}


def send_patient_activation(addresses, sender):
    email_count = 0
    booking_link = "https://physioward.com.au/book-now/"
    image_url = "https://physioward.com.au/wp-content/uploads/2022/09/physioward-secondary-logo-stacked-left-full-color-rgb.svg"
    subject = "Physio Update"
    body = """
        Hi {name},
        I noticed it's been a while since you've been in the clinic.\n
        How are you getting on? Are you making progress towards your goals?\n
        Best regards,\n
        {sender} - Physiotherapist\n
        Phone: (02) 9905 0048\n
        Book Here: {booking_link}\n
        """
    for name, address in addresses.items():
        to = [f"{address}"]
        from_email = settings.DEFAULT_FROM_EMAIL

        # Creating EmailMessage object
        email = EmailMultiAlternatives(subject=subject, body=body, from_email=from_email, to=to)

        # Adding HTML content
        html_content = f"""
            <html>
                <body>
                    <p>Hi {name},</p>
                    <p>I noticed it's been a while since you've been in the clinic.</p>
                    <p>How are you getting on? Are you making progress towards your goals?</p>
                    <p>Best regards,</p>
                    <strong>{sender} - Physiotherapist</strong><br>
                    <p>Phone: (02) 9905 0048</p>
                    <p><a href={booking_link}>Book Online</a></p>
                    <img src={image_url} alt="Physio Ward Logo" width="100" height="50"><br>
                </body>
            </html>
            """
        email.attach_alternative(html_content, "text/html")
        try:
            email.send()
            email_count += 1
        except Exception as e:
            print(f"Error sending email: {e}")
    return email_count
