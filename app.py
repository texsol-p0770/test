from websocket_server import WebsocketServer
from datetime import datetime
import json
import logging
import time
import traceback

def new_client(client, server):
#	hash = {"message": "new_client:[" + client["address"][0] + ":" + str(client["address"][1]) + "]"}
#	server.send_message_to_all(json.dumps(hash))
#	print(json.dumps(hash))
	print("@@@ new_client @@@")

def client_left(client, server):
#	hash = {"message": "client_left:[" + client["address"][0] + ":" + str(client["address"][1]) + "]"}
#	server.send_message_to_all(json.dumps(hash))
#	print(json.dumps(hash))
	print("@@@ client_left @@@")

def message_received(client, server, message):
#	hash = {"message": message}
#	server.send_message(client, json.dumps(hash))
#	server.send_message_to_all(json.dumps(hash))
#	print(json.dumps(hash))
	print("@@@ message_received @@@")

if __name__ == "__main__":
	try:
		server = WebsocketServer(8080, host="0.0.0.0", loglevel=logging.INFO)
		server.set_fn_new_client(new_client)
		server.set_fn_client_left(client_left)
		server.set_fn_message_received(message_received)
		server.run_forever()
	except:
		traceback.print_exc()
