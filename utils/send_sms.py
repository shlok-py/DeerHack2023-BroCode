from twilio.rest import Client

def main(animal):
# Twilio account information
    account_sid = 'AC64b7275b459e06b4ee69a42ec3c8e57f'
    auth_token = '4a5b04aaf9b29ea34c27ac3951542a44'
    client = Client(account_sid, auth_token)

    msg = f"Urgent!! There seems to be a {animal} in your area. Please take necessary precautions."

    # Message parameters
    from_number = '+13203503890' # Your Twilio phone number
    to_numbers = ['+9779819325102'] # List of phone numbers to send messages to

    # Send the messagesS
    for to_number in to_numbers:
        message = client.messages.create(
            body=msg,
            from_=from_number,
            to=to_number
        )
        print(f"Sent message to {to_number}, message ID: {message.sid}")
