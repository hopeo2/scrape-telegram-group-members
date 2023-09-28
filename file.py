import pandas as pd
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest, JoinChannelRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.functions.messages import GetDialogsRequest, AddChatUserRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import InputPeerChannel
from telethon.tl.types import InputPeerUser

api_id = ************
api_hash = "********************************"

try:
    client = TelegramClient('session', api_id, api_hash)
    client.start()

    target_group = ["campsfreefire", "MahyarBadNews"]
    df = pd.DataFrame()
    for group in target_group:
        u = 1
        client(JoinChannelRequest(group))
        all_participants = client.get_participants(group, aggressive=True)
        for user in all_participants:
            print(user)
            user_id = user.id
            username = user.username
            access_hash = user.access_hash
            data = {"user_id": user_id, "group": group, "username": username, "access_hash": access_hash}
            temp_df = pd.DataFrame(data, index=[1])
            df = df.append(temp_df)
        df.to_excel(r"./members"+str(u)+".xlsx", index=False)
        u += 1

except Exception as e:
    print(e)
