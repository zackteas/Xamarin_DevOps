"""
Program to filter through and grab data from IMDb and Wikipedia.
"""
from httplib import *
from urllib2 import *

def getMovieList():
  
  
def getActorList(str movie):
  
  
def getActorAge(list actors):
  
  
def calcAvgAge(list actorAges):
  age = 0.0
  for i in range(len(actors)):
    age+=actors[i]
  age=float(age)/len(actors)
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
    
main()
