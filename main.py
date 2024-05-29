#modules
import os
import discord
import requests
import json
import random
from better_profanity import profanity
from keep_alive import keep_alive
import pronotepy
import datetime

#setting up client
my_secret = os.environ['key']
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#Setting up pn
samsung = os.environ['BRAVIAXR50"ClassX90J4KHDRFull']
apple = os.environ['brawlhalal']
proclient = pronotepy.Client(
  'ENTER YOUR SCHOOL WEBSITE',
  username="ENTER YOUR USERNAME",
  password="ENTER YOUR PASSWORD")
if proclient.logged_in:
  print("PN has launched")

#University randomizer
def get_university():
  response = requests.get(
    "http://universities.hipolabs.com/search?country=France")
  print("status code is", response.status_code)
  json_data = json.loads(response.text)
  quote = json_data[random.randrange(0, 552)]
  quote = quote["name"]
  return (quote)

#activity response
def get_activity():
  response = requests.get("https://www.boredapi.com/api/activity")
  json_data = json.loads(response.text)
  activity = json_data["activity"]
  return (activity)

#Login check
@client.event
async def on_ready():
  print(f"We have logged in as {client.user}")


#Checks if client is messsanger
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  #Uni questions
  if msg.startswith("$What is my future university") or msg.startswith(
      "$What is my future university?") or msg.startswith(
        "$what is my future university") or msg.startswith(
          "$what is my future university?"):
    quote = get_university()
    await message.channel.send(F"You gonna go to {quote} idiot")

#Who are you question
  if msg.startswith("$Who are you?"):
    mylist = [
      "I HATE STUDENTS AHHHHHHHH",
      "Hello I am a pronote bot and I really like pouring oil on children just to set them on fire!",
      "Some guy", "Shut up don't ask questions, give me good reviews!"
    ]
    await message.channel.send(mylist[random.randrange(0, 4)])

#hello message
  if msg.startswith("$hello") or msg.startswith("$Hello"):
    await message.channel.send("Hello I love you! Give me a kiss!")

#profanity checker
  if (profanity.contains_profanity(msg)):
    await message.channel.send("STOP SAYING NONO WORDS")

#homework
  if msg.startswith("$homework") or msg.startswith("$Homework"):
    for i in proclient.homework(datetime.date.today()):
      homework_info = i.description
      homework_class = i.subject.name
      homework_due = i.date
      await message.channel.send(f"homework is due in {homework_class} and is for {homework_due} and for this you must {homework_info}")

#show all the grades 
  if msg.startswith("$showall"):
    periods = proclient.periods
    for period in periods:
      for grade in period.grades:  
        note_moyenne = grade.average
        note_classe = grade.subject.name
        note_top = grade.out_of
        note_date = grade.date
        note_cof = grade.coefficient
        await message.channel.send(f"test of {note_classe} with an average of {note_moyenne} out {note_top} of and with a coefficient of {note_cof} was done on the {note_date}")

#activity
  if msg.startswith("$bored") or msg.startswith("$activity"):
    activity = get_activity() 
    await message.channel.send(activity)
    
#code that runs the secret
keep_alive()
client.run(my_secret)


