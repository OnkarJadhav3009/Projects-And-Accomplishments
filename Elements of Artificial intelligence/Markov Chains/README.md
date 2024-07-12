# a3-release

# Problem 1 Description

In this problem we are given a large text file which has two components the words and their tags. They are basically the different parts of speech. The list of these parts of speech is as follows "adv", "prt", "adp", "conj", "adj", "det", "noun", "num", "pron", "verb", "x". Apart from these there is one more tag i.e. a ".". This tag is given to a punctuation mark encountered in a corpus. The task that we have to perform here is that we have to perform POS tagging i.e. for the data we have been given. This POS tagging has to be done using three algorithms; these are

1. Simplied Method.
2. Viterbi Method.
3. Complex MCMC method.

# Approach 

Firstly we have the implmented the POS tagging by using the Simplified Model. In this we have used the simple Bayes Network for the probability calculation. The formulation of this is as follows:


P(S|W) = max. P(W|S)*P(S)/P(W) 

The probability of a tag given a word is calculated as the product of probability of word given a tag and the probability of that tag. In the denominator the probability of word is calculated. This is calculated by taking the count of that particular word in the dataset divided by the total number of words in the corpus. In the similar way the probability of tags are calculated by taking the total count of a particular tag divided by the total number of tags in the corpus. Lastly, we have calculated the probability of word given a tag by taking the count of how many times a particular word tag pair has occured in the corpus divided by the total count of that particular tag. 

We have repeated the above process for all the words in the corpus and finally the tag with the highest probability is taken as the tag of that particular word.

**2. Viterbi Algorithm**

For this part we have calculated two probabilities i.e. emission and the transition probabilities.Emission probabilities describe the transition probability from the hidden parts of speech hidden state to the words of your corpus. In other words, from POS to a word.  

**The formulation of emission probabilities is as follows.**

 ![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a3/blob/main/Screen%20Shot%202022-12-05%20at%208.11.24%20PM.png).
 
 For eg. if we are calculating the emission probability of a particular word For example the word "Rain"; to calculate the emission probability we will first calculate how many times the word "Rain" has occured with a particular tag, and then we will divide this count with the total number of count of  that particular tag.
 
 **Example for Emission Probability**
 
 ![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a3/blob/main/Screen%20Shot%202022-12-05%20at%2010.16.48%20PM.png)
 
 Next we have calculated the transition probabilities:
 
 **The formulation of the transition probabilities is as follows.**

![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a3/blob/main/Screen%20Shot%202022-12-05%20at%2010.18.33%20PM.png).

Transition probabilities = Count of combination of previous tag and current tag / Count of combination with starting previous tag 

These probabilities can be estimated from a training dataset by counting the number of times each pair of tags appears in the dataset, and dividing by the total number of times the previous tag appears.

**Implementation of Viterbi**
After the calculation of the emission and transition probabilities we have calculated the probabilities of each word given a tag in the entire corpus by multiplying the transition and the emission probabilities for each word. All these probabilities are stored in a array and finally we have taken the max probability and we have assigned the corresponding tag for that word.


**Complex MCMC Algorithm**

Gibbs sampling is a specific example of the Metropolis-Hastings algorithm in its simplest form. In contrast, its extended versions can be used as a general framework for sampling from a large set of variables by sampling each variable (or, in some cases, each group of variables) in turn. One or more of the sampling steps can be implemented using the Metropolis-Hastings algorithm or other techniques, such as slice sampling. Gibbs sampling is used when the conditional distribution of each variable is known and easy to sample from, but the joint distribution is not explicitly known or is difficult to sample from directly. Based on the current values of the other variables, the Gibbs sampling process creates an instance from the distribution of each variable in turn. It can be demonstrated that the samples' sequence forms a Markov chain, and that chain's stationary distribution is exactly the desired joint distribution.


For complex model, while creating the samples we making use of 4 different types of probabilities as below.
1.	Initial probability

3.	Emission Probability

5.	Transition probability

4.	2- layer Transition Probability
<br>
Initial probability : We have calculated this using number of  specific tag divided by total number of tags in the whole corpus.
<br>

Emission probability and Transition probability : These 2 probabilities are same as the one we used in HMM model. 
<br>

2-layer Transition probability : In this transition probability, we are considering transition from previous 2 states and applying same logic as Transition probability for calculating this probability.
<br>


At first, we are calculating 2-layer Transition probability then under the sample_generation function, we are executing probability function to get probability after combining above 4 mentioned probabilities. Also, for generating samples, we are discarding first 30 samples to reduce the relation between original sample and generated sample, after first 30 samples, we are selecting every 10th sample till the total number of generated samples is 100.  Considering these 7 samples, we are deciding label for given word by checking the label with most occurrence for given word.

For all the algorithms we have used laplace smoothing as zero probabilities can cause the overall probability to be zero. So, we have decided the value of alpha of 0.001.

**Problems / Challenges Faced and Enhancements that can be made**
The main problem that we faced was in the understanding of the gibbs sampling algorithm. Hence the accuracy was not as expected. We were not able to decide on the correct number of sample so that probabilities will converge and the correct labels according to the probabilities will be returned. We think that because of this only our accuracy of the algorithm was functioning as expected.

The enhancements that can be made are, currently we are have not removed the punctuations from the corpus. If we remove this we can get an increase in the accuracy of the algorithms. 

# Problem 2 Description
The main task that we have to perform in this problem is that we have to recognize the text from the given image. We have to extract the text as accurate as possible from the provided test images. Some images that are provided have noise in them. For this we have used two algorithms; simplified and Viterbi.

# Approach

**Simplified Model:**
For the simplified part we have first used the pixel to pixel matching from the images. We have compared the basically counted the no. of "*" and the number of blanks i.e. white spaces in the exact image height and image width. From this we got two counts the "*" count and the (" ")blank counts. Finally we are assigning some weights to both the counts. We are assigning more weight to the "*" part as it contains more important information required for mathcing and assigning less weights to the blanks as they contain less significant information. This process is repeated for all the letters in the test images and the letter with the maximum match is then returned and matched.    

**Viterbi / HMM:**

 1. Calculate transition probabilities using the text training set.
     FORMULA: P(letter1|letter2) = count(letter1 -> letter2) / count(letter1)
 We have calculated the probability of letter2 given that previous letter is letter1. To do this, we created a dictionary with letter1 as the key and the value will be another dictionary which has all the other letters as the keys. The value of a key in the nested dictionary is the count of pair of letter2 that comes after letter1 divided by the total count of the letter1 in the corpus.


 2. Calculate emission probabilities using the courier-text and test images. 
     FORMULA: P(letter from courier-train|letter from sentence) = (noise ^ count of stars) * ((1 - noise) ^ count of spaces)
 We were provided with a matrix for each letter from the courier-text and test images. We matched each letter's matrix from one set to another letter's matrix from the other set. In the above formula we tweaked the value of the noise to reach the desired output. 
 
 **Output examples is as follows**
 
 ![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a3/blob/main/test-0-0.png)
 ![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a3/blob/main/test-15-0.png)
 ![ScreenShot](https://github.iu.edu/cs-b551-fa2022/ojadhav-crpathak-sdete-a3/blob/main/test-17-0.png)

