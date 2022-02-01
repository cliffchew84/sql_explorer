# SQL Script Explorer

Hi. I am a data analyst that has worked a lot with SQL. Unfortunately, like most data analysts, I eventually had to deal with a legacy database workflow that had 100s of SQL scripts with no documentation. Most of the data analysts who wrote those scripts have left the team, and the current team was kind of just winging it as we go along. Even more unfortunately, by my second year in this role, the team had to go through the dreaded process of a database workflow migration.

I tried searching for some open source tool, framework, or implementation that could help me map out my database workflows, but I couldn't find any. So in my extra time, I look through the logic of my database system, and wrote some Python scripts to map out all the SQL scripts that I had access to. With some very aggressive tinkering and ugly patch-and-go code, I patched up some google sheets "dashboard" that showed which scripts were using what tables, and what variables from those tables were in those scripts. 

## This repo would be useful to you if
1. You know Python and SQL.
2. You have access to the SQL scripts of your teams.
3. You want a mapping of the database tables used in your team's SQL scripts. 

## This repo WILL NOT...
1. Read your database to give you your table schemas. The repo doesn't have access to your database. It only looks at whatever SQL scripts that you have given it access to. 
2. Help you tune the performance of your database
3. Give you advice on how to write your SQL scripts

This is a side project that I am open-sourcing in my spare time. Because there are so many different SQL dialects and different use cases, I am quite confident that this repo will break for your use case. Feel free to do a Git push, and I will try my best to add those features into the repo. Looking forward to learn more from this online community as well.