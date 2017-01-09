#!C:/Python27/python.exe

import sys, re
import os
import json

print "Starting commit-msg hook"

#Get the commit file
commitMessageFile = open(sys.argv[1]) #The first argument is the file  
commitMessage = commitMessageFile.read().strip()

if "RB=" not in commitMessage:
    print "Reviewboard ID must be linkedin with a commit!"
    sys.exit(1)
else:
    rb_val = re.search(r'\d+', str(commitMessage.split("RB="))).group()
    curl_cmd = 'curl -u admin:admin http://10.244.117.24/api/review-requests/'+str(rb_val)+'/'
    result = os.popen(curl_cmd).read()
    json_data = json.loads(result)
    if 'err' in json_data:
        print json_data["err"]["msg"]
        sys.exit(1)
    else:
        if json_data["review_request"]["approved"]:
            print "Commit message is validated"
            sys.exit(0)
        else:
            print "Your RB should be approved."
            sys.exit(1)