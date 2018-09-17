# -*- coding: utf-8 -*-
#Code by Riley Bowling ~ RileyBot is my child and my treasure

#add who'm'st've'th't capabilities
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint, choice
import logging
import pyttsx
import pydub
import subprocess
import urllib, json
import sys
# some bullshit
reload(sys)
sys.setdefaultencoding('utf-8')

updater = Updater(token='185901816:AAGMRidUou4y2Wh0vkCq7zO2B4TG5Zp4pSA')
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
      
def talk(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text=talk_gen(), parse_mode="Markdown")

def yell(bot, update):
  bot.sendMessage(chat_id=update.message.chat_id, text=yell_gen(), parse_mode="Markdown")

def consider(bot, update, args):
  bot.sendMessage(chat_id=update.message.chat_id, text=consider_gen(args), parse_mode="Markdown")
  
def pic(bot, update, args):
  bot.sendPhoto(chat_id=update.message.chat_id, photo=gen_pic(args))
  
def speak(bot, update, args):
  gen_mp3(args,False)
  bot.sendAudio(chat_id=update.message.chat_id, audio=open("/home/ubuntu/RileyBBot/botspeak.mp3", 'rb'))
  
def echo(bot, update, args):
  gen_mp3(args,True)
  bot.sendAudio(chat_id=update.message.chat_id, audio=open("/home/ubuntu/RileyBBot/botspeak.mp3", 'rb'))

def poetry(bot, update, args):
  bot.sendMessage(chat_id=update.message.chat_id, text=poetry_gen(args), parse_mode="Markdown")

def message_reader(bot, update):
  #1/5 chance it adds a message someone types to its memories
  if not randint(0,4):
    new_mem(update.message.text.split())
  
dispatcher.add_handler(CommandHandler('talk', talk))
dispatcher.add_handler(CommandHandler('yell', yell))
dispatcher.add_handler(CommandHandler('consider', consider, pass_args=True))
dispatcher.add_handler(CommandHandler('speak', speak, pass_args=True))
dispatcher.add_handler(CommandHandler('echo', echo, pass_args=True))
dispatcher.add_handler(CommandHandler('pic', pic, pass_args=True))
dispatcher.add_handler(CommandHandler('poetry', poetry, pass_args=True))
dispatcher.add_handler(MessageHandler(Filters.text, message_reader))

adj = ["yes","no","dat","hott","nut","nutt","thicc","thicc","thicc","holy","sweet","dum","big","juicy","fat","smol","wack","lit","round","mega","super","yeety","crazy",
"dope","crispy","stylish", "I hate", "I love","steezy","pointy","loud","nutty","old","young","stupid","sick","cool","weird","strange","giant","slimy","greasy","grimy","fresh",
"tall","short","monster","meaty","sticky","pray for","magic","small","dusty","lost","ancient","long","short","secret","exclusive","tiny","fast","slow","sexy","motherfucking","fucked up","insane",
"crank","deadass","gucci"]

noun = ["dog","frog","cheeto","boy","boy","thot","goblin","rat","meat","milk","bird","worm","hair","child","cat","lizard","protein","brain","soul","banger","yeet",
"yam","ham","fire","anime","melee","peanut","pepper","sword","hands","town","clown","swag","dawg","bitch","hoe","hole","cash","flow","plum","starfruit","cheese","truck",
"forever","love","hate","death","life","darkness","light","science","video games","jail","fight","riot","star","internet","chat","light","juice","college","dumpster","house",
"music","sick","grime","grease","shit","trash","garbage","party","human","robot","gun","mom","dad","snake","idiot","god","son","good","evil","leg","eye","mouth",
"fur","lip","sky","moon","earth","government","agent","fuck","toad","button","lever","head","master","legend","daddy", "lemon", "succ", "demon", "smell","stick","hentai"]

