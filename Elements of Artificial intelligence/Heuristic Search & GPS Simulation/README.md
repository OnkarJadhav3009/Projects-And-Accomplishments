# Elements of AI

## Assignment 1

-----------------
### TEAM MEMBERS:
-----------------

**Onkar Jadhav - ojadhav** <br>
**Sai Teja Burla - saburla** <br>
**Maitreya Kanitkar - mkanitka** <br>

-------------------------------------------
### Problem - 1 (Birds, Heuristics and A*):
-------------------------------------------

**Problem Description** <br>
We are given N number of birds sitting randomly on a power line that are labelled with numbers from 1 to N. We need to find out the least possible moves needed to make the N birds sit in a sorted manner from 1 to N. The successors are obtained by swapping only one bird at a time with it's either neighbour and that would be considered as one movement. We are going to consider <u> N = 5 </u> for this report.

**Problem With The Given Solution** <br>
The provided solution had a basic BFS implementation. BFS is not an efficient way to solve a problem which has a very large state space.<br>
Using the given code, the algorithm takes too long to give the solution. Therefore we needed a faster solution for this problem. This was achieved using A*.

**State Space** <br>
S = {12345, 12354, 12453, ...} <br>
The state space for this problem would be all the different possible combinations of the number 12345.<br>
We can calculate the number of possible states using N! which is 5! = 120.

**Successor Function** <br>
The successor function for this problem returns a list of states, in which, each state is obtained by swapping two adjacent birds from the current state. <br>
For example: If we have the current state as 23154, the possible successors for this would be: 32154,21354,23514,23145 etc. <br>

**Edge Weights** <br>
The edge weight for any movement in this problem is 1.

**Goal State** - {[1,2,3,4,5]} <br>
The goal state for this problem is the sorted numbers on the birds which is 1,2,3....,N and for the example we considered above it will be '[1,2,3,4,5]'.

**Initial State** <br>
The initial state for this problem would be the input given by the user.<br>
This input should belong to the State Space Set.

**Heuristic Function** <br>
h(s) -> number of misplaced tiles <br>
Our heuristic function for this problem calculates the number of misplaced birds for the successor states. <br>
A heuristic is admissible if it never overestimates the true cost to a nearest goal<br>
Proof: <br>

    Conisder current state as [2,3,4,5,1]

    for the above state heuristic value is 5 as all 5 tiles are misplaced. Our goal state will have a heuristic of 0. <br>
    We can observe that the heuristic will only underestimate the the cost to it's goal state, i.e, the heuristic for a particular state will never be less than 0. 

**Cost Function** - f(x) = g(x) + h(x) <br>
Here, <br>
g(x) - This is the cost from initial state to the current state 's'. <br>
h(x) - This is the heuristic cost calculated for the current state 's'.

**Working of Our Algorithm** <br>
We are implementing a simple A* algorithm by using a priority queue. The priority queue is utilised for getting a state that would help the algorithm reach the goal in least number of moves. The total cost fn is enqueued into the fringe. We get the state with the minimum value of fn. <br>
Algotithm: <br>
While fringe is not empty: <br>
We put the initial state in the fringe, which is our priority queue. <br>
We pop the fringe using PriorityQueue's get(), so that we get the state with minimum fn. <br>
If the state is goal state we return the path. Else get the successors. <br>
We take all successor states, get their heuristics and add it the fn value. Also we add the path from initial node till now.

**Addtional Note** <br>
The problem statement and test cases were pointing to the case where the number of birds N = 5. We intitially developed a code for this case only but then thought of generalising it so that it works for any number of birds N.

----------------------------------
### Problem - 2 (The 2022 Puzzle):
----------------------------------

**Problem Description** <br>
In the 2022 Puzzle we have '5 * 5' board which is filled with numbers from 1-25. The problem statement here is that we will be given one such board but the numbers on it will be jumbled and there are a given set of operations we can perform on the board to reach the sorted goal state. So we need to find the least number of movements to reach the goal state. 

