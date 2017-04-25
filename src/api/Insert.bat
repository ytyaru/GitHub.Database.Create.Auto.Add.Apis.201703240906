@echo off
set sqlite=sqlite3.exe
set sql_dir=%~dp0res/sql/insert/
set db=%~dp0res/db/GitHub.Apis.sqlite3
"%sqlite%" "%db%" < "%sql_dir%Apis.sql"
