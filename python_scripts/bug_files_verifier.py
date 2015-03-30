#!/usr/bin/python

import os
import psycopg2
import sys


try:
    
    #connect to the database to retrieve the file name linked with the commit
    connection = psycopg2.connect(host='cranberry', port='5432', database='everton_soen6611', user='everton', password='evermal01')
    cursor = connection.cursor()
    cursor.execute("select path from bug_info order by path")
    rows = cursor.fetchall()
    
    directory = "/Users/evermal/Documents/soen6411/course_project/data/chrome_data_bugs/"
    found_files = 0
    not_found_files = 0 
    for row in rows:
        name = row[0].replace("chrome_data_bugs/", "")
        if os.path.isfile(directory+name):
            # print "encontrou " + name
            found_files = found_files + 1 
        else:
            not_found_files = not_found_files + 1
    
    print "found: "+ str(found_files)
    print "not found: "+ str(not_found_files)
    print "total: "  + str(found_files + not_found_files)    


except Exception, e:
    print  e
