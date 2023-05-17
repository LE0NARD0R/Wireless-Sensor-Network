import subprocess
import json
import pathlib
import re
import time

class Error(Exception):
	pass

class FetchError(Error):
	def __init__(self, expression, message):
		self.expression = expression
		self.message = message

def sensor_pull_storage():
	args = [ "curl" ]
	args += [
		"-G", f"https://au1.cloud.thethings.network/api/v3/as/applications/wsn-corrosion-endpoints/packages/storage/uplink_message",
		"--header", f"Authorization: Bearer NNSXS.YW667JCZK4KIBPXOTJTJV5NU7WWKDRG5CDN53NY.GAWRQU4JHE6D3BZN6IO4ZIXJTPGME5QDX632CS47T4LHVULFL3WQ",
		"--header", "Accept: text/event-stream",
		"-d", f"last=20s",
		"-d", "field_mask=up.uplink_message.decoded_payload",
	]
	result = subprocess.run( 
		args, shell=False, check=True, capture_output=True
		)
	sresult = result.stdout
	return list(map(json.loads, re.sub(r'\n+', '\n', sresult.decode()).splitlines()))
	
	
def constant():
	while(True):
		try:
			fuera = sensor_pull_storage()
			fuere = fuera[0]['result']['uplink_message']
		except:
			print('no hay 0')
		try:			
			print(fuere['decoded_payload'])
		except:
			print('no hay uplink')
		
		
		time.sleep(5)

