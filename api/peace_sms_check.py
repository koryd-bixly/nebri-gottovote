import logging
from libraries.gottovotemodels import SmsPeaceSender, SmsPeaceReceiver
import json

logging.basicConfig(filename='peace_sms_check.auth.log', level=logging.DEBUG)

def auth(request):
    # logging.debug(dir(request))
    data = json.loads(request.BODY)

    if request.PROCESS:
        request.PROCESS['auth_check'] = data['auth_code']
        request.PROCESS.save()
    else:
        p = Process.objects.create()
        p.auth_check = data['auth_code']
        p.save()

    # request.PROCESS['auth_check'] = data['auth_code']

    logging.debug('Finished API auth')

    return 'finished'
