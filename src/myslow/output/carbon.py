import socket
import time
from cStringIO import StringIO


class Histogram(object):

    def __init__(self):
        self.thresolds = [0, 1, 5, 10, 15, 30]
        self.reset()

    def reset(self):
        self.values = {0: 0, 1: 0, 5: 0, 10: 0, 15: 0, 30: 0}

    def _step(self, value):
        for a in self.thresolds:
            if value <= a:
                return a
        return self.thresolds[-1]

    def count(self, value):
        self.values[self._step(value)] += 1


class Carbon(object):
    def __init__(self, target, prefix="myslow", sample=60):
        self.prefix = prefix
        self.sample = sample
        z = target.split(':')
        if len(z) == 1:
            self.host = target
            self.port = 2003
        else:
            self.host, self.port = z
        self.histo = Histogram()

    def __call__(self, log):
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.connect((self.host, self.port))
        first = None
        qt_max = 0
        re_max = 0
        for t, h, c in log:
            ts = int(time.mktime(t.timetuple()))
            qt_max = max(qt_max, h['Query_time'])
            re_max = max(re_max, h['Rows_examined'])
            self.histo.count(h['Query_time'])
            if first is None:
                first = ts
            elif ts - first > self.sample:
                first += self.sample
                buff = StringIO()
                buff.write(self.prefix)
                buff.write('.query_time.max %i %i\n' % (qt_max, first))
                buff.write(self.prefix)
                buff.write('.row_examined.max %i %i\n' % (re_max, first))
                print buff.getvalue(),
                #print ts, qt_max, re_max, self.histo.values
                qt_max = 0
                re_max = 0
                self.histo.reset()
