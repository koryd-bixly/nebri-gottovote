class test_sms(NebriOS):
    # listens_to = ['korytest']
    listens_to = ['auth_check']

    def check(self):
        return True

    def action(self):
        send_email("koryd@bixly.com","""Test message test_sms""")