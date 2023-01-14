import imaplib
import twilio
from twilio.rest import Client
import time

# IMAP server information
imap_server = "imap.gmail.com"
imap_user = "XXX@gmail.com"
imap_pass = "XXX"

# Twilio client information
account_sid = 'XXX'
auth_token = 'XXX'
client = Client(account_sid, auth_token)

# phone number to call
to_phone_number = "XXX"

# email address to check for
target_email = "XXX"

while True:
    try:
        # connect to the IMAP server
        imap = imaplib.IMAP4_SSL(imap_server, 993)
        imap.login(imap_user, imap_pass)

        # select the inbox
        imap.select("inbox")
        print('IMAP selected Inbox')

        # search for unread emails from the target email address
        status, emails = imap.search(None, "UNSEEN", f"FROM {target_email}")
        emails = emails[0].split()

        # if there are any unread emails from the target email address
        if emails:
            # make a phone call
            call = client.calls.create(
                to=to_phone_number,
                from_="XXX",
                url="http://demo.twilio.com/docs/voice.xml"
            )
            print(f"Calling {to_phone_number}")
            break
        else:
            print("No new emails from the target address.")

        # close the connection to the server
        imap.close()
        imap.logout()
    except Exception as e:
        print("Error connecting to the server. Retrying in 1 seconds.")
        print("Error: " + str(e))
    time.sleep(1)