con = ["is","my","go","blease","on my","on","that","that","these","more","some","with","who","out","the","it's","bruh","too","me","probs","and","time to","in","with",
"plus","get","make","form","hundo p", "but with", "but","than", "p","after","before","lmao","fuck","becomes","then","the key to","the perfect","the worst","within","inside",
"next to","should be","is a","would be","from","in the", "from the","a","at","he a","she a","I","to","could","should","had a", "was a","these","that"]

bonus = ["af","yo","bruh","yeet","probs","blease","lol","lmao","fam","boi","hmu","🔥","👌","❤️","🔥👌","🐸☕️","🐸","☕️","ass"]
  
beg = ["b","bl","g","gw","gl","gr","j","pl","pr","p","ch","v","n","s","sl","cl","h","th","f","fr","w","m","shw","shm","y","sh","tr","d","gun","jum","gam","gom","bam","slam","gig",
"big","bog","bill","timb","bib","bun","gib","shim","gunn","gn","bugs","bug",""]
mid = ["o","a","oo","u","e"]
end = ["nis","nus","mu","gus","bus","mb","ly","sby","bo","boo","go","mbo","nna","ck","ck","cc","cc","gum","m","b","g","s","my","ggin","me","dom","me","th","gun","ll","ng","nt","gle",
"gock","ke","le","de","ba","so","zo","mon","bon","rn","chum","wang","dang","nto","ray","day","ndo","nd","zum","ngus","mass","bass","son","bow","rco",""]

#load memory file
with open('/home/ubuntu/RileyBBot/memory.txt', 'r') as f:
    for line in f.readlines():
      noun.append(line[:-1])
  
def gen_mp3(input,echo):
  text = ""
  if echo == True:
    text = ' '.join(input)
  elif not input:
    text = talk_gen(True)
  else:
    text = consider_gen(input,True)

  pitch = randint(20,80)
  
  subprocess.call(["espeak","-ven-uk","-s120","-p" + str(pitch),"-w/home/ubuntu/RileyBBot/botspeak.wav", text])
  pydub.AudioSegment.from_wav("/home/ubuntu/RileyBBot/botspeak.wav").export("/home/ubuntu/RileyBBot/botspeak.mp3", format="mp3")

def gen_pic(search):
  searchterm = " ".join(search);
  if randint (0,1):
    searchterm += " " + choice(adj)
  else:
    searchterm += " " + choice(noun)
  
  url = "https://www.googleapis.com/customsearch/v1?key=AIzaSyDR0B3vuK_DPvaUeGqDC0bofNCFfvQjDiE&cx=016887377983348429422:ufj6ke__3fs&q=" + searchterm + "&searchType=image&start=30&num=1"
  response = urllib.urlopen(url)
  data = json.loads(response.read())
  
  return data['items'][0]['link']
  
def talk_gen(speak=False):
  txt = ""
  
  #1/2 chance adjective is added
  if randint(0,1): 
    txt += choice(adj) + " "
  
  #2/3 chance noun is added 
  if randint(0,2): 
    if not randint(0,2): #1/3 chance it's a made up noun, 2/3 chance it's a normal noun
      txt += choice(beg) + choice(mid) + choice(end) + " "
    else:
      txt += choice(noun) + " "
    if not randint(0,1) and txt[-2] != 's': #1/5 chance noun is made plural
      txt = txt[:-1]
      txt += "s "
  
  #1/6 chance it adds a bonus word
  if not randint(0,5) and (txt != 0):
    txt += choice(bonus) + " "
  
  #1/4 chance punctuation is added
  if not randint(0,3) and (txt != ""): 
    r = randint(1,4)
    txt = txt[:-1]
    if r == 1: #1/4 chance "?" is added
      txt += "?"
    elif r == 2: #1/4 chance "!" is added
      txt += "!"
    else: #2/4 chance "," is added
      txt += ","
    txt += " "
    
  #1/6 chance to bold a word
  if not randint(0,5) and not speak and (txt != ""):
    word = choice(txt.split())
    txt = txt.replace(word, "*" + word + "*",1)
    
  #1/7 chance to italicize a word
  elif not randint(0,6) and not speak and (txt != ""):
    word = choice(txt.split())
    txt = txt.replace(word, "_" + word + "_",1)
    
  #1/3 chance to replace "b" with the emoji version
  if not randint(0,2) and "b" in txt and not speak:
    txt = txt.replace("b", "🅱",1)
  
  #1/3 chance to replace "B" with the emoji version
  if not randint(0,2) and "B" in txt and not speak:
    txt = txt.replace("B", "🅱",1)
  
  #1/3 chance the process repeats unless nothing was added then it must repeat
  if not randint(0,2) or (txt == "") or ((len(txt) > 2) and (txt[-2] == ',')) or ((len(txt) > 3) and (txt[-3] == ',')): 
    if randint(0,4): #4/5 chance a connecting word is added
      txt += choice(con) + " "
    txt += talk_gen(speak)
  return txt

