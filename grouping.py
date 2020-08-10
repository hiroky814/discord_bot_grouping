import discord
import random
import os

token = os.environ["DISCORD_BOT_TOKEN"]

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if message.content.startswith('test'):
            try:
                number_of_teams = int(message.content.split(" ")[1])
            except:
                await message.channel.send("invalid error. \"team [number of teams]\"")
                return
            
            # チームリスト作成
            teams = []
            for index in range(number_of_teams):
                array = []
                teams.append(array)

            # チャンネルのメンバー取得
            members = []
            for member in message.channel.members:
                # オフラインのメンバー以外を対象にする
                if str(member.status) != "offline":
                    members.append(member)

            # メンバーをシャッフル
            random.shuffle(members)
            
            # メンバーをチームリストに追加
            team_counter = 0
            for member in members:
                # 自分自身の時は処理しない
                if member == self.user:
                    continue

                # 名前を取得
                name = str(member).split("#")[0]

                # チームリストに追加
                teams[team_counter].append(name)
                team_counter = team_counter + 1

                # チーム数までカウントアップしたらリセットする
                if team_counter == number_of_teams:
                    team_counter = 0

            # メッセージ作成
            send_message = ""
            team_counter = 1
            for team in teams:
                send_message = send_message + "チーム " + str(team_counter) + ":\n"
                for member in team:
                    send_message = send_message + member + " "
                send_message = send_message + "\n\n"
                team_counter = team_counter + 1 

            await message.channel.send(send_message)
            return

client = MyClient()
client.run(token)