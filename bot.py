import vk_api

login, password = "Your login", "Your password"
token = "Your token"
vk_session = vk_api.VkApi(login=login, password=password, token=token)
deleted_subs = []


# Готовый код
def get_subs(group_id):
    first = vk_session.method("groups.getMembers", {"group_id": group_id})
    data = first["items"]
    count = first["count"] // 1000
    for i in range(1, count + 1):
        data = data + vk_session.method("groups.getMembers", {"group_id": group_id, "offset": i * 1000})["items"]
    print(data)
    return data


def get_deleted_subs(info):
    temp = []
    for sub in range(len(info)):
        if len(temp) < 999:
            temp.append(info[sub])
        else:
            temp.append(info[sub])
            users = ",".join(str(i) for i in temp)
            data = vk_session.method("users.get", {"user_ids": users})
            for i in range(len(data)):
                try:
                    if data[i]["deactivated"] == "deleted":
                        deleted_subs.append(data[i])
                except KeyError:
                    continue
            temp.clear()
            data.clear()


def delete(group_id, deleted_subs):
    for i in range(len(deleted_subs)):
        vk_session.method("groups.removeUser", {"group_id": "Your group id", "user_id": deleted_subs[i]["id"]})


info = get_subs("Your group id")
get_deleted_subs(info)
print(deleted_subs)
delete("Your group id", deleted_subs)
