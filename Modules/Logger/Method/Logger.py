from Modules.Interface import EventElements


def init_logger():
    import logging.handlers
    import os
    import datetime

    os.makedirs('Logs', exist_ok=True)
    datetime_str = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    EventElements.logger = logging.getLogger('ping_test_logger')
    EventElements.logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handler = logging.handlers.RotatingFileHandler(
        os.path.join('Logs', 'ping_test_log_' + datetime_str + '.log'),
        maxBytes=1048576,
        backupCount=5
    )
    handler.setFormatter(formatter)
    EventElements.logger.addHandler(handler)
    EventElements.logger.info('Start Ping Pong app')
