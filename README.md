Xamarin_DevOps
==============
Current Movies and Avg. Age of Actors design:
  In order to grab the data from IMDb and Wikipedia, four functions as well as a main function were required, 
  where one function grabbed the list of movies from IMDb, another got a list of the actors in a given movie, the third 
  got a list of all the ages of the actors in the movie, and the final found the average age of all the actors in that 
  specific movie.  The main function tied all of the others together and first found the list of all the movies and then 
  iterated through the list and called the other three functions.  The function to get the movie list never ended up being
  finished due to the fact that IMDb and other similar sites store a large amount of data in relation to each movie and 
  parsing only the title proved to be a difficult task.  I would like to approach finding that data in a similar fashion as
  I approached getting the information in the other functions. The function to get the list of actors however, was a bit easier
  due to the fact that Wikipedia stores their information in fairly simple formats, allowing for easy access and filtering.
  This was done by loading the page of the movie passed to the getActorList function and getting the content of the page
  into an array.  Then, the array was split based on the sections of HTML desired, which were found by inspecting the 
  elements on the webpage.  After this, the resulting text was filtered to find only the actor names and the function 
  returned that list of actor names.  The next function performed in a very similar way, except, it iterates over all 
  of the actors and pulls up their individual Wikipedia pages and grabs their ages.  Then that list of ages gets passed 
  to the average age function which performs a simple addition of all the ages of the actors gathered from the previous
  function and then divides that sum by the number of actors in the movie.  I will definitely continue working on this
  however so I can really understand it and keep learning about web scraping!!
  
Running:
  Download the repository into your desired destination, then navigate to that directory in command line using a sequence of
  cd calls, for instance, if the folder is in your desktop the commands you would run would be:
  $ cd Desktop
  $ cd Xamarin_DevOps_master
  $ python data_grabber.py
  This will call the data_grapper.py program.
