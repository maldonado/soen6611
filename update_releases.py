import os
import psycopg2
import sys
import datetime

connection = None

try:
    
    #connect to the database 
    connection = psycopg2.connect(host='cranberry', port='5432', database='everton_soen6611', user='everton', password='evermal01')
    cursor = connection.cursor()

    cursor.execute("select commit, bug_id, commit_date, bug_report_date from bugfix_commits")
    commit_and_report_dates = cursor.fetchall()

    cursor.execute("select release_number from releases order by 1")
    releases = cursor.fetchall()
    
    counter = 0
    total_rows = len(commit_and_report_dates)

    for line in commit_and_report_dates:
        commit = line[0]
        bug_id = line[1]
        commit_date = line[2]
        bug_report_date = line[3]

        last_release_item = releases[-1]
        last_release = last_release_item[0]
        
        for release in releases:    
            release_number = release[0]
            # temp solution to take care of last version
            if release_number + 1 == last_release:
                break
            
            cursor.execute("select release_date from releases where release_number = '"+str(release_number)+"'")
            current_release_date_result = cursor.fetchone()
            current_release_date = current_release_date_result[0]

            cursor.execute("select release_date from releases where release_number = '"+str(release_number + 1) +"'")
            next_release_date_result = cursor.fetchone()
            next_release_date = next_release_date_result[0]
            
            
            if commit_date is not None:
                if current_release_date <= commit_date.date() < next_release_date:
                    # print current_release_date , commit_date.date() , next_release_date
                    # print "true commit_date"
                    if bug_report_date is None:
                        cursor.execute("update bugfix_commits set commit_release ='"+str(release_number)+"' where commit = '"+ str(commit) +"' and bug_id = '"+ str(bug_id) +"' and bug_report_date = null and commit_date ='"+ str(commit_date) +"'")
                    else:    
                        cursor.execute("update bugfix_commits set commit_release ='"+str(release_number)+"' where commit = '"+ str(commit) +"' and bug_id = '"+ str(bug_id) +"' and bug_report_date = '"+ str(bug_report_date) +"' and commit_date ='"+ str(commit_date) +"'")
            if bug_report_date is not None:
                if current_release_date <= bug_report_date.date() < next_release_date: 
                    # print current_release_date , bug_report_date.date() , next_release_date
                    # print "true commit_date"
                    if commit_date is None:
                        cursor.execute("update bugfix_commits set bug_report_release ='"+str(release_number)+"' where commit = '"+ str(commit) +"' and bug_id = '"+ str(bug_id) +"' and bug_report_date = '"+ str(bug_report_date) +"' and commit_date = null")
                    else:    
                        cursor.execute("update bugfix_commits set bug_report_release ='"+str(release_number)+"' where commit = '"+ str(commit) +"' and bug_id = '"+ str(bug_id) +"' and bug_report_date = '"+ str(bug_report_date) +"' and commit_date ='"+ str(commit_date) +"'")

        counter = counter + 1
        print str(counter)+ " out of: " + str(total_rows)                              

except Exception, e:
    print  e
    connection.rollback()

finally:
    print "commiting"
    connection.commit()