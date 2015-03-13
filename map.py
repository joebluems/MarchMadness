#!/usr/bin/python
import csv
import re
import os

count=0
teams={}
map={}
winSparse={}
losses={}
games={}

with open('./games_mar11.csv','rb') as csv_file:
    csv_reader = csv.reader(csv_file,delimiter='|')
    for row in csv_reader:
       ### remove rankings, create map of teams/integer ###

	     if int(row[1])>int(row[3]): 
	       win=row[0]
	       lose=row[2]
	     else:
	       win=row[2]
	       lose=row[0]
	   
      if win not in teams:
	       teams[win]=count
	       map[count]=win
	       losses[count]=0
	       games[count]=0
	       count+=1
      if lose not in teams:
	       teams[lose]=count
	       map[count]=lose
      	 losses[count]=0
      	 games[count]=0
      	 count+=1
   
      value = 1
	    #### keep track of total games & losses for each team ###
      games[teams[lose]]+=1 
      games[teams[win]]+=1 
      losses[teams[lose]]+=value 
      ### create sparse matrix for each loser - increment number of wins ###
      if teams[lose] not in winSparse: 
	       winSparse[teams[lose]]={} 
      if teams[win] not in winSparse[teams[lose]]: winSparse[teams[lose]][teams[win]]=0
      winSparse[teams[lose]][teams[win]]+=value

##### print team mapping to file #####
f = "teams"
try:
  os.remove(f)
except OSError:
  pass
for i in range(0,len(teams)):
   with open(f,'a') as file:
      file.write("%s|%s|%s|%s\n" % (i,map[i],losses[i],games[i]))


##### print out H matrix #####
for i in range(0,len(teams)):
  for j in range(0,len(teams)):
     if i not in winSparse: winSparse[i]={}
     if j in winSparse[i]: print "%f" % (float(winSparse[i][j])/max(25,losses[i])),
     else: print 0,
  print
