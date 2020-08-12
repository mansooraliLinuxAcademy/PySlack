#!/usr/bin/python2.7
import os
import time
import requests
import json
import subprocess
import logging


web_hook_url ='https://hooks.slack.com/services/TN29ZMMAB******************mucwjJl7vJpKgEQucW'
checkstatus ='active'
service = os.getenv("SERVICE1", default="none")
cmd = "hostname -I | awk '{print $1}'"
d = os.popen(cmd).read()
#slack_msg = {'text':'\n*Region=AUS* \n Alert from _ip-10-20-0-53_ *US* \n *'+service+'*  is not running\n ######END#####','username': 'markdownbot', 'mrkdwn': 'true',"attachments":[{"fallback":"START or IGNORE","actions":[{"type":"button","name":"start-a-service","text":"START","style":"primary"},{"type":"button","name":"ignore-the-service","text":"IGNORE","style":"danger"}]}]}
slack_msg = {'text':'\n*Region=AUS* \n Alert from '+d+' *AUS* \n *'+service+'*  is not running\n ######END#####','username': 'markdownbot', 'mrkdwn': 'true'}
def status_service(s1):
   p = subprocess.Popen('systemctl is-active '+service+'', stdout=subprocess.PIPE, shell=True)
   (status1, err) = p.communicate()
   status = status1.rstrip()
   return status

def main():
  # f= open("/root/scripts/test.txt", "a+")
  # print 'This is function'
  # print status_service(service)
  # print 'This is service '+service+''
  # print status_service(service)
  # f.write(status_service(service))
  # f.close()
   if (status_service(service) == checkstatus):
      print "SERVICE",service,"is running"
      #del os.environ['SERVICE1']
   else:
      print "Service",service,"Not Running!!! it needs to be restarted"
      requests.post(web_hook_url,data=json.dumps(slack_msg))
      #del os.environ['SERVICE1']
main()
del os.environ['SERVICE1']
