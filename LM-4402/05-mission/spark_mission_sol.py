import json
import sys
import requests

#MISSION: FILL IN THE REQUESTED DETAILS
ACCESS_TOKEN 	= "YOUR-SPARK-TOKEN-HERE" #Replace None with your access token. Shroud with quotes.
ROOM_NAME		= "Mission 2 Example Room Name" #Replace None with the name of the room to be created. Shroud with quotes.
YOUR_MESSAGE 	= "This is a message for Mission 2" #Replace None with the message that you will post to the room. Shroud with quotes.


#sets the header to be used for authentication and data format to be sent.
def setHeaders():         
	accessToken_hdr = 'Bearer ' + ACCESS_TOKEN
	spark_header = {'Authorization': accessToken_hdr, 'Content-Type': 'application/json; charset=utf-8'}
	return (spark_header)


#check if spark room already exists.  If so return the room id
def findRoom(the_header,room_name):
	roomId=None
	uri = 'https://api.ciscospark.com/v1/rooms'
	resp = requests.get(uri, headers=the_header)
	resp = resp.json()
	for room in resp["items"]:
		if room["title"] == room_name:
			print()
			print("findRoom JSON: ", room)	
			#print("MISSION: findRoom: REPLACE None WITH CODE THAT PARSES JSON TO ASSIGN ROOM ID VALUE TO VARIABLE roomId")
			#Required API https://developer.ciscospark.com/endpoint-rooms-get.html
			#Code Start->
			roomId=room["id"]
			#<-Code End
			break	
	return(roomId)
	
# checks if room already exists and if true returns that room ID. If not creates a new room and returns the room id.
def createRoom(the_header,room_name):
	roomId=findRoom(the_header,room_name)
	if roomId==None:
		roomInfo = {"title":room_name}
		uri = 'https://api.ciscospark.com/v1/rooms'
		resp = requests.post(uri, json=roomInfo, headers=the_header)
		var = resp.json()		
		print()
		print("createRoom JSON: ", var)	
		#print("MISSION: createRoom: REPLACE None WITH CODE THAT PARSES JSON TO ASSIGN ROOM ID VALUE TO VARIABLE roomId.")		
		#Required API https://developer.ciscospark.com/endpoint-rooms-post.html
		#Code Start->
		roomId=var["id"]
		#<-Code End
		
	return(roomId)
	
# adds a new member to the room.  Member e-mail is test@test.com
def addMembers(the_header,roomId):
	member = {"roomId":roomId,"personEmail": "test@test.com", "isModerator": False}
	uri = 'https://api.ciscospark.com/v1/memberships'
	resp = requests.post(uri, json=member, headers=the_header)
	print()
	print("addMembers JSON: ", resp.json())

#posts a message to the room
def postMsg(the_header,roomId,message):
	message = {"roomId":roomId,"text":message}
	uri = 'https://api.ciscospark.com/v1/messages'
	resp = requests.post(uri, json=message, headers=the_header)
	print()
	print("postMsg JSON: ", resp.json())

#MISSION: WRITE CODE TO RETRIEVE AND DISPLAY DETAILS ABOUT THE ROOM.
def getRoomInfo(the_header,roomId):
	print("In function getRoomInfo")
	#MISSION: Replace None in the uri variable with the Spark REST API call	
	#Required API https://developer.ciscospark.com/endpoint-rooms-roomId-get.html
	#Code Start->
	uri = "https://api.ciscospark.com/v1/rooms/"+roomId
	#<-Code End
	if uri == None:
		sys.exit("Please add the uri call to get room details.  See the Spark API Ref Guide")
	resp = requests.get(uri, headers=the_header)
	print("Room Info: ",resp.text)
	resp = resp.json()
	#print("MISSION: Add code to parse and display details about the room.")
	#Adding details
	#https://developer.ciscospark.com/endpoint-rooms-roomId-get.html
	#This is just example code. Mission target is to access the response data and print it to the console
	#Code start->
	print("\nRoom details:")
	print("The room id is "+resp["id"])
	print("The title is "+resp["title"])
	print("Last activity was "+resp["lastActivity"])
	print("The room was created in "+resp["created"])
	#<-Code end
	

if __name__ == '__main__':
	if ACCESS_TOKEN==None or ROOM_NAME==None or YOUR_MESSAGE==None:
		sys.exit("Please check that variables ACCESS_TOKEN, ROOM_NAME and YOUR_MESSAGE have values assigned.")
	header=setHeaders()
	#passing the ROOM_NAME for the room to be created
	room_id=createRoom(header,ROOM_NAME) 
	if room_id == None:
		sys.exit("Please check that functions findRoom and createRoom return the room ID value.")
	#passing roomId to members function here to add member to the room.
	addMembers(header,room_id)   
	#passing roomId to message function here to Post Message to a room.
	postMsg(header,room_id,YOUR_MESSAGE)
	print()
	#print("MISSION: ADD FUNCTION CALL getRoomInfo(header,room_id)")	
	#Calling the getRoomInfo function
	#Code Start->
	getRoomInfo(header, room_id)
	#<-Code End