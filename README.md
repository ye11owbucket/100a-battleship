## SDSS Computing Studies Python Assignment
### Assignment #100a Battelship

#### Introduction
This assignment takes components that could be used to create the classic boardgame "Battleship". This is the game where you place your ships on a 10x10 grid, and then take turns attacking square in the grid, hoping to hit your opponents ships.  
Although it uses an x,y coordinate system, the coordinates are often read as Letters for columns and numbers for rows.  For example "A1" would correspond to the coordinate (0,0) and "A5" would correspond to the coordinate (0,4).  What would B3 correspond to? (1,2) of course!

Assignments:
##### 1. Display the map
Given a list of coordinates that shows the occupied squares on the map, draw a representation of what the map looks like.
##### 2. Convert coordinates
Given a string literal convert it to a list that contains the coordinate. Your string literal should be able to remove whitespace and work with both lower and upper case values.  "B3", "b3" , "B 3" and "b 3" should all correspond to the list item [1,2]
##### 3. Generate data for each boat.
There are 5 boats in battleship.  They must occupy coordinates that are horizontal or vertical only (no diagonals).  The size of the boats are 2, 3, 3, 4 and 5.  Create a function that generates a list of the data for your boats.

