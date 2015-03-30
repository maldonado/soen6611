#!/usr/bin/python

import os
import psycopg2
import sys
import re

connection = None

try:
    
    #connect to the database to retrieve the file name linked with the commit
    connection = psycopg2.connect(host='cranberry', port='5432', database='everton_soen6611', user='everton', password='evermal01')
    cursor = connection.cursor()

    cursor.execute("drop table commit_trend")
    cursor.execute("create table commit_trend (commit text primary key, commit_release integer,  commit_message text, classification text)")

    cursor.execute("select commit, ")
        
except Exception, e:
    print  e
    connection.rollback()

finally:
    connection.commit()