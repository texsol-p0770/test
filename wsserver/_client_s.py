from websocket import create_connection
import time
import sys

if __name__ == "__main__":
	server = create_connection("ws://pt-wrap-node15-vmg.wni.co.jp:1064")
	server.send(sys.argv[1])
#	message = server.recv()
#	print(message)
#	time.sleep(10)
	server.close()
