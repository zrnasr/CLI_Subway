import logging

def setup_logger(log_file): 
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)

    return logger

user_logger = setup_logger("debug/user.log")
bank_logger = setup_logger("debug/bank_acc.log")
ticket_logger = setup_logger("debug/ticket.log")





