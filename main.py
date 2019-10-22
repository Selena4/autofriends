import vk_api, time,sys, random

login, password = '', ''
ids = 464994063
t = 86400/50 #recommend 

def add(id):
	items = vk.friends.get(user_id=id)["items"]
	print("all_friends: " + str(vk.friends.get(user_id=id)["count"]))
	for usr in items:
		if "deactivated" in vk.users.get(user_id=usr)[0].keys():
			print("[error] [" + str(usr) + "] the user is blocked")
		elif vk.users.get(user_id=usr)[0]["is_closed"] == True:
			print("[error] [" + str(usr) + "] the user's profile is closed")
		elif vk.friends.get(user_id=usr)["count"] < vk.users.getFollowers(user_id=usr)["count"] *2:
			print("[error] [" + str(usr) + "] the number of friends does not meet the requirements")
		elif usr in my:
			print("[info] [" + str(usr) + "] the user is friend already")
		elif vk.friends.areFriends(user_ids=usr)[0]["friend_status"] == 1:
			print("[info] [" + str(usr) + "] the user has already been added as a friend")
		else:
			try:
				vk.friends.add(user_id=usr)
				print("[request] [" + str(usr) + "] friend added successfully")
			except:
				print("[error] captcha")
			print("waiting "+str(t)+"s...")
			time.sleep(t)
def main():
	global ids, vk,my
	vk_session = vk_api.VkApi(login, password)
	vk_session.auth()
	vk = vk_session.get_api()
	my = vk.friends.get()["items"] 
	while True:
		add(ids)
		while True:
			id = random.choice(vk.friends.get(user_id=ids)["items"])
			if "deactivated" in vk.users.get(user_id=id)[0].keys():
				continue
			elif vk.users.get(user_id=id)[0]["is_closed"] == True:
				continue
			elif  vk.friends.get(user_id=id)["count"]  < 10:
				continue
			else:
				ids = id
				print("[info] target switched to id" + str(ids))
				break
	
	
if __name__ == "__main__":
	main()
