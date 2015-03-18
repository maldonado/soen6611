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
    # cursor.execute("select a.path from bug_info a, bugfix_commits2 b where a.bug_id = b.bug_id and b.bug_id = '62936' ;")
    cursor.execute("select path, bug_id from bug_info order by path")
    rows = cursor.fetchall()
    
    directory = "/Users/evermal/Documents/soen6611/course_project/data/chrome_data_bugs/"
    pattern = 'span class="date"\stitle=(.{26})'   

    not_found_files = 0 
    for row in rows:
        bug_id = row[1]
        name = row[0].replace("chrome_data_bugs/", "")
        if os.path.isfile(directory+name):
            with open(directory+name, 'r') as f:
                lines = f.readlines();
            for line in lines:
                match = re.search(pattern, line)
                if match:
                    new_line = match.group(1) + '\n'
                    formated_date = new_line.replace("\"", "\'")
                    cursor.execute("update bugfix_commits2 set bug_reported_date = to_timestamp("+formated_date+", 'Dy Mon DD HH24:MI:SS YYYY') where bug_id = '"+bug_id+"';")     
                    break  
        else:
            not_found_files = not_found_files + 1

    print not_found_files
        
except Exception, e:
    print  e
    connection.rollback()

finally:
    connection.commit()