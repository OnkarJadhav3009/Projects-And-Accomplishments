# ojadhav-crpathak-sdete-a2
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
**Problem 1:**

**1.DESCRIPTION:**

The problem is about finding the next best possible move from a given state to the next state. In the given problem, we are provided with a starting state, we have to find the next best move for either white or black set according to the input. 

Each side has three type of pieces: Pichu, Pikachu and Raichu.

White Pichu moves diagonally one step to the bottom left or bottom right. Black Pichu moves diagonally one step to the top left and top right. If an opponent pichu is present at the move step, out pichu jumps one step over the oppenent pichu.
When a pichu reaches the end of opposite side, it becomes raichu.

White Pikachu moves down, left or right one or two steps. If an oppenent pichu or pikachu is present at the move step, our pikachu jumps over the opponent pichu or pikachu and moves one step. Black Pikachu moves up, left or right one or two steps. If an oppenent pichu or pikachu is present at the move step, our pikachu jumps over the opponent pichu or pikachu and moves one step.
When a pikachu reaches the opposite side, it becomes raichu.

A Raichu can move in all 8 direction at any empty cell, provided all the cells in between are empty. A Raichu can jump over only one opponent pichu/pikachu or raichu and land on any cell that is empty provided all the cells in between the jumped cell and landing cell are empty.


**2. APPROACH:**

We have chosen to implement alpha beta pruning to solve this problem. Since the amount of successors in for each state is very large, especially if a raichu is present on the board, exploring the states while require a lot of time and then obtaining an optimal outcome will become time consuming. To avoid this problem pruning some branches in the explored tree will be beneficial.

In the begining, we got the successors for each of the type of piece, ie, white pichu, pikachu and raichu, and black pichu, pikachu and raichu.

After obtaining the successors, we implemented alpha beta pruning algorithm.


**3. WORKING OF THE MODEL:**

The begining of the alpha beta pruning starts from the minimax algorithm. The minimax algorithm explores all the states starting from initial state recursively. Alternate levels are played by max and min players. The initial starting node is played by the max node. The max node explores all the successor states of the current player. Then we explore all the successors of the successors according to the oppenent. We do this recursively untill we reach a winning, loosing or a tie condition. After reaching the terminal state, we assign each of the nodes with +1 if winning, 0 if a tie and -1 if loosing.
After exploring all the possible moves and assigning the values, to decide a move we have to back up the values till the root max node. This decision is carried out by maximizing the max node with min values of minimum nodes. Similartly, the min decision is given by minimizing the min node with the max value of the max nodes.
We reach a point where the successors of the initial state are assigned certain values. The initial max node plays the successor with the max value.

**We can make it better.**

Instead of assigning values as +1, 0 and -1, we can assign them an evaluation value, i.e a heuristic that determines how close the current state is to winning.
By doing this we can maximize and minimize efficiently. 
Also instead of going to terminal states, we can go to certain depth and then backtrack and get the decision.

The final step to optimizing comes by alpha beta pruning. Each node is assigned an alpha and a beta value. We maximize max node's alpha from min values of min nodes.We minimize min node's beta from max values of max nodes. 
If a max node's beta value is less than or equal to alpha value we prune the branch and return the alpha. If a min node's alpha is greater than or equal to the beta value then prune the branch and return beta.

The minimax decision is given by the max value of the beta values of the successor min nodes.


