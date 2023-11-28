# Crontab_py

## introduction
This crontab_py, is a python module that allows you to easily add, remove, and list cron jobs.

## example 

>from crontab_py import Crontab
ct = Crontab()
ct.add_job(
    cmd=”echo ‘hello world’”, 
    frequency=”* * * * *”, 
    path_to_log=”/tmp/crontab.log”, 
    id=”my_job”, description=”my job”)

## sphinx documentation
look at the documentation at https://anglisano.github.io/crontab_py/api_guide.html