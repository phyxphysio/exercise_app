import pandas as pd
from django.core.mail import EmailMultiAlternatives

MESSAGE_BODIES = {
    "physiotherapy": """
        I hope this email finds you well. I noticed that it's been a while since your last visit to the clinic, and thought I would check in to see how you are doing. 

It's important to stay on top of your health, and we are here to help with anything from lingering pain to goal setting and planning for the future. 

Take advantage of all the benefits physiotherapy can offer, and give us a call or book online today. 

I look forward to welcoming you back to PhysioWard Brookvale (formerly AusHealth Physiotherapy).
    """,
    "hydrotherapy": """
        I hope you’re doing well! I’ve noticed that you haven’t attended our hydrotherapy classes for a while, and I wanted to invite you back to experience the benefits of our pool sessions.

Hydrotherapy is a fantastic way to improve mobility, reduce pain, and enhance overall wellness. We're keen to help you achieve your health goals in a fun and supportive environment.

Don’t miss this chance to jump back into a fitness routine that will make you feel great.

Give us a call to sign up for your next class today!
    """,
}

def get_addresses(f, service):
    try:
        f.seek(0)
        df = pd.read_csv(f)
    except Exception as e:
        return f"An error occurred: {str(e)}"
    if service == "Physiotherapy":
        filtered_df = df[~df["Location"].str.contains("Hydrotherapy", case=False)]
    else:
        filtered_df = df[df["Location"].str.contains("Hydrotherapy", case=False)]
    name_email_dict = dict(zip(filtered_df["Client"], filtered_df["Email"]))
    return {name.split()[0]: email for name, email in name_email_dict.items()}


def send_patient_activation(addresses, sender, service):
    sender = ' '.join([name.title() for name in sender.split('_')])
    email_count = 0
    booking_link = "https://physioward.com.au/book-now/"
    image_url = "https://physioward.com.au/wp-content/uploads/2022/09/physioward-secondary-logo-stacked-left-full-color-rgb.svg"
    subject = f"{service.title()} at Physioward Brookvale"
    for name, address in addresses.items():
        to = [f"{address}"]
        from_email = f"{sender.split()[0]} at PhysioWard"
        body = f"""Dear {name},
        {MESSAGE_BODIES[service]},
        Best regards,\n
        {sender} - Physiotherapist\n
        Phone: (02) 9905 0048\n
        Book Here: {booking_link}\n """

        # Creating EmailMessage object
        email = EmailMultiAlternatives(
            subject=subject, body=body, from_email=from_email, to=to, reply_to=['brookvale@physioward.com.au'],
        )

        # Adding HTML content
        lines = MESSAGE_BODIES[service].strip().split('\n')
        wrapped_lines = [f'<p>{line.strip()}</p>' for line in lines if line.strip()]
        html_body = '\n'.join(wrapped_lines)
        html_content = f"""
            <html>
                <body>
                    <p>Hi {name},</p>
                    {html_body}
                    <p>Best regards,</p>
                    <strong>{sender} - Physiotherapist</strong><br>
                    <p>Phone: (02) 9905 0048</p>
                    <p><a href={booking_link}>Book Online</a></p>
                <img src={image_url} alt="Physioward Logo" style="display: block; width: 100%; max-width: 600px; height: auto;">
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