def consider_gen(input,speak=False):
  new_mem(input[:])
  r = randint(0,2)
  input = ' '.join(input)
  
  if not r:
    txt = input + " " + choice(con) + " " + talk_gen(speak)
  elif r == 1:
    txt = talk_gen(speak) + choice(con) + " " + input
  else:
    txt = talk_gen(speak) + input + " " + talk_gen(speak)
  return txt
  
def yell_gen():
  return talk_gen().upper()
 
def new_mem(msg):
  last = ""
  msg = clean_wordlist(msg)
  for w in msg:
    #1/4 chance it adds a the last word and makes a phrase
    if not randint(0,3) and last:
      w = last + " " + w
      noun.append(w)
    else:
      noun.append(w)
    with open('/home/ubuntu/RileyBBot/memory.txt', 'a') as f:
      f.write(w + "\n")
    f.close()
    last = w

def poetry_gen(input=""):
  #things to fix
  #"ed" endings support
  # UNICODE ISSUES
  if not input:
    if not randint(0,2):
      subject = choice(beg) + choice(mid) + choice(end)
    else:
      subject = choice(noun)
    if not randint(0,2):
      subject2 = choice(beg) + choice(mid) + choice(end)
    else:
      subject2 = choice(noun)
  else: 
    clean_wordlist(input)
    if len(input) > 1:
      subject = choice(input)
      input.remove(subject)
      subject2 = choice(input)
    elif input:
      subject = choice(input)
      subject2 = choice(noun)
    else:
      subject = choice(noun)
      subject2 = choice(noun)
  
  poem = ""
  
  syllcounts = [randint(1,8),randint(1,8)]
  
  if randint(0,1):
    syllcounts.append(randint(1,8))
  
  linecount = choice([2,3,4])
  
  r = randint(0,3)
  alt = not randint(0,1)
  for i in range (0,linecount):
    sylls = choice(syllcounts)
    s = subject
    if r and linecount == 4:
      if alt:
        s = subject2
      alt = not alt
    poem += '_' + line_gen(sylls,s)[:-1] + '_\n'
    
  if subject not in poem:
    c = choice(poem.split())
    if c[0] == '_':
      c = c[1:]
    if len(c) > 1 and c[-1] == '_':
      c = c[:-1]
    if len(c) > 3 and c[-3:] == '_\n':
      c = c[:-3]
    poem = poem.replace(c,subject,1)
    
  return poem

def line_gen(sylls, subject):
  rhymes = get_rhymes(subject)
  allits = get_allits(subject)
  t = 0
  l = 0
  while t != sylls and l < 50000:
    t = 0
    line = ""
    l += 1
    if not randint(0,2):
      w = choice(adj)
      line += w + " "
      t += syll_count(w)
    if randint(0,1):
      w = choice(allits)
      line += w + " "
      t += syll_count(w)
      if randint(0,2):
        w = choice(con)
        line += w + " "
        t += syll_count(w)
    if not randint(0,2):
      w = choice(adj)
      line += w + " "
      t += syll_count(w)
    if not randint(0,1):
      w = choice(rhymes)
      line += w + " "
      t += syll_count(w)
      if randint(0,2):
        w = choice(con)
        line += w + " "
        t += syll_count(w)
    if not randint(0,3):
      w = choice(noun)
      if not randint(0,5):
        w += 's'
      line += w + " "
      t += syll_count(w)
      if randint(0,2):
        w = choice(con)
        line += w + " "
        t += syll_count(w)
    if randint(0,2):
      w = choice(rhymes)
      line += w + " "
      t += syll_count(w)
    else:
      line += subject + " "
      t += syll_count(subject)
  return line
  
def syll_count(phrase):
  vows = 'aeiouy'
  c = 0
  vi = -1
  for w in phrase:
    for i in range(0,len(w)):
      if w[i] in vows:
        if (not (i == len(w)-1 and vi >= 0 and w[i] == 'e')) and (not (i == len(w)-2 and w[i+1] == 's' and vi >= 0 and w[i] == 'e')):
          if vi > 0:
            if not w[i-1] in vows:
              vi = i
              c += 1
          else:
            vi = i
            c += 1 
  return c
  
def get_rhymes(word):
  vows = 'aeiouy'
  rhymes = []
  vi = -1
  for i in range(0,len(word)):
    if word[i] in vows:
      #if there's already been a vowel and the last letter is a vowel then don't continue, or if the last letter is s and second to last is a vowel
      if (not (i == len(word)-1 and vi >= 0)) and (not (i == len(word)-2 and (word[i+1] == 's' or word[i+1] == 'd' or word[i+1] == 'r') and vi >= 0)):
        if vi > 0:
          if not word[i-1] in vows:
            vi = i
        else:
          vi = i
          
  end = word[vi:]
  c = 4
  a = ""
  while c > 0:
    a = choice(beg) + end
    if not randint(0,5) and a[-1] != 's':
      a += "s"
    rhymes.append(a)
    c-=1
      
  c = 6
  l = 0
  a = ""  
  while c > 0 and l < 10000:
    a = choice(noun)
    if type(end) == 'unicode':
      a = unicode(a, 'utf-8')
    l+=1
    #horrible
    if len(a) >= len(end) and not (len(a) > len(end) and a[len(a)-1] != 's' and a[-len(end)-1] in vows) and a != word:
      if a[-len(end):].lower() == end.lower() or (len(a) > len(end) and a[-len(end)-1:].lower() == end.lower() + 's'):
        rhymes.append(a)
        c-=1
      
  return rhymes
  
def get_allits(word):
  allits = []
  beg = word[0]
  
  c = 4
  a = ""  
  while c > 0:
    a = beg + choice(mid) + choice(end)
    if not randint(0,5) and a[-1] != 's':
      a += "s"
    allits.append(a)
    c-=1
      
  c = 6
  l = 0
  a = ""  
  while c > 0 and l < 10000:
    l+=1
    a = choice(noun)
    if type(end) == 'unicode':
      a = unicode(a, 'utf-8')
    if len(a) > 0 and a[0].lower() == beg.lower() and a != word:
      allits.append(a)
      c-=1
      
  return allits
  
def clean_wordlist(words):
  stopwords = ['a','i','to','the','im', 'me', 'too', 'hes', 'shes', 'eve', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'when', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'i', 'yours', 'so', 'the', 'having', 'once']
  wordsc = words[:]
  for i, w in enumerate(wordsc):
    prew = ""
    if w[0] == "\"" and w[-1] == "\"":
      prew = w
      wordsc[i] = w[1:-1]
    if w[-1] in ",.?!'":
      if not prew:
        prew = w
      wordsc[i] = w[:-1]
    if w.lower() in stopwords:
      if prew:
        wordsc.remove(prew)
      else:
        wordsc.remove(w)
  return wordsc
  
#blast off
updater.start_polling()