4. ALPHA BETA PRUNING:

        MAX-Value(S, alpha, beta)
        - If Terminal?(S) return Result(S)
        - For all S' belongs SUCC(S)
        -        alpha <- max(alpha, MIN-Value(S',alpha,beta)
        -        if beta <= alpha, return alpha
        - return alpha
        MIN-Value(S, alpha, beta)
        - If Terminal?(S) return Result(S)
        - For all S' belongs SUCC(S)
        -        beta <- max(beta, MAX-Value(S',alpha,beta)
        -        if alpha >= alpha, return beta
        - return beta

    (from professor's slides)


5. CHALLENGES FACED:

i.Heuristic: Did not get an admissible evaluation of heuristic for a state.
Because of this, in certain states, getting an optimal next move becomes time consuming. The min max decision comes out to be sub obtimal.

ii.Writing successors: Since there are different rules for different type of pieces, writing the functions of obtaining the successors becaume tedious.

iii.Moving Raichu: Since the number successors for a raichu piece is huge, the heuristic value for each successor had to be distinct. Due to suboptimal heuristic, the minmax node was choosing an suboptimal move.

iv.Sometimes using higher depths for simple moves make the algorithm not work. So we have used dynamic depth according to the current state.



**STATE SPACE**: The state space consists of all the boards containing or not containing all the pieces provided those pieces obey their rule. 

    for eg:
    ...........
    ....b...w..
    ...b...w...
    ..@...$....
    ....w..w...
    ..W...W....
    ...b...W...
    ...@.......

**INITIAL STATE**: The initial state is a board which can be empty or contains atleast one of the pieces.

    for eg:
    .......$...
    ...w.w...w.
    ..WW..W....
    ...$...b.b.
    ..b.b...b..
    ..W..W...@.
    ..@........

**GOAL STATE**: Goal state is a state where one of the player wins or is a tie.

    for eg:
    .......$...
    ...........
    ...........
    ...........
    ..b.b...b..
    ...........
    ...........

**COST FUNCTION**:

We have chosen count of the our player pieces minus the count of opponent pieces.
We have given 1 weight to pichu, twice weightage to Pikachu and 4 times the weight to raichu.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------


**Problem 2:
Description**:
In this problem we were given two datasets which contained movie reviews. The dataset was a labeled dataset which contained some reviews and each review was given a label which was either "deceptive" or "truthful". Our task was to correctly classify the reviews from the given test dataset as truthful or deceptive using the Naive Bayes classifier.

**Approach**:
The skeleton code which was given contained a funtion named classifier to which the train data and test data were given as two parameters.This function was not doing anything in the start. It just returned sample accuracy as 50 percent. We followed the following steps to improve the accuracy of the classifier function.

1. **Preprocessing the data:**

    a. **Removing the punctuation marks**: Firstly when we observed the dataset we noticed that the train dataset consisted of many punctuations. In the first step we removed all these punctuation marks from the sentences. We got the ouput as only the sentences without any punctuation marks in it.

    b. **Removing the Whitespaces**: The next step that we performed in the pipeline was that of removing the whitespaces in the words. We observed that there were some words which contained whitespaces between them and these were affecting the accuracy of the model. Hence, we removed the observed whitespaces.

    c. **Removing the Stopwords**: After this we performed the step of removing the stopwords from the sentences. We performed this in order to remove the non-important words from the setences so as to focus on the more important words which were contributing more towards the accuracy of the model. The list of stopwords was taken from the  link (https://gist.github.com/sebleier/554280).

    d. **Creating a Vocabulary**: In this part we created vocabulary i.e. a set of all the unique words from the sentences.

    e. **Converting the words to lowercase**: In this step we are converting all the words in the train dataset into lowercase. This helped us reduce the entropy of the system. For e.g. if we don't convert the words into lower case we end up using three different combinations of the same word "YOU'RE" and "you're" and "You're". Instead if we only use the single lower case word "you're" we end up reducing the combinations and this will help in increasing the accuracy of the model.
   
2. **Applying Naive Bayes Classifier:**
   
   a. **Calculating the probabilities**:
 
      i. The first step that we did was to calculate the probalities of truthful and deceptive messages. The probablity of truthful messages was calculated by dividing the count of truthful messages by the count of all the messages i.e. truthful and deceptive messages. In a similar manner we calculated the probability of deceptive messages.
      
     ii. In the next step calculates the probablity for P(Word|Truthful) and P(Word|Deceptive). These probabilites were calculated by using the below formula. In the formula alpha is the laplace smoothing coefficient.
       
     ![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a2/blob/main/Screen%20Shot%202022-11-11%20at%209.21.12%20PM.png)
     
  b. **Classify the Sentences:** 
  
  While classifying the images the following steps were followed:

  1. Firstly we are taking the sentences as the input.
  2. Then we are splitting the sentence into words.
  3. Once we get these words we are calculating the probality of each word given truth and each word given deceptive for the given sentence.
  4. Then we are comparing the probabilities. If the probability of deceptive is greater than truthful then the given sentence is classified as Truthful otherwise it is a Deceptive sentence.

3. **Steps taken to improve the accuracy:**
   1. We have used the laplace smoothing for improving the accuracy. Laplace smoothing is a smoothing technique that helps tackle the problem of zero probability in the Naïve Bayes machine learning algorithm. Using higher alpha values we tried to push the likelihood towards a value of 0.5, i.e., the probability of a word equal to 0.5 for both the truthful and deceptive reviews.
   2. We are also using log probabilities for calculation. We are using this because when we multiply two small numbers this leads to even smaller numbers. It is difficult to precisely store and compare these very small numbers. To avoid working with very small numbers, we are taking the log probabilities by taking the logarithm of probability values. While calculating the probabilities the log property i.e. log A + log B = log AB is used.

4. **Problems Faced**:
   1. The main problem that was faced was deciding the laplace coefficient for smoothing. For this we plotted the graph for different values of coefficient v/s the accuracy and decided the value of alpha.
   2. Other problem that was faced was performing the preprocessing task without using libraries like nltk.
   3. Final accuracy of our model was 87.25. This accuracy can be improved by using root words, correcting the spelling. But the challenges we faced was implmenting witout using nltk. 
