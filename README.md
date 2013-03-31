Myslow
======

Read Mysql slow query log.

Use it
------

You can use virtualenv

    python setup.py build
    python setup.py install

Try it
------

    slowlog --input /var/log/mysql/mysql-slow.log --thresold 2

Todo
----

 * √ Parsing log as a flow
 * _ Graphite export
 * _ Usage with logtail
 * _ CSV export
 * _ Explore CSV with R
 * _ Elastic Search export

Licence
=======

3 terms BSD Licence © 2013 Mathieu Lecarme.
