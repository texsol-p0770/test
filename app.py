from websocket_server import WebsocketServer
from datetime import datetime
import json
import time

def new_client(client, server):
	hash = {"message": "new_client:[" + client["address"][0] + ":" + str(client["address"][1]) + "]"}
#	server.send_message_to_all(json.dumps(hash))
	print(json.dumps(hash))

def client_left(client, server):
	hash = {"message": "client_left:[" + client["address"][0] + ":" + str(client["address"][1]) + "]"}
#	server.send_message_to_all(json.dumps(hash))
	print(json.dumps(hash))

def message_received(client, server, message):
	hash = {"message": message}
#	server.send_message(client, json.dumps(hash))
	server.send_message_to_all(json.dumps(hash))
	print(json.dumps(hash))

if __name__ == "__main__":
	server = WebsocketServer(1064, host="wsstest-1-2d3g7")
	server.set_fn_new_client(new_client)
	server.set_fn_client_left(client_left)
	server.set_fn_message_received(message_received)
	server.run_forever()
