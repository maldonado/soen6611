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

    cursor.execute("drop table releases")
    cursor.execute("create table releases (release_number integer primary key, release_date date)")

    # -- development channel releases 
    # cursor.execute("insert into   releases values ('17', to_date('Dec 5th, 2011', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('18', to_date('Jan 30th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('19', to_date('Mar 26th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('20', to_date('May 7th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('21', to_date('Jun 18th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('22', to_date('Aug 6th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('23', to_date('Sept 17th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('24', to_date('Oct 29th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('25', to_date('Dec 17th, 2012', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('26', to_date('Feb 11th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('27', to_date('Mar 25th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('28', to_date('May 6th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('29', to_date('Jun 24th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('30', to_date('Aug 12th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('31', to_date('Sept 23rd, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('32', to_date('Nov 4th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('33', to_date('Dec 16th, 2013', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('34', to_date('Feb 17th, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('35', to_date('Mar 31st, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('36', to_date('May 9th, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('37', to_date('Jun 20th, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('38', to_date('Aug 15th, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('39', to_date('Sep 26th, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('40', to_date('Nov 7th, 2014', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('41', to_date('Jan 9th, 2015', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('42', to_date('Feb 20th, 2015', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('43', to_date('Apr 03rd, 2015', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('44', to_date('May 15th, 2015', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('45', to_date('Jun 26th, 2015', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('46', to_date('Aug 21st, 2015', 'Mon DDth, YYYY'))") 
    # cursor.execute("insert into  releases values ('47', to_date('Oct 02nd, 2015', 'Mon DDth, YYYY'))") 


    # -- stable channel releases
    cursor.execute("insert into  releases values ('1', to_date('THURSDAY, DECEMBER 11, 2008', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('2', to_date('THURSDAY, MAY 21, 2009', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('3', to_date('TUESDAY, SEPTEMBER 15, 2009', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('4', to_date('MONDAY, JANUARY 25, 2010', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('5', to_date('TUESDAY, MAY 25, 2010', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('6', to_date('THURSDAY, SEPTEMBER 2, 2010', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('7', to_date('TUESDAY, OCTOBER 19, 2010', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('8', to_date('THURSDAY, DECEMBER 2, 2010', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('9', to_date('THURSDAY, FEBRUARY 3, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('10', to_date('TUESDAY, MARCH 8, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('11', to_date('WEDNESDAY, APRIL 27, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('12', to_date('TUESDAY, JUNE 7, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('13', to_date('TUESDAY, AUGUST 2, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('14', to_date('FRIDAY, SEPTEMBER 16, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('15', to_date('TUESDAY, OCTOBER 25, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('16', to_date('TUESDAY, DECEMBER 13, 2011', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('17', to_date('WEDNESDAY, FEBRUARY 8, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('18', to_date('WEDNESDAY, MARCH 28, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('19', to_date('TUESDAY, MAY 15, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('20', to_date('TUESDAY, JUNE 26, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('21', to_date('TUESDAY, JULY 31, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('22', to_date('TUESDAY, SEPTEMBER 25, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('23', to_date('FRIDAY, NOVEMBER 2, 2012', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('24', to_date('THURSDAY, JANUARY 10, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('25', to_date('THURSDAY, FEBRUARY 21, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('26', to_date('TUESDAY, MARCH 26, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('27', to_date('TUESDAY, MAY 21, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('28', to_date('TUESDAY, JULY 9, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('29', to_date('TUESDAY, AUGUST 20, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('30', to_date('TUESDAY, OCTOBER 1, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('31', to_date('TUESDAY, NOVEMBER 12, 2013', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('32', to_date('TUESDAY, JANUARY 14, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('33', to_date('THURSDAY, FEBRUARY 20, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('34', to_date('TUESDAY, APRIL 8, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('35', to_date('TUESDAY, MAY 20, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('36', to_date('WEDNESDAY, JULY 16, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('37', to_date('TUESDAY, AUGUST 26, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('38', to_date('TUESDAY, OCTOBER 7, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('39', to_date('TUESDAY, NOVEMBER 18, 2014', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('40', to_date('WEDNESDAY, JANUARY 21, 2015', 'DAY, MONTH DD, YYYY'))") 
    cursor.execute("insert into  releases values ('41', to_date('TUESDAY, MARCH 3, 2015', 'DAY, MONTH DD, YYYY'))") 
        
except Exception, e:
    print  e
    connection.rollback()

finally:
    connection.commit()