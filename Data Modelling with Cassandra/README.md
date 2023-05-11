# Project: Data Modeling with Apache Cassandra

## Introduction

This project was completed as part of Udacity's Data Engineering Nanodegree program.

A startup called *Sparkify* wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, there is no easy way to query the data to generate results, since the data reside in a directory of __CSV files__ on user activity on the app. The CSV files are partitioned by date. 

They'd like a __data engineer__ to create an __Apache Cassandra database__ using __Python__ which can create queries on song play data to answer their questions, and wish to bring you on the project. Your role is to create a database for this analysis. You'll be able to test your database by running queries given to you by the analytics team from Sparkify to create the results.

## Project Description

The goal of this project was to model the data by creating tables in Apache Cassandra to run queries on. 
The ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables was provided. The provided project template takes care of all the imports and provides a structure for an ETL pipeline that I needed to process this data.

## ETL Pipeline
I was provided with part of the ETL pipeline that transfers data from a set of CSV files within a directory to create a streamlined CSV file to model and insert data into Apache Cassandra tables. The provided project template takes care of all the imports and provides a structure for an ETL pipeline that I needed to process this data.

## Customer Requests on Data and Final Queries
I had to create the data tables in Apache Cassandra based on the queries and the queries are based on the customer's request for data. The completed __data model__ can be examined in the _Project_1B_Data_Modeling_with_Cassandra.ipynb_ Jupyter Notebook. 
1.   Give me the artist, song title and song's length in the music app history that was heard during sessionId = 338, and itemInSession = 4:
> **Query Description:** In this query, we only need the sessionId and itemInSession columns in the primary key as these columns are effectively the where clause for the query.
>
> `select artist, song, length from song_info_by_session_id where sessionId=338 and itemInSession=4`

2. Give me only the following: name of artist, song (sorted by itemInSession) and user (first and last name) for userid = 10, sessionid = 182:
> **Query Description:** In this query, userId and sessionId make up the primary key as they are effectively the where clause.  
> itemInSession is the clustering key as we need to sort by this column.
>
> `select artist, song, user from song_info_by_user_and_session_id where userId=10 and sessionId=182`

3. Give me every user name (first and last) in my music app history who listened to the song 'All Hands Against His Own':
> **Query Description:** In this query, we need the song in the primary key but also the userId.  
> We cannot use first name and last name in the primary key in case there are two or more people with the same first name and last name.
>
> `select song, user from user_name_by_song where song='All Hands Against His Own``
