import os
import psycopg2
import sys
import datetime

connection = None

try:
    
    #connect to the database 
    connection = psycopg2.connect(host='cranberry', port='5432', database='everton_soen6611', user='everton', password='evermal01')
    cursor = connection.cursor()

    cursor.execute("select commit, author_dt from git_commit_classification")
    commit_dates = cursor.fetchall()

    cursor.execute("select release_number from releases order by 1")
    releases = cursor.fetchall()
    
    counter = 0
    total_rows = len(commit_dates)

    last_release_item = releases[-1]
    last_release = last_release_item[0]

    for line in commit_dates:
        commit = line[0]
        commit_date = line[1]    
        
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
                    cursor.execute("update git_commit_classification set release ='"+str(release_number)+"' where commit = '"+ str(commit) +"'")
        
        counter = counter  + 1
        print str(counter) + " out of: " + str(total_rows)                              

except Exception, e:
    print  e
    connection.rollback()

finally:
    print "commiting"
    connection.commit()