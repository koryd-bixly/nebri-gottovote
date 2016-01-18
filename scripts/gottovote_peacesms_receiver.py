from twilioutils import send_message

class PeaceSms(NebriOS):
    listens_to = ['verified']

    def check(self):
        check_number = not self.to_number == ''
        check_verified = self.sender.verified
        check_kind = self.kind == 'smspeacereceiver'
        check_sent = self.sent is False
        return check_kind and check_number and check_verified and check_sent

    def action(self):
        try:
            # do stuff with the message
            message_id = send_message(
                shared.twilio_sid,
                shared.twilio_token,
                self.pid
            )
            self.twilio_id = message_id
            self.date_sent = datetime.now()
            self.sent = True
        except:
            # something happened and we got an error... do nothing with this message.
            pass