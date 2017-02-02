import csv
#import  mysql.connector
import random
import string
#from mysql.connector import errorcode
import pymysql.cursors
import masterScraper as MS
import json
from random import randint

connection = pymysql.connect(host='localhost',
								user = 'root',
								password = '',
								db='JOBSEARCH',
								charset = 'utf8mb4',
								cursorclass=pymysql.cursors.DictCursor)

def database_insert():	
	try:
		with connection.cursor() as cursor:
			add_participant_data = "INSERT INTO PARTICIPANT(NAME,participant_id,email_addr,job_loc,job_keywords,job_type,num_job_post) VALUES(%s, %s, %s, %s, %s, %s, %s)"
			
			f = open("bs.csv", 'rU')

			csv_f = csv.reader(f)
			i=-1
			for row in csv_f:
				i+=1
				if i<2:
					continue
				rand = row[0][2:]+''.join(random.choice(string.ascii_letters +string.digits) for _ in range(5))
				'''			print(rand)#response id
				print(row[2])	#name
				print(row[4])	#email_addr
				print(row[10])	#joblocation
				print(row[11])	#keywords
				print(row[12])	#jobtype
				print(row[13])	#num_posting
			#	list = (rand,row[2],row[4],row[10],row[11],row[12],row[13])
				'''
				list = (row[2],rand,row[4],row[10],row[11],row[12],row[13])
			#	print(list)
				cursor.execute(add_participant_data,list)
		connection.commit()
		print('Insert into Participant table successful!')
	except Exception as e:
		print(e)

def call_scraper():
	try:
		with connection.cursor() as cursor:
			sql_select = "SELECT * FROM PARTICIPANT"
			sql_insert = "INSERT INTO JOB_SEARCH_RESULTS (job_search_id, participant_id, url, company, location, time_posted, job_title, snippet) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
			cursor.execute(sql_select)
			result = cursor.fetchall()
			for i in range(0,len(result)):
				participant_id = result[i]['participant_id']
				job_results = MS.jobs_master(result[i]['job_keywords'],result[i]['job_loc'],result[i]['num_job_post'])
		#		print(participant_id,result[i]['job_keywords'],result[i]['job_loc'],result[i]['num_job_post'],'/n')
				json_jobs = json.loads(job_results)
				for i in json_jobs:
					li = (None,participant_id,i['url'],i['company'],i['formattedLocationFull'],i['formattedRelativeTime'],i['jobtitle'],i['snippet'])
					cursor.execute(sql_insert,li)
		connection.commit()
		print('Insert into Job Search Results table successful!')
	except Exception as e:
		print(e)
	finally:
		print('connection closed')
		connection.close()

def main():
	database_insert()
	call_scraper()


main()
