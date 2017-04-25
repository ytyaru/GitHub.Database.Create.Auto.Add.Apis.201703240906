@echo off
set sqlite=sqlite3.exe
set db=%~dp0res/db/GitHub.Apis.sqlite3
set sql_dir=%~dp0res/sql/check/
"%sqlite%" "%db%" < "%sql_dir%check.sql"