**State Space** <br>
The state space for this problem is all the permutations of the board with the following moves: <br>
Sliding Rows: Slide any of the 5 rows either left or right by one. The move can be written as R or L followed by row number. <br>
Sliding Column: Slide any of the 5 columns either up or down by one. The move can be written as U or D followed by column number. <br>
Outer Rotation: Take the outer circle of the board and rotate it either clockwise or counter clockwise by one. The move can be written as O followed by c for clockwise and cc for counter clockwise. <br>
Inner Rotation: Take the inner circle of the board and rotate it either clockwise or counter clockwise by one. The move can be written as I followed by c for clockwise and cc for counter clockwise. 

**Successor Function** <br>
The successor function for this problem would calculate all of the above mentioned moves for a given state. <br>
For example: If we have a state of the board then we calculate: {L1, L2, L3, L4, L5, R1, R2, R3, R4, R5, U1, U2, U3, U4, U5, D1, D2, D3, D4, D5, Oc, Occ, Ic, Icc} for that state. <br>
So for each state there will be 24 successors in total. <br>
So the successor function calculates all such states which we then send to the heuristic to select the best next state.

**Edge Weights** <br>
The edge weight for any movement in this problem would be 1.

**Goal State** - {[[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]} <br>
The goal state for this problem would be the sorted board. Which is shown as follows: <br>
1  2  3  4  5 <br>
6  7  8  9  10 <br>
11  12  13  14  15 <br>
16  17  18  19  20 <br>
21  22  23  24  25 

**Initial State** <br>
The initial state for this problem would be the input board given by the user.

**Heuristic Function** <br>
For the heuristic function we made use of the manhattan distance. So we took the state given as input to the heuristic function and got the manhattan distance of that state with respect to the goal state. This means that we take each element of the current state and compare and get the manhattan distance with respect to the goal state of the same element and then take the sum of all the manhattan distances we get and return that value. To make this heuristic efficient and to reach the goal in optimal number of moves, we did the following: <br>
For a state where we did a row or column movement: We divided the returned manhattan distance value by 5 since 5 tiles are moved to do a row or column movement. <br>
For a state where we did outer circle movements: We divided the returned manhattan distance value by 16 since 16 tiles are moved to do a clockwise or counter clockwise movement. <br>
For a state where we did inner circle movements: We divided the returned manhattan distance value by 8 since 8 tiles are moved to do a clockwise or counter clockwise movement. <br>
Generally, this can be reduced as SUM OF MANHATTAN DISTANCES/NUMBER OF ELEMENTS MISPLACED IN THAT MOVE

Since the value of h will never be overestimated as we are restricting the constraints to be the indices of the elenments, the calculated heuristic will never reach -1, which is an overestimation.

**Cost Function** - f(x) = g(x) + h(x) <br>
Here, <br>
g(x) - This is the cost from initial state to a certain state 's'. <br>
h(x) - This is the cost calculated from the heuristic function which is the sum of manhattan distances for each element.

**Working of Our Algorithm** <br>
The logic and structure is similar to that of Problem 1. In this problem we have many number of successors and hence just implementing a basic heuristic won't work.
So after implementing our heuristic we reduced the time and number of moves required to reach the goal state.


**Different Heuristic Functions** <br>
For this problem heuristic function was the most trickiest part to implement. We ended up implementing the following heuristics in search of the perfect one for this problem: <br>
1. Euclidean Distance
2. Manhattan Distance
3. Number of Misplaced Tiles
4. Penalty Heuristic
5. Cosine Distance <br>
Additional to this we tried out different combinations of all of these before we got to the heuristic function that did end up working.

**Questions** <br>

1. In this problem, what is the branching factor of the search tree?

The branching factor of any search tree is the number of children at a particular node of the tree. So in this problem the <u> branching factor would be 24 </u> since each state can be branched out to 24 different state as there are 24 different moves that could be made. This is at level 1 which is below the root. At level 2 of the tree the branching factor would be 24 to the power 2 and level 3 it would be 24 to the power 3 and at level n it would be 24 to the power n.

2. If the solution can be reached in 7 moves, about how many states would we need to explore before we found it if we used BFS instead of A* search? A rough answer is fine.

The BFS algorithm checks every single successor state before it decides which state to select and go ahead with. So if the solution for a certain board could be reached in 7 moves then a BFS algorithm would take: <br>
Level 0: 24 to the power 0 = 1 <br>
Level 1: 24 to the power 1 = 24 <br>
Level 2: 24 to the power 2 = 576 <br>
Level 3: 24 to the power 3 = 13824 <br>
Level 4: 24 to the power 4 = 331776 <br>
Level 5: 24 to the power 5 = 7962624 <br>
Level 6: 24 to the power 6 = 191102976 <br>
Level 7: 24 to the power 7 = 4586471000 <br>
Therefore, if we implement a BFS algorithm for this problem then in the worst case we have to go through approximately 4700000000 states before we find a solution.

-----------------------------
### Problem - 3 (Road Trip!):
-----------------------------

**Problem Description** <br>
Given a start city, an end city and a cost function we need to find the best route from that start city to the end city.

**State Space** <br>
All the places/cities that are present in the dataset will be a part of our state space as these would be the nodes in our graph.

**Successor Function** <br>
The successor function here will find all the neighbouring cities keeping in mind the cost function given as an input from the user.

**Edge Weights** <br>
The edge weight for this problem is the distance between two nodes which are cities in this problem.

**Goal State** <br>
The goal state in this problem would be the end city that the user entered.

**Initial State** <br>
The initial state in this problem would be the start city that the user entered.

**Heuristic Function** <br>
We are making use of Haversine Distance for our heuristic function which is used to calculate the distance between two places given their Latitude and Longitude.

**Cost Function** <br>
There are a total of four cost functions for this problem: <br>
1. Segments - This cost function is defined to find the path with the least number of road segments compared to other paths.
2. Distance - This cost function is defined to find the path with the least distance compared to other paths.
3. Time - This cost function is defined to find the path where we can reach very quickly with the condition that the driver drives within the speed limit.
4. Delivery - This cost function is defined to find the fastest path for a delivery driver. There are chances that a package that the delivery driver is holding will fall down if the speed limit on a road is greater than or equal to 50. In that case the driver has to go back to the start city and get a replacement for that package and should avoid the same path when coming back.

**Working of Our Algorithm** <br>
The structure of the code is similar to the previous problems. <br>
We get a the city with minimum heuristic using PriorityQueue. <br>
If goal, return the values. <br>
Check the successors, calculate new heuristics and put into fringe. <br>
Repeat the process until fringe is empty.

**Problems While Coding** <br>
There are some cities where there is no exit, but just connect to a junction which then are connected to different cities or junctions. <br>
We could not implement how the traversing to and from these junction work. And also the delivery time.
We have the idea ready that,
If the village is a dead end, i.e, there are no successor cities, connect to the highway associated with it and hence join the junction.

The code that we have pushed gets the solution if the start and end cities are connected via cities but not via villages adnd juntions.


    PS A:\DOCUMENTS\IU Github\Elements of AI\saburla-ojadhav-mkanitka-a1\Part3> python3 ./route.py Abbot_Village,_Maine Solon,_Maine segments
    Abbot_Village,_Maine
    Bingham,_Maine
    Solon,_Maine
    Start in Abbot_Village,_Maine
       Then go to Bingham,_Maine via ME_16 for 0.5333333333333333
       Then go to Solon,_Maine via US_201 for 0.17777777777777778

              Total segments:    2
                 Total miles:   32.000
                 Total hours:    0.711
    Total hours for delivery:    0.000
