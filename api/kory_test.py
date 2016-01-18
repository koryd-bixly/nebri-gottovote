import logging

logging.basicConfig(filename='korytest.log', level=logging.DEBUG)

def mydata(request):
    try:
        logging.debug(dir(request))
        logging.debug(request.BODY)
        logging.debug(request.POST)
    except Exception as e:
        logging.debug(str(e))

