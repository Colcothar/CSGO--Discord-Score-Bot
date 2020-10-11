import discord 
from discord.ext import commands
import server
import time
import subprocess

def process_exists(process_name):
    call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
    # use buildin check_output right away
    output = subprocess.check_output(call).decode()
    # check in last line for process name
    last_line = output.strip().split('\r\n')[-1]
    # because Fail message could be translated
    return last_line.lower().startswith(process_name.lower())

global CSserver
CSserver = server.GSIServer(("127.0.0.1", 3000), "S8RL9Z6Y22TYQK45JB4V8PHRJJMD9DS9")
client = commands.Bot(command_prefix=">")


@client.event
async def on_ready():
    print("Bot ready")
    


@client.command()
async def status(ctx):
    if process_exists('csgo.exe'):
        
        CSserver.start_server()
    
        team = str(CSserver.get_info('player.team'))
        ct = str(CSserver.get_info('map.team_ct')['score'])
        t = str(CSserver.get_info('map.team_t')['score'])
        string = str("Player is playing CS (" + team + "side) \nCT Side:"+ ct + "       T Side:"+ t)
        await ctx.send(string)
   
         

    else:
        await ctx.send("Player is not playing CS")


client.run(token)

