#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3
fields = 'HTTP_HOST', 'REQUEST_METHOD', 'REQUEST_URI', 'REMOTE_ADDR', 'HTTP_USER_AGENT', 'post'
conn = sqlite3.connect('test.db')
c = conn.cursor()
r = 'CREATE TABLE req (dt datetime, ' + ' text, '.join(fields) + ' text)'
c.execute(r)
conn.commit()
conn.close()
