#!/usr/bin/python

import os
import psycopg2
import sys
import re
import csv

connection = None

try:
    
    #connect to the database to retrieve the file name linked with the commit
    connection = psycopg2.connect(host='cranberry', port='5432', database='everton_soen6611', user='everton', password='evermal01')
    cursor = connection.cursor()
    
    # select all versions
    cursor.execute("select release_number from releases order by 1")
    releases = cursor.fetchall()


    with open('bugfix_distribution.csv', 'w') as csvfile:
        fieldnames = ['analyzed_release', 'total_bug_fixes', 'release_1', 'release_2', 'release_3', 'release_4', 'release_5', 'release_6', 'release_7', 'release_8', 'release_9', 'release_10', 'release_11', 'release_12', 'release_13', 'release_14', 'release_15', 'release_16', 'release_17', 'release_18', 'release_19', 'release_20', 'release_21', 'release_22', 'release_23', 'release_24', 'release_25', 'release_26', 'release_27', 'release_28', 'release_29', 'release_30','release_31','release_32','release_33','release_34','release_35','release_36','release_37','release_38','release_39','release_40','release_41' ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        # for each version select all bugfix_commits registers that has the same release number that the one analyzed
        for release in releases:
            release_1_counter = 0
            release_2_counter = 0
            release_3_counter = 0
            release_4_counter = 0
            release_5_counter = 0
            release_6_counter = 0
            release_7_counter = 0
            release_8_counter = 0
            release_9_counter = 0
            release_10_counter = 0
            release_11_counter = 0
            release_12_counter = 0
            release_13_counter = 0
            release_14_counter = 0
            release_15_counter = 0
            release_16_counter = 0
            release_17_counter = 0
            release_18_counter = 0
            release_19_counter = 0
            release_20_counter = 0
            release_21_counter = 0
            release_22_counter = 0
            release_23_counter = 0
            release_24_counter = 0
            release_25_counter = 0
            release_26_counter = 0
            release_27_counter = 0
            release_28_counter = 0
            release_29_counter = 0
            release_30_counter = 0
            release_31_counter = 0
            release_32_counter = 0
            release_33_counter = 0
            release_34_counter = 0
            release_35_counter = 0
            release_36_counter = 0
            release_37_counter = 0
            release_38_counter = 0
            release_39_counter = 0
            release_40_counter = 0
            release_41_counter = 0

            release_number =  release[0]
            cursor.execute("select commit, bug_id, bug_report_date, bug_report_release, commit_date, commit_release from bugfix_commits where bug_report_release = '"+ str(release_number) +"'")
            rows = cursor.fetchall()
            # store the number of registers found as the bugs reported in that version
            print "release: " + str(release_number) + " number of bugs: " + str(len(rows)) 
            # for each version check how many of then were fixed in the same version
            for row in rows:
                commit_release = row[5]
                if commit_release == 1:
                    release_1_counter = release_1_counter + 1
                if commit_release == 2:
                    release_2_counter = release_2_counter + 1
                if commit_release == 3:
                    release_3_counter = release_3_counter + 1
                if commit_release == 4:
                    release_4_counter = release_4_counter + 1
                if commit_release == 5:
                    release_5_counter = release_5_counter + 1
                if commit_release == 6:
                    release_6_counter = release_6_counter + 1
                if commit_release == 7:
                    release_7_counter = release_7_counter + 1
                if commit_release == 8:
                    release_8_counter = release_8_counter + 1
                if commit_release == 9:
                    release_9_counter = release_9_counter + 1
                if commit_release == 10:
                    release_10_counter = release_10_counter + 1
                if commit_release == 11:
                    release_11_counter = release_11_counter + 1
                if commit_release == 12:
                    release_12_counter = release_12_counter + 1
                if commit_release == 13:
                    release_13_counter = release_13_counter + 1
                if commit_release == 14:
                    release_14_counter = release_14_counter + 1
                if commit_release == 15:
                    release_15_counter = release_15_counter + 1
                if commit_release == 16:
                    release_16_counter = release_16_counter + 1
                if commit_release == 17:
                    release_17_counter = release_17_counter + 1
                if commit_release == 18:
                    release_18_counter = release_18_counter + 1
                if commit_release == 19:
                    release_19_counter = release_19_counter + 1
                if commit_release == 20:
                    release_20_counter = release_20_counter + 1
                if commit_release == 21:
                    release_21_counter = release_21_counter + 1
                if commit_release == 22:
                    release_22_counter = release_22_counter + 1
                if commit_release == 23:
                    release_23_counter = release_23_counter + 1
                if commit_release == 24:
                    release_24_counter = release_24_counter + 1
                if commit_release == 25:
                    release_25_counter = release_25_counter + 1
                if commit_release == 26:
                    release_26_counter = release_26_counter + 1
                if commit_release == 27:
                    release_27_counter = release_27_counter + 1
                if commit_release == 28:
                    release_28_counter = release_28_counter + 1
                if commit_release == 29:
                    release_29_counter = release_29_counter + 1
                if commit_release == 30:
                    release_30_counter = release_30_counter + 1
                if commit_release == 31:
                    release_31_counter = release_31_counter + 1
                if commit_release == 32:
                    release_32_counter = release_32_counter + 1
                if commit_release == 33:
                    release_33_counter = release_33_counter + 1
                if commit_release == 34:
                    release_34_counter = release_34_counter + 1
                if commit_release == 35:
                    release_35_counter = release_35_counter + 1
                if commit_release == 36:
                    release_36_counter = release_36_counter + 1
                if commit_release == 37:
                    release_37_counter = release_37_counter + 1
                if commit_release == 38:
                    release_38_counter = release_38_counter + 1
                if commit_release == 39:
                    release_39_counter = release_39_counter + 1
                if commit_release == 40:
                    release_40_counter = release_40_counter + 1
                if commit_release == 41:
                    release_41_counter = release_41_counter + 1


            if release_1_counter > 0:
                print "release 1 :" + str(release_1_counter)
            if release_2_counter > 0:
                print "release 2 :" + str(release_2_counter)    
            if release_3_counter > 0:
                print "release 3 :" + str(release_3_counter)
            if release_4_counter > 0:
                print "release 4 :" + str(release_4_counter)
            if release_5_counter > 0:
                print "release 5 :" + str(release_5_counter)
            if release_6_counter > 0:
                print "release 6 :" + str(release_6_counter)
            if release_7_counter > 0:
                print "release 7 :" + str(release_7_counter)
            if release_8_counter > 0:
                print "release 8 :" + str(release_8_counter)
            if release_9_counter > 0:
                print "release 9 :" + str(release_9_counter)
            if release_10_counter > 0:
                print "release 10: " + str(release_10_counter)
            if release_11_counter > 0:
                print "release 11: " + str(release_11_counter)
            if release_12_counter > 0:
                print "release 12: " + str(release_12_counter)    
            if release_13_counter > 0:
                print "release 13: " + str(release_13_counter)
            if release_14_counter > 0:
                print "release 14: " + str(release_14_counter)
            if release_15_counter > 0:
                print "release 15: " + str(release_15_counter)
            if release_16_counter > 0:
                print "release 16: " + str(release_16_counter)
            if release_17_counter > 0:
                print "release 17: " + str(release_17_counter)
            if release_18_counter > 0:
                print "release 18: " + str(release_18_counter)
            if release_19_counter > 0:
                print "release 19: " + str(release_19_counter)
            if release_20_counter > 0:
                print "release 20: " + str(release_20_counter)
            if release_21_counter > 0:
                print "release 21: " + str(release_21_counter)
            if release_22_counter > 0:
                print "release 22: " + str(release_22_counter)    
            if release_23_counter > 0:
                print "release 23: " + str(release_23_counter)
            if release_24_counter > 0:
                print "release 24: " + str(release_24_counter)
            if release_25_counter > 0:
                print "release 25: " + str(release_25_counter)
            if release_26_counter > 0:
                print "release 26: " + str(release_26_counter)
            if release_27_counter > 0:
                print "release 27: " + str(release_27_counter)
            if release_28_counter > 0:
                print "release 28: " + str(release_28_counter)
            if release_29_counter > 0:
                print "release 29: " + str(release_29_counter)
            if release_30_counter > 0:
                print "release 30: " + str(release_30_counter)
            if release_31_counter > 0:
                print "release 31: " + str(release_31_counter)
            if release_32_counter > 0:
                print "release 32: " + str(release_32_counter)    
            if release_33_counter > 0:
                print "release 33: " + str(release_33_counter)
            if release_34_counter > 0:
                print "release 34: " + str(release_34_counter)
            if release_35_counter > 0:
                print "release 35: " + str(release_35_counter)
            if release_36_counter > 0:
                print "release 36: " + str(release_36_counter)
            if release_37_counter > 0:
                print "release 37: " + str(release_37_counter)
            if release_38_counter > 0:
                print "release 38: " + str(release_38_counter)
            if release_39_counter > 0:
                print "release 39: " + str(release_39_counter)
            if release_40_counter > 0:
                print "release 40: " + str(release_40_counter)                
            if release_41_counter > 0:
                print "release 41: " + str(release_41_counter)

            writer.writerow({'analyzed_release': release_number, 'total_bug_fixes': len(rows), 'release_1': release_1_counter, 'release_2': release_2_counter, 'release_3': release_3_counter, 'release_4': release_4_counter, 'release_5': release_5_counter, 'release_6': release_6_counter, 'release_7': release_7_counter, 'release_8': release_8_counter, 'release_9': release_9_counter, 'release_10': release_10_counter, 'release_11': release_11_counter, 'release_12': release_12_counter, 'release_13': release_13_counter, 'release_14': release_14_counter, 'release_15': release_15_counter, 'release_16': release_16_counter, 'release_17': release_17_counter, 'release_18': release_18_counter, 'release_19': release_19_counter, 'release_20': release_20_counter, 'release_21': release_21_counter, 'release_22': release_22_counter, 'release_23': release_23_counter, 'release_24': release_24_counter, 'release_25': release_25_counter, 'release_26': release_26_counter, 'release_27': release_27_counter, 'release_28': release_28_counter, 'release_29': release_29_counter, 'release_30': release_30_counter,'release_31': release_31_counter,'release_32': release_32_counter,'release_33': release_33_counter,'release_34': release_34_counter,'release_35': release_35_counter,'release_36': release_36_counter,'release_37': release_37_counter,'release_38': release_38_counter,'release_39': release_39_counter,'release_40': release_40_counter,'release_41': release_41_counter})

except Exception, e:
    print  e
    

finally:
    print "finished"
    