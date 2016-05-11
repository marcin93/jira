import json
import getpass
import requests as req

# jira instance url
jira = raw_input('jira url is: ')

# user credentials
user = raw_input('Username: ')
passwd = getpass.getpass()

# connection test
try:
	r = req.get(jira)
except Exception:
	print ('Server '+jira+' is unreachable')

# get groups list
try:
	groups = req.get(jira+'/rest/api/2/groups/picker', auth=(user,passwd))
	parsed_groups = json.dumps(groups.json(), indent=4)
	decoded_groups = json.loads(parsed_groups)
	group_counter = 0
	print ('\nGroup list:')
	for i in decoded_groups['groups']:
		print (i['name'])
		group_counter = group_counter +1
	print 'We have:',group_counter,'groups'
	print ('\n')
except Exception:
	print ('Group grep failed')

group = raw_input('Group: ')

# get users from choosed grup
try:
	users = req.get(jira+'/rest/api/2/group?groupname='+group+'&expand=users[0:99]', auth=(user,passwd))
except Exception:
	print ('Api request is failed')

try:
	j = json.dumps(users.json(), indent=4)
	decoded = json.loads(j)
	user_counter = 0
	print ('\nUser list:')
	for x in decoded['users']['items']:
		print ('email: '+x['emailAddress']+', Username: '+x['name'])
		user_counter = user_counter + 1
	print 'We have:',user_counter,'users'
	print ('\n')
except Exception:
	print ('Parsing error')
