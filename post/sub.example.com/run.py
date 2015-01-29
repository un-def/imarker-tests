#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
from datetime import datetime
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    fields = ('HTTP_HOST', 'REQUEST_METHOD', 'REQUEST_URI', 'REMOTE_ADDR', 'HTTP_USER_AGENT')
    data = [environ.get(f, '') for f in fields]
    try:
        body_size = int(environ.get('CONTENT_LENGTH', 0))
    except ValueError:
        body_size = 0
    body = environ['wsgi.input'].read(body_size)
    data.insert(0, datetime.now())
    data.append(body)
    conn = sqlite3.connect('test.db')
    c = conn.cursor()
    r = 'INSERT INTO req VALUES(' + ('?,'*len(data))[:-1]  + ')'
    c.execute(r, data)
    conn.commit()
    conn.close()
    start_response('200 OK', [('Content-type', 'text/html; charset=utf-8')])
    return ['''<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body>
<p>I regret nothing.</p>
<img src="/dude.jpg">
</body>
</html>''']

WSGIServer(app).run()
