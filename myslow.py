#!/usr/bin/env python


class MySlow(object):
    def __init__(self, source):
        self.source = source
        self.header = None
        self.state = 'header'
        self.time = None
        self.commands = []

    def __iter__(self):
        for line in self.source:
            if line[0] != '#':  # sql or first informations
                if self.header is None:
                    continue
                self.commands.append(line[:-1])
            else:  # header
                if len(self.commands):
                    yield self.time, self.header, "\n".join(self.commands)
                    self.commands = []
                if self.header is None:
                    self.header = {}
                if line.startswith("# Time: "):
                    self.time = line[8:-2]
                    continue
                if line.startswith("# User@Host: "):
                    u, h = line[13:-1].split(' @ ')
                    self.header['user'] = u
                    self.header['host'] = h
                    continue
                if line.startswith("# Query_time: "):
                    # Query_time: 0  Lock_time: 0  Rows_sent: 0  Rows_examined: 164124
                    for value in line[2:-1].split("  "):
                        k, v = value.split(': ')
                        self.header[k] = int(v)
                    continue
                print "Unknow format :", line


if __name__ == '__main__':
    with open('mysql-slow.log') as log:
        for time_, headers, command in MySlow(log):
            if headers['Query_time'] > 0:
                print headers, command
