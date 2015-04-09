drop table if exists git_commit_classification;
CREATE TABLE git_commit_classification (
  commit        text,                        
  tree          text,                       
  author        text,                        
  author_dt     timestamp without time zone, 
  release       integer,
  author_id     text,                        
  committer     text,                       
  committer_dt  timestamp without time zone, 
  committer_id  text,                        
  subject       text,                        
  num_children  integer,                     
  num_parents   integer,                     
  log           text,                        
  classification text, 
  username      text,                        
  period        integer,                     
  PRIMARY KEY  (commit)
);

insert into git_commit_classification(commit, tree, author, author_dt, author_id, committer, committer_dt, committer_id, subject, num_children, num_parents, log, username, period) 
    select commit, tree, author, author_dt, author_id, committer, committer_dt, committer_id, subject, num_children, num_parents, log, username, period
        from git_commit_backup ; 

-- populate the table with releases.

