import logging

logging.basicConfig(filename="debug/bank_acc.log", format='%(asctime)s %(message)s', filemode='w')
subway_logger = logging.getLogger()
subway_logger.setLevel(logging.DEBUG)

logging.basicConfig(filename="debug/ticket.log", format='%(asctime)s %(message)s', filemode='w')
ticket_logger = logging.getLogger()
ticket_logger.setLevel(logging.DEBUG)
