def output(log):
    yield "Time;Query_time;Rows_examined;Rows_sent;Lock_time;host;user"
    for time_, headers, command in log:
        yield "%s;%i;%i;%i;%i;%s;%s" % (time_.strftime('%s'),
                                        headers['Query_time'],
                                        headers['Rows_examined'],
                                        headers['Rows_sent'],
                                        headers['Lock_time'],
                                        headers['host'], headers['user'])
