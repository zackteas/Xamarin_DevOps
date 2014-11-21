"""
Program to filter through and grab data from IMDb and Wikipedia.
"""
import httplib
import urllib2
import json

def getMovieList():
  movies = []
  url = "http://www.imdb.com/showtimes/location?ref_=inth_ov_sh_sm"
  req = urllib2.Request(url)
  handle = urllib2.urlopen(req)
  content = handle.read()
  split_page = content.split("<div class=\"lister-list\">", 1)
  split_page = split_page[1].split("<div class=\"hidden lister-working\">", 1)
  
  
  
def getActorList(str movie):
  actor_list = []
  count = 0
  baseurl = "http://en.wikipedia.org/wiki/"
  url = baseurl+movie+"_(film)"
  req = urllib2.Request(url)
  handle = urllib2.urlopen(req)
  content = handle.read()
  actor_section = content.split("<b>Astronaut crew</b>", 1)
  actor_section = actor_section[1].split("<h2>", 1)
  actor_section = actor_section[0].split"<li>")
  for i in range(len(actor_section)):
    actor_section[i] = actor_section[i].split("<a href=\"/wiki/", 1)
  for i in range(len(actor_section)):
    if (len(actor_section[i])>1):
      actor_section[i] = actor_section[i][1].split("\"",1)
    if (actor_section[i][0]=='<'):
      count++
  for i in range(count):
    for j in range(len(actor_section)):
      if (actor_section[i][0]!='<'):
        actor_list.append(actor_section[i])
      break
  
def getActorAge(list actors):
  actorAges = []
  for i in len(actors):
    baseurl = "http://en.wikipedia.org/wiki/"
    url = baseurl+actors[i]
    req = urllib2.Request(url)
    handle = urllib2.urlopen(req)
    content = handle.read()
    age_section = content.split("<span class=\"noprint ForceAgeToShow\">(age&nbsp;",1)
    age_section = age_section[1].split(")</span>",1)
    actorAges.append(int(age_section))
  return actorAges
  
def calcAvgAge(list actorAges):
  age = 0.0
  for i in range(len(actorAges)):
    age+=actors[i]
  age=float(age)/len(actorAges)
  return age
  
def main():
  movies = getMovieList()
  print("The movies currently playing in US theaters are: \n=======================================\n")
  for i in range(len(movies)):
    actors = []
    actorsAge = 0
    actors = getActorList(movies[i])
    actorAges = getActorAge(actors)
    avgAge = calcAvgAge(actorAges)
    print(str(i)+" "+movies[i]+".")
    print("Average actor age for "+movies[i]+" is "+str(avgAge)".")
    
if __name__ == '__main__':
  main()
