import indeedScraper as IS
#AS import jobGatewayScraper as GS
import csv
import pprint
import sys
import re
import json

# Walk B to find all jobs in A that are not in B, given
# that they have the same ordering
def jobDifference(jobsA, jobsB):
    result = []
    index = 0
    for job in jobsB:
        while index + 1 < len(jobsA) and jobsA[index] != job:
            result += [jobsA[index]]
            index = index + 1
        index = index + 1
    return result

# finding jobs which do not salary information
# Only for JobGateway, since indeed estimates salaries.
#ASdef getUnsalariedJobs(what, where, count, jobType, radius):
#AS    allJobs = GS.getRawJobs(what, where, count, jobType, radius, "0")
#AS    salariedJobs = GS.getRawJobs(what, where, count, jobType, radius, "1")

    # jobs which are in salariedJobs but not allJobs are notSalaried
#AS    return jobDifference(allJobs, salariedJobs)

# Fields Received for getJobs
#   company
#   jobtitle
#   url
#   snippet
#   formattedLocationFull
#   formattedRelativeTime
def getJobs(what, where, count, salaryRanges, jobType = "", radius = 50):
# salaryBrackets must be strictly increasing

    jobs = []
   #AS jobs += [[getUnsalariedJobs(what, where, count, jobType, radius), "Unsalaried", "Unsalaried"]]
    
    # Use 1 as salary to remove unsalaried jobs from query results
#    minSal = "1"
    minSal = "20000"

    # Since the ordering of the jobs are maintained across different salaries,
    # we use differences in salary queries to find jobs within ranges
    prevIndeedJobs = IS.getRawJobs(what, where, count, jobType, radius, minSal)
 #AS   prevGatewayJobs = GS.getRawJobs(what, where, count, jobType, radius, minSal)
    for maxSal in salaryRanges:
        indeedJobs = IS.getRawJobs(what, where, count, jobType, radius, maxSal)
  #AS      gatewayJobs = GS.getRawJobs(what, where, count, jobType, radius, maxSal)
        rangedJobs = jobDifference(prevIndeedJobs, indeedJobs) #AS + jobDifference(prevGatewayJobs, gatewayJobs)

        jobs += [[rangedJobs, minSal, maxSal]]

        prevIndeedJobs = indeedJobs
    #AS    prevGatewayJobs = gatewayJobs
        minSal = maxSal

 #AS  jobs += [[prevIndeedJobs + prevGatewayJobs, maxSal, "Unbounded"]]
    jobs += [[prevIndeedJobs , maxSal, "Unbounded"]]
    return jobs



def jobs_master(job_title, job_loc, job_num):     
    salaryRanges = ["10000", "50000", "100000"]
    #res = getJobs("Sales", "Pittsburgh", 10, salaryRanges)
    ####FInal results
    #####res = getJobs(sys.argv[1],sys.argv[2],int(sys.argv[3]),"10000")

 #   res = IS.getRawJobs(sys.argv[1],sys.argv[2],int(sys.argv[3]),jobType="",radius=50,salary="10000")
    res = IS.getRawJobs(job_title,job_loc,job_num,jobType="",radius=50,salary="10000")
    file = open('jobs.json','w')
    file.write(res)
    file.close()
#    print(res)
    return res
