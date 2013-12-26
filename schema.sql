drop table if exists entries;
create table entries (
       title text not null,
       sender text not null,
       recipient text not null,
       message text not null, 
       background text not null
);