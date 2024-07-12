# ojadhav-a0

**ASSIGNMENT-1 REPORT**

**PROBLEM I :**

***What the problem is about?:***

The first problem was about how the pichu will traverse through a grid of buildings over empty spaces to reach the goal in minimum number of steps. Our bird, pichu is denoted by the letter "p", the buildings are denoted by the letter "X", the goal is denoted by "@" and the open spaces are denoted by "." . 

***What are we provided with?:***

To give a headstart for solving the problem 2 we were given some functions which would help us in finding the main logic of the code faster.

1. parse_map : used to parse the map in the txt files.
2. valid_index: used to check whether the row and column are in between there terminal ends.
3. moves : Returns the next possible moves for the pichu to move.
4. search : This was an incomplete function. We had to add things in this function so that the code works.

***What did I do?***

1. I went through the code and tested what the provided functions did. 
2. The outputs of the function gave me an idea to implement breadth first search algorithm.
3. Performed the bfs starting from the pichu location till the goal element.

Here's what my algorithm is:

1. Got the pichu location. Created an empty path string and declared a cost variable and set it to 0.
2. Create a map for each direction U, R, D, L.
3. Enqueued the tuple (pichu location, cost, path) in the fringe queue.
4. While the fringe is not null
         i. Dequeue the fringe
        ii. if the pichu location is @ then return the path and the cost.
       iii. else if the the pichu location is visited then continue.
        iv. else mark the pichu location as visited. For every move in the moves, get the difference between the new and the original move for obtaining the direction and then add the direction from the map to the path string and increment the cost by 1.
         v. Enqueue the new location, path and cost in the fringe.

***Problems faced and how I solved it:***

1. Going through the code was difficult at first as I was not expecting a code of this scale for the first assignment. But after spending some time on it I got it. 
2. Getting the direction for the next move and appending the respective letter to path was difficult but after applting the map for the direction it became easy.
3. The code was taking some time to run. I implemented the visited set for that.

Goal State: When pichu location 'p' is at goal location '@'.
Initial State: A position on the map where pichu is placed and a goal position where @ is placed. Also there are Xs and .s.
Successor function: Successor function gives us the next possible moves for the pichu to go.
Cost function: The total steps taken for the pichu to reach its goal.

**PROBLEM II :**

***What the problem is about?:***

The problem is about how we can place k agents 'p' in the grid where the existing 'p' do not see each other and the 'x' act like walls.

***What are we provided with?:***

To give a headstart for solving the problem 1 we were given some functions which would help us in finding the main logic of the code faster.

1. parse_map : used to parse the map in the txt files.
2. count_pichus: returns the number of pichus in the map
3. printable_house_map : prints the final house map with k agents 'p' placed. If the functions returns none then the output is False.
4. add_pichu : Adds the pichu at the current location
5. successors: Returns the possible housemap where the 'p' can be placed.
6. is_goal: check if the placed pichus are equal to k.
7. solve: performs the bruteforce algorithm of placing the elements.

***What did I do?***

1. Added the functions that checked if the position in the map was valid to place or not.
2. Mostly, I added my code in the successors function so that when check is to done, I can add my checking function.

Here's what my algorithm is:

1. Got the pichu locations. Got a list of 2d indices where the agent cannot be placed
2. Passed that list over to the successor function.

***Problems faced and how I solved it:***

1. Getting the indices that need to marked as invalid was difficult. I managed to solve it using 9 different functions. 8 for each direction and 1 to get the list of invalid indices.
2. How to write the code for the logic I built.

Goal State: k agents placed in the house map where each agent cannot see each other.
Initial State: House_map where one location of p is given. Also there are Xs and .s. 'x's act like walls.
Successor function: Successor function gives us the next possible house_map where the agents can be placed.
Cost function: The total number of successors needed to reach the goal state.