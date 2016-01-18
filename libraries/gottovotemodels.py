from nebriosmodels import NebriOSModel, NebriOSField, NebriOSReference
from random import randint

def get_auth_code():
    return randint(1000, 9999)

class CountryRegistration(NebriOSModel):
    # id handled by database. May need to add anyways.
    region_code = NebriOSField(required=True)
    region_name = NebriOSField(required=True)
    district_code = NebriOSField(required=True)
    district_name = NebriOSField(required=True)
    electoral_area_name = NebriOSField(required=True)
    electoral_area_code = NebriOSField(required=True)
    reg_centre_code = NebriOSField(required=True)
    reg_centre_name = NebriOSField(required=True)
    other_polling_stations = NebriOSField(required=True)


class SmsRegistrationCheck(NebriOSModel):
    from_number = NebriOSField(required=True)
    message = NebriOSField()
    date_check = NebriOSField(required=True)
    sent = NebriOSField(required=True, default=False)


class SmsPeaceSender(NebriOSModel):
    from_number = NebriOSField(required=True)
    date_created = NebriOSField(required=True)
    auth_code = NebriOSField(required=True, default=get_auth_code)
    verified = NebriOSField(required=True, default=False)

    @property
    def message(self):
        message = "Hi. Thank you for keeping the peace & making history along " \
                  "with thousands of {country} like you. Send this SMS free " \
                  "at {url} From: [{number}]".format(
            country='Kenyans',
            url='example.com',
            number=str(self.from_number)
        )
        return message


class SmsPeaceReceiver(NebriOSModel):
    to_number = NebriOSField(required=True)
    sender = NebriOSReference(SmsPeaceSender, required=True)
    date_sent = NebriOSField()
    sent = NebriOSField(required=True, default=False)

