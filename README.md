# MarchMadness
Running PageRank on men's college basketball teams for the 2014-2015 season

This repository contains game data, python script to create the H matrix for use in the algorithm.

Next, the Octave script runs the power method and ranks the teams in descending order, printing to stdout the top 25 teams

1) python map.py > H.mat

2) octave page.m


Sample Output:
------------
(1) Kentucky 34G 0L

(2) Villanova 34G 2L

(3) Wisconsin 34G 3L

(4) Arizona 34G 3L

(5) Duke 33G 4L


Requirements:
--------------
Python 2.6 or higher

MatLab or Gnu Octave (open-source)


Files:
------------
games_mar15.csv - pipe-delimited data on ~5,800 games (format: team1|score|team2|score)

map.py - Python script writes a file call "teams" in working directory and H matrix to stdout (Usage: python mapy.py > H.mat)

page.m - Octave/MatLab script that reads "teams" and "H.mat", then prints out top 25 teams ranked by PageRank to stdout (Usage: octave page.m)

