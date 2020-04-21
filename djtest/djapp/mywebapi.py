import xmltodict
import pymongo
import json
import requests

def my_webapi(search):
	myclient = pymongo.MongoClient("mongodb://localhost:27017/")
	mydb = myclient["testdb"]
	mycol = mydb["collect2"]
	URL = f"https://www.als.ogcio.gov.hk/lookup?q=<{search}>"
	#print(URL)
	response = requests.get(URL)
	xml_data=response.content
	my_dict=xmltodict.parse(xml_data)
	json_data=json.dumps(my_dict)
	myjson=json.loads(json_data)
	mycol.insert_one(myjson)


my_webapi("香港機場")
my_webapi("abc")

