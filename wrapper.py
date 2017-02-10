import csv
#import  mysql.connector
import random
import string
#from mysql.connector import errorcode
#import pymysql.cursors
import psycopg2
import masterScraper as MS
import json
from random import randint
import uuid

def database_insert():	
	try:
#		connection = psycopg2.connect(database='jobportal', user = 'ankitasastry')
		connection = psycopg2.connect("host='ec2-54-243-185-132.compute-1.amazonaws.com' dbname='d2ftjp5a24rakj' user='bgcdtjsazvveou' password='b8288eda378a650ad70687aff55ac3bdcd0f73dc634bc5f3a6a63847b4259308'")
		cur = connection.cursor()
		add_participant_data = "INSERT INTO PARTICIPANT(name,participant_id,email_addr,job_loc,job_keywords,job_type,num_job_post) VALUES(%s, %s, %s, %s, %s, %s, %s);"
#		add_participant_data = "INSERT INTO PARTICIPANT (SELECT * FROM( VALUES(%s, %s, %s, %s, %s, %s, %s)) AS tmp(name, part_id, email, loc, keywds, type, num_post) WHERE NOT EXISTS ( SELECT 1 FROM PARTICIPANT WHERE participant_id = tmp.part_id));"
			
		f = open("bs.csv", 'rU')
		csv_f = csv.reader(f)
		i=-1
		for row in csv_f:
			i+=1
			if i<2:
				continue
			rand = row[0][2:]+''.join(random.choice(string.ascii_letters +string.digits) for _ in range(5))
			list = (row[2],rand,row[4],row[10],row[11],row[12],row[13])
			sql_select = "SELECT * FROM PARTICIPANT WHERE participant_id='"+rand+"';"
			cur.execute(sql_select)
			res = cur.fetchall()
			if(res == None):
				cur.execute(add_participant_data,list)
			
		connection.commit()

		print('Insert into Participant table successful!')
	except psycopg2.DatabaseError, e:
		if connection:
			connection.rollback()
		print(e)

	finally:
		if connection:
			connection.close()
		

def call_scraper():
	try:
#		connection = psycopg2.connect(database='jobportal', user = 'ankitasastry')
		connection = psycopg2.connect("host='ec2-54-243-185-132.compute-1.amazonaws.com' dbname='d2ftjp5a24rakj' user='bgcdtjsazvveou' password='b8288eda378a650ad70687aff55ac3bdcd0f73dc634bc5f3a6a63847b4259308'")

		cur = connection.cursor()
		sql_select = "SELECT * FROM PARTICIPANT;"
		sql_insert = "INSERT INTO JOB_SEARCH_RESULTS (job_search_id, participant_id, url, company, location, time_posted, job_title, snippet) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
		cur.execute(sql_select)
		result = cur.fetchall()
#		print(result[0][1])
		for i in range(0,len(result)):
			#participant_id = result[i]['participant_id']
			participant_id = result[i][1]
#			job_results = MS.jobs_master(result[i]['job_keywords'],result[i]['job_loc'],result[i]['num_job_post'])
			job_results = MS.jobs_master(result[i][5],result[i][4],result[i][7])
		#		print(participant_id,result[i]['job_keywords'],result[i]['job_loc'],result[i]['num_job_post'],'/n')
			json_jobs = json.loads(job_results)
			for i in json_jobs:
				job_srch_id = str(uuid.uuid4())
				li = (job_srch_id,participant_id,i['url'],i['company'],i['formattedLocationFull'],i['formattedRelativeTime'],i['jobtitle'],i['snippet'])
				sql_select_jobs = "SELECT * FROM JOB_SEARCH_RESULTS WHERE job_search_id='"+job_srch_id+"' AND participant_id='"+participant_id+"';"
				cur.execute(sql_select_jobs)
				res1 = cur.fetchone()
				if(res1 == None):
					cur.execute(sql_insert,li)
					connection.commit()
		print('Insert into Job Search Results table successful!')
	except psycopg2.DatabaseError, e:
		if connection:
			connection.rollback()
		print(e)
	finally:
		if connection:
			connection.close()

def main():
	database_insert()
	call_scraper()


main()
