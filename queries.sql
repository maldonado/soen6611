-- scraped_bug_summary (in this table you will find bug log, bug severity, bug closing date etc)
-- git_revision_backup (this table has the commit numbers and its respective files)
-- git_commit_backup (this table has the author's name, the commit and the commit log)
-- bugfix_commits2 (this table you will find the commit that solved the bug, the commit date and the release that commit was made).
-- bug_info (you have a bug ID and if this bug was reported by project member or an user).
-- release (contains the first date and last date of each release).

select * from bug_info a, bugfix_commits2 b where a.bug_id = b.bug_id limit 10;

select id, priority, release, iteration, status, modified, modified_timestamp, modified_timestamp2 from scraped_bug_summary where release is not null limit 100

#the author_date in the bugfix_commits2 table are stored with timezone, taking that into consideration will allow us to have the same date from git_commits_backup and bugfix_commits2
-- http://stackoverflow.com/questions/9571392/ignoring-timezones-altogether-in-rails-and-postgresql
select commit ,  release , bug_id,  author_date  at time zone 'utc'  from bugfix_commits2 limit 2

#add column to set reported date.
alter table bugfix_commits2 add column bug_reported_date timestamp ;

#python regex
--http://stackoverflow.com/questions/14840310/python-using-re-module-to-parse-an-imported-text-file

update bugfix_commits2 set bug_reported_date = to_timestamp('Tue Nov 15 13:48:12 2011', 'Dy Mon DD HH24:MI:SS YYYY') where bug_id = '32321';
--http://stackoverflow.com/questions/17833176/postgresql-days-months-years-between-two-dates
select age(author_date, bug_reported_date) from bugfix_commits2;

change the types of the columns 
--http://stackoverflow.com/questions/7683359/how-to-change-column-datatype-from-character-to-numeric-in-postgresql-8-4
alter table releases alter column release_number type numeric (10,0) using release_number::numeric;

select * from bugfix_commits2 bf , releses r where bf.relese = r.relese_number;

select count(*) from bugfix_commits where bug_reported_release

-------------------------------------------------------------------------------------------------------------------------------------------------------------

