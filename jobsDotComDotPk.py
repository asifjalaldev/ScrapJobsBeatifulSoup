from bs4 import BeautifulSoup
import requests
import csv
source=requests.get('https://jobs.com.pk/').text
soup=BeautifulSoup(source, 'lxml')
jobs=soup.find_all('tr')

# open csv file
csv_file=open('jobs.csv', 'w')

csv_writer=csv.writer(csv_file)
csv_writer.writerow(['Job Title', 'Department', 'JOb Link'])

for job in jobs:

    job_title=job.find_all('td')[1].text

    job_link=job.td.a['href']

    job_dep=job.find_all('td')[0].text

    print(f'job_title: {job_title}')
    print(f'job_link: {job_link}')
    print(f'job_department: {job_dep}')
    csv_writer.writerow([job_title,job_dep,job_link])