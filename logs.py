import datetime


def write_log(log_message):
    f = open('logger.txt', 'a')
    f.write(str(datetime.datetime.now()) + " " + log_message + "\n")
    f.close()
