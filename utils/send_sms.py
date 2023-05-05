from twilio.rest import Client

def main(message_body):
# Twilio account information
    account_sid = 'AC64b7275b459e06b4ee69a42ec3c8e57f'
    auth_token = '49fd61e486df043b61538800e8e06834'
    client = Client(account_sid, auth_token)

    # Message parameters
    from_number = '+13203503890' # Your Twilio phone number
    to_numbers = ['+9779819325102'] # List of phone numbers to send messages to
    message_body = message_body # The body of the message to send

    # Send the messagesS
    for to_number in to_numbers:
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        print(f"Sent message to {to_number}, message ID: {message.sid}")
