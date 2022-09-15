import datetime


def tsm():
    return datetime.datetime.now(datetime.timezone.utc).strftime('%H:%M:%S.%f')[:-3]

class Log:
    LOGLEVEL = 3

    @staticmethod
    def line(msg, level):
        return tsm() + '\t{' + level + '}\t' + msg

    @staticmethod
    def debug(what):
        if Log.LOGLEVEL >= 3:
            print(Log.line(what, 'DEBUG'))

    @staticmethod
    def info(what):
        if Log.LOGLEVEL >= 2:
            print(Log.line(what, 'INFO'))

    @staticmethod
    def warn(what):
        if Log.LOGLEVEL >= 1:
            print(Log.line(what, 'WARN'))

    @staticmethod
    def error(what):
        if Log.LOGLEVEL >= 0:
            print(Log.line(what, 'ERROR'), file=sys.stderr)