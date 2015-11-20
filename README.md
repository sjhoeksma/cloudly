Cloudly
=======

[![Codacy Badge](https://api.codacy.com/project/badge/grade/da6052b0ab774f03ac5fe999bea91da5)](https://www.codacy.com/app/koon/cloudly)

Project Cloudly is "The Easiest To Setup" software to Monitor and to control your servers.  It's a first line of defence for your servers and also the ultimate Management Dashboard for your Cloud.
It saves you money and the energies by taking away most of the usual servers monitoring complexities allowing you to focus more on control and better use of your infrastructure.

Cloudly can scale to writing millions of data per 'second' on commodity servers with regular spinning hard drives.  This is due and thanks to the technologies it utilises (e.g. Hadoop/OpenTSDB to begin with).

Cloudly is fully automated and does the servers monitoring for you with close to nothing to setup.



Installation Instructions
-------------------------

In order to run this project in what we call the "Enterprise Mode", please follow the installation instructions below.


###### Install various python modules and git

<pre>
$ apt-get install git
$ apt-get install python-dev
$ apt-get install python-django
$ apt-get install python-openssl
$ apt-get install python-pip
</pre>

###### Download the latest version of the Cloudly Project from github

<pre>
$ sudo adduser cloudly
$ su - cloudly
$ git clone https://github.com/ProjectCloudly/cloudly cloudly
$ cd cloudly
</pre>

###### Define project settings

We have prepared an example configuration, just copy it over and modify to meet your specific requirements.

<pre>
$ cp -f cloudly/settings.py.sample cloudly/settings.py
</pre>

###### Install the MongoDB and its python connectors

<pre>
$ apt-get install mongodb
$ pip install pymongo
$ mongoimport --db cloudly --collection services_tags services_tags.json
</pre>

..and configure your server to meet your specific requirements.

###### Install MySQL server and Python MySQLdb

<pre>
$ apt-get install mysql-server python-mysqldb
</pre>

Optionally configure your MySQL server to meet your specific requirements.

As for the user/password, this one needs to match the entries in the cloudly/cloudly/settings.py file.

###### Create the ORM database and tables

<pre>
$ sudo pip install pymysql
$ mysql -u root -p
mysql> create database cloudly;
</pre>

<pre>
$ python manage.py syncdb
</pre>

If you get an error saying "Access denied for user 'root'@'localhost" then you'd need to edit the cloudly/settings.py and setup the DB section accordingly to your present DB settings.

Assuming this operation succeded, Django will ask you the following:

<pre>
You just installed Django's auth system, which means you don't have any superusers defined.
Would you like to create one now? (yes/no): no
</pre>

Answer "no" to this question.


###### Enable Unicode on the SQL database

<pre>
$ mysql -u root -p
mysql> use cloudly;
mysql> ALTER DATABASE cloudly charset=utf8;
mysql> ALTER TABLE userprofile_profile CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci;
</pre>

* please note that the MySQL is used only to store users profiles and sessions information.

###### Run the MongoDB

<pre>
$ sudo mkdir /data
$ sudo mkdir /data/db
$ mongod
</pre>

..and configure your server to meet your specific requirements.

###### Run the development server

At this point you should be able to run the administration dashboard (Django App):

<pre>
$ echo Never run this as user root!
$ ./run_devel.sh
</pre>

Now that you have the User Interface (Admin Dashboard) up and running you'd need to get the API started.  You can do so by following the instructions in the next step.


###### Run the API

API server runs off of Flask therefore you'd need to install Python Flask first.  To do so simply copy and paste the following into your terminal window:

<pre>
$ apt-get install python-flask
</pre>

Once you have the Flask installed, simply run the API like so:

<pre>
$ python api.py
</pre>


DB Backends
-----------

###### Install OpenTSDB

Cloudly runs off of Hadoop and is powered by the OpenTSBD.  Please refer to the official OpenTSDB documentation for installation instructions - http://opentsdb.net/docs/build/html/installation.html

..and that's that!  :)

Enjoy!


Screenshots & Live Demo
-----------------------

![alt screen0](https://raw.githubusercontent.com/jparicka/cloudly/master/static/screenshots/screenshot0.png)

![alt screen1](https://raw.githubusercontent.com/jparicka/cloudly/master/static/screenshots/screenshot1.png)

###### Demo

Project can be currently seen on https://projectcloudly.org/demo
