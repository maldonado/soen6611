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

    cursor.execute("create table releases (release_number integer primary key, release_date date)")

    cursor.execute("insert into   releases values ('17', to_date('Dec 5th, 2011', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('18', to_date('Jan 30th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('19', to_date('Mar 26th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('20', to_date('May 7th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('21', to_date('Jun 18th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('22', to_date('Aug 6th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('23', to_date('Sept 17th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('24', to_date('Oct 29th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('25', to_date('Dec 17th, 2012', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('26', to_date('Feb 11th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('27', to_date('Mar 25th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('28', to_date('May 6th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('29', to_date('Jun 24th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('30', to_date('Aug 12th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('31', to_date('Sept 23rd, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('32', to_date('Nov 4th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('33', to_date('Dec 16th, 2013', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('34', to_date('Feb 17th, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('35', to_date('Mar 31st, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('36', to_date('May 9th, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('37', to_date('Jun 20th, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('38', to_date('Aug 15th, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('39', to_date('Sep 26th, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('40', to_date('Nov 7th, 2014', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('41', to_date('Jan 9th, 2015', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('42', to_date('Feb 20th, 2015', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('43', to_date('Apr 03rd, 2015', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('44', to_date('May 15th, 2015', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('45', to_date('Jun 26th, 2015', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('46', to_date('Aug 21st, 2015', 'Mon DDth, YYYY'))") 
    cursor.execute("insert into  releases values ('47', to_date('Oct 02nd, 2015', 'Mon DDth, YYYY'))") 

    

        
except Exception, e:
    print  e
    connection.rollback()

finally:
    connection.commit()