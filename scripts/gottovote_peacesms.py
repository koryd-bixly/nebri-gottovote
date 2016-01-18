class peacesms(NebriOS):
    # listens_to = ['korytest']
    listens_to = ['auth_check']
    is_run = False
    # test

    def check(self):
        return self.is_run is False

    def action(self):
        self.is_run = True
#        self.korytest = "Ran"
        send_email("koryd@bixly.com","""Test message""")
        self.is_run = False
