# Logs Analysis Project
Submitted as part of the Udacity Full Stack Web Developer Nanodegree.

## Project Prompt
Write SQL queries to build an internal reporting tool for a newspaper site that answers the following: 

1. What are the three most popular articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Setting up and Running the Reporting Tool

#### Install the Virtual Machine
Follow the instructions given [here](https://github.com/udacity/fullstack-nanodegree-vm) to install [VirtualBox](https://www.virtualbox.org/), [Vagrant](https://www.vagrantup.com/) and set up the virtual machine (VM) that we will use to run the reporting tool.

#### Download the Data
After setting up the VM, log into it using `vagrant ssh`. Download the dataset [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Unzip the file after downloading and put it in the folder `/vagrant` which is shared with the `vagrant` folder on your local machine. To load the data, `cd` into `/vagrant` and use the command `psql -d news -f newsdata.sql` to execute the SQL commands in the downloaded file, that creates tables and populates them with data.

#### Run the Reporting Tool
In order to solve question 3 of the project prompt above, we created a view of the dataset that counts both the total number of requests and errors on each day, as below:
```
CREATE VIEW errorlog as 
SELECT time::date, 
       count(status) as total, 
       count(case when status = '404 NOT FOUND' then 1 else null end) as error
FROM   log 
GROUP BY time::date; 
```
Download the python file `logsanalysis.py` into `/vagrant`. Now, we can run the reporting tool using the command `python logsanalysis.py > out.txt` from within the VM. The answers will be available in the text file `out.txt`.
