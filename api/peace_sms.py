import logging
from libraries.gottovotemodels import SmsPeaceSender, SmsPeaceReceiver
import json

logging.basicConfig(filename='send_peace.log', level=logging.DEBUG)

def send_peace(request):
    data = json.loads(request.BODY)
    logging.debug(data)
    try:
        from_number = data['from_number']
    except Exception as e:
        raise e
        # return 404

    # collect all the to numbers. I can't get a list in the post message...
    to = data['to']

    # make sure at least one of them has something in them...
    if not any(to):
        raise Exception('any(to) failed')
        # return 404

    try:
        sender = SmsPeaceSender(
            from_number=from_number,
            date_created=datetime.now(),
        )
        sender.save()
    except Exception as e:
        logging.debug(e)
        raise e

    # create receivers
    for s in to:
        if s:
            try:
                receiver = SmsPeaceReceiver(
                    to_number=s,
                    sender=sender
                )
                receiver.save()
            except Exception as e:
                logging.debug(e)
                raise e

    send_email("koryd@bixly.com", 'auth code is: ' + str(sender.auth_code))

    logging.debug('auth code is: ' + str(sender.auth_code))
    logging.debug('Finished with this API')

    return json.dumps(dict(
        auth_code=str(sender.auth_code),
        id=str(sender.pid)
    ))
