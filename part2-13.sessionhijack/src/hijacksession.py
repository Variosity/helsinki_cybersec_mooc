import sys
import requests
import json


def test_session(address):
	url = f"{address}/balance/"
	for i in range(1, 12):
		session_id = f"session-{i}"
		response = requests.get(url, cookies={'sessionid': session_id}, allow_redirects=False)
		if response.status_code == 200:
			data = json.loads(response.text)
			if data['username'] != 'anonymous':
				return data['balance']
	return



def main(argv):
	address = sys.argv[1]
	print(test_session(address))


# This makes sure the main function is not called immediatedly
# when TMC imports this module
if __name__ == "__main__": 
	if len(sys.argv) != 2:
		print('usage: python %s address' % sys.argv[0])
	else:
		main(sys.argv)
