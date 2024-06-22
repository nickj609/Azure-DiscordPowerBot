import os
import discord
from discord.ext import commands
from azure.identity import ClientSecretCredential
from azure.mgmt.compute import ComputeManagementClient

# Bot credentials
TOKEN = os.environ.get('TOKEN')  
ADMIN_ROLE_ID = int(os.environ.get('ADMIN_ROLE_ID'))  # Convert to integer

# Azure credentials
TENANT_ID = os.environ.get('TENANT_ID')
CLIENT_ID = os.environ.get('CLIENT_ID')
CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
SUBSCRIPTION_ID = os.environ.get('SUBSCRIPTION_ID')
RESOURCE_GROUP = os.environ.get('RESOURCE_GROUP')
VM_NAME = os.environ.get('VM_NAME')

intents = discord.Intents.all()
intents.messages = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def startvm(ctx):
    if is_admin(ctx.author):
        credential = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
        compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)
        compute_client.virtual_machines.begin_start(RESOURCE_GROUP, VM_NAME)
        await ctx.send(f'Starting VM {VM_NAME}...')
        await ctx.send('Server started successfully!')
    else:
        await ctx.send('You do not have permission to use this command.')

@bot.command()
async def stopvm(ctx):
    if is_admin(ctx.author):
        credential = ClientSecretCredential(TENANT_ID, CLIENT_ID, CLIENT_SECRET)
        compute_client = ComputeManagementClient(credential, SUBSCRIPTION_ID)
        compute_client.virtual_machines.begin_deallocate(RESOURCE_GROUP, VM_NAME)
        await ctx.send(f'Stopping VM {VM_NAME}...')
        await ctx.send('Server stopped successfully!')
    else:
        await ctx.send('You do not have permission to use this command.')

def is_admin(user):
    for role in user.roles:
        print(f"{role.name} (ID: {role.id})")
        if role.id == ADMIN_ROLE_ID:
            return True
    return False

bot.run(TOKEN)
