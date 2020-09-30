import requests
import json

def git(id):
	if not isinstance(id,str):
		return "Id not a String"
	
	link ="https://api.github.com/users/" + id + "/repos"
	req = requests.get(link)
	data = req.json()
	if not isinstance(data,list):
		#print( "USER DNE")
		return "User DNE"
		
	list1 =[]
	list2 =[]
	ans = []
	for i in range(len(data)):
		list1.append(data[i]["name"])
		
	for i in range(len(list1)):	
		link2 ="https://api.github.com/repos/" + id +"/"+ list1[i] + "/commits"
		req2 = requests.get(link2)
		data2 = req2.json()
		list2.append(len(data2))
		
		
	for i in range(len(list1)):
		ans.append("Repo "+ list1[i] +" Number of commits " +str(list2[i]))

	
	return ans
	
