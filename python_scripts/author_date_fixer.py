import os
import psycopg2
import sys
import re

connection = None

try:
    
    #connect to the database 
    connection = psycopg2.connect(host='cranberry', port='5432', database='everton_soen6611', user='everton', password='evermal01')
    cursor = connection.cursor()
    
    #create table
    print "create table"
    cursor.execute("drop table bugfix_commits")
    cursor.execute("create table bugfix_commits (commit text, bug_id text, bug_report_date timestamp, bug_report_release integer, commit_date timestamp,  commit_release integer)")
    
    #define commit, bug_id, author_date and path to seach the txt file 
    cursor.execute("select a.commit, a.bug_id, b.author_dt, c.path from bugfix_commits2 a, git_commit_backup b, bug_info c  where b.commit = a.commit and a.bug_id = c.bug_id order by a.bug_id")
    rows = cursor.fetchall()

    counter = 0
    total_rows = len(rows)
    # directory where the txt files are allocated
    directory = "/Users/evermal/Documents/soen6611/course_project/data/chrome_data_bugs/"

    # regex to match the reported date
    pattern = 'span class="date"\stitle=(.{26})'   

    for row in rows:
        bug_report_date = None
        commit = row[0]
        bug_id = row[1]
        commit_date = row[2]
        file_name = row[3].replace("chrome_data_bugs/", "")
        # commit_release = "null"
        # bug_report_release = "null"
        # reading the txt file searching for the regex match
        if os.path.isfile(directory+file_name):
            with open(directory+file_name, 'r') as f:
                lines = f.readlines();
            for line in lines:
                match = re.search(pattern, line)
                if match:
                    new_line = match.group(1) + '\n'
                    bug_report_date = new_line.replace("\"", "\'")
                    # insert line with it was able to find the formated date 
                    cursor.execute("insert into bugfix_commits values ('"+ str(commit) +"','"+ str(bug_id) +"', to_timestamp("+bug_report_date+", 'Dy Mon DD HH24:MI:SS YYYY'), null, '"+ str(commit_date) +"' ,null)")
                    break  
            if bug_report_date == None:
                # insert line with it was not able to find a formated date  
                cursor.execute("insert into bugfix_commits values ('"+ str(commit) +"','"+ str(bug_id) +"', null, null, '"+ str(commit_date) +"',null)")                  
        else:
            print "not found file: "+ directory+file_name
        counter = counter + 1
        print str(counter)+ " out of: " + str(total_rows)  

except Exception, e:
    print  e
    connection.rollback()

finally:
    print "commiting"
    connection.commit()
    