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
    
    # select all versions
    cursor.execute("select release_number from releases order by 1")
    releases = cursor.fetchall()

    # for each version select all bugfix_commits registers that has the same release number that the one analyzed
    for release in releases:
        same_release_counter = 0
        future_release_counter = 0
        previous_release_counter = 0

        release_number =  release[0]
        cursor.execute("select commit, bug_id, bug_report_date, bug_report_release, commit_date, commit_release from bugfix_commits where bug_report_release = '"+ str(release_number) +"'")
        rows = cursor.fetchall()
        # store the number of registers found as the bugs reported in that version
        print "release: " + str(release_number) + " number of bugs: " + str(len(rows)) 
        # for each version check how many of then were fixed in the same version
        for row in rows:
            bug_report_release = row[3]
            commit_release = row[5]
            if bug_report_release is not None and commit_release is not None:
                if bug_report_release == commit_release:
                    same_release_counter = same_release_counter + 1
                # for each version check how many of then were fixed in a future version
                # if bug_report_release < commit_release:
                if (bug_report_release - commit_release) < -1:
                    future_release_counter = future_release_counter + 1
                # for each version check how many of then were fixed in a previous version (should not happen)
                if bug_report_release > commit_release: 
                    previous_release_counter = previous_release_counter + 1

        print "number of bugs: " + str(same_release_counter)
        print "number of DD: "  + str(future_release_counter)
        print "number of exceptions: " + str(previous_release_counter)

    
except Exception, e:
    print  e
    

finally:
    print "finished"
    