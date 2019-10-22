import vk_api, time,sys

login, password = '', ''
ids = 546262046
t = round(86400/39)
vk_session = vk_api.VkApi(login, password)
vk_session.auth()
vk = vk_session.get_api()
my = vk.friends.get()["items"] 
def add(id):
	items = vk.friends.get(user_id=id)["items"]
	
	for usr in items:
		if "deactivated" in vk.users.get(user_id=usr)[0].keys():
			print("[error] [" + str(usr) + "] the user is blocked")
		elif vk.users.get(user_id=usr)[0]["is_closed"] == True:
			print("[error] [" + str(usr) + "] the user's profile is closed")
		elif vk.friends.get(user_id=usr)["count"] < vk.users.getFollowers(user_id=usr)["count"] *4:
			print("[error] [" + str(usr) + "] the number of friends does not meet the requirements")
		elif usr in my:
			print("[info] [" + str(usr) + "] the user is friend already")
		elif vk.friends.areFriends(user_ids=usr)[0]["friend_status"] == 1:
			print("[info] [" + str(usr) + "] the user has already been added as a friend")
		else:
			vk.friends.add(user_id=usr)
			print("[request] [" + str(usr) + "] friend added successfully")
			for i in range(t):
				sys.stdout.write("waiting " +str(t-i) +"s...")
				sys.stdout.flush()
				sys.stdout.write("\b")
				time.sleep(1)
	
add(ids)
