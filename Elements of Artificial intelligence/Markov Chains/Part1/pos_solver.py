###################################
# CS B551 Fall 2022, Assignment #3
#
# Your names and user ids:
#
# (Based on skeleton code by D. Crandall)
#


import random
import math
import copy


# We've set up a suggested code structure, but feel free to change it. Just
# make sure your code still works with the label.py and pos_scorer.py code
# that we've supplied.
#
class Solver:
    count_dic = {}
    tags_count = {"adv": 0, "prt": 0, "adp": 0, "conj": 0, "adj": 0, "det": 0, "noun": 0, "num": 0, "pron": 0,
                  "verb": 0, "x": 0, ".": 0}
    total_tag_count = {"adv": 0, "prt": 0, "adp": 0, "conj": 0, "adj": 0, "det": 0, "noun": 0, "num": 0, "pron": 0,
                       "verb": 0, "x": 0, ".": 0}
    total_word_count = 0
    sim_word_prob = {}
    sim_word_label = {}

    transition_probs = {"adv": {}, "prt": {}, "adp": {}, "conj": {}, "adj": {}, "det": {}, "noun": {}, "num": {},
                        "pron": {},
                        "verb": {}, "x": {}, ".": {}}
    initial_probs = {}
    emission_probs = {}
    hmm_word_labels = {}
    hmm_word_prob = {}

    laplace_alpha = 0.001

    transition2_probs = copy.deepcopy(transition_probs)

    mcmc_prob = []

    # Calculate the log of the posterior probability of a given sentence
    #  with a given part-of-speech labeling. Right now just returns -999 -- fix this!
    def posterior(self, model, sentence, label):
        if model == "Simple":
            prob = 0.0
            for word in sentence:
                prob += math.log(self.sim_word_label[word][1])

            return prob

        elif model == "HMM":
            prob = 0.0
            for word in sentence:
                prob += math.log(self.hmm_word_prob[word])
            return prob

        elif model == "Complex":
            sentence = list(sentence)
            labels = list(label)
            prob = math.log(self.total_tag_count[labels[0]]/sum(self.total_tag_count.values()))
            a = 0
            b = 0
            for i in range(len(label)) :
                if sentence[i] in self.count_dic.keys() :
                    a += math.log(self.emission_probs[sentence[i]][labels[i]])
                if i != 0 :
                    b += math.log(self.transition_probs[labels[i-1]][labels[i]])

            return prob+a+b
        else:
            print("Unknown algo!")

    # Do the training!
    #
    def train(self, data):

        for line in data:
            for i in range(len(line[1])):
                self.total_tag_count[line[1][i]] += 1

            for i in range(len(line[0])):
                if line[0][i] not in self.count_dic.keys():
                    temp = copy.deepcopy(self.tags_count)
                    self.count_dic[line[0][i]] = temp
                    self.count_dic[line[0][i]][line[1][i]] = 1
                else:
                    self.count_dic[line[0][i]][line[1][i]] += 1

        self.simple_train(data)

        for i in self.transition_probs.keys():
            self.transition_probs[i] = copy.deepcopy(self.tags_count)

        for i in self.transition2_probs.keys() :
            self.transition2_probs[i] = copy.deepcopy(self.transition_probs)

        for i in self.transition2_probs.keys() :
            for j in self.transition2_probs[i].keys() :
                self.transition2_probs[i][j] = copy.deepcopy(self.tags_count)

        self.calcTransitionProbabilities(data)
        self.calcEmissionProbabilities(data)
        self.calculateInitialProbabilities(data)
        self.hmm_train(data)

        self.cal_transition2_probablitites(data)

    def simple_train(self, data):
        for i in self.count_dic.keys():
            temp = copy.deepcopy(self.count_dic[i])
            for t in temp.keys():
                temp[t] *= 1.0
            self.sim_word_prob[i] = temp

        for i in self.count_dic.keys():
            for l in self.sim_word_prob[i]:
                self.sim_word_prob[i][l] = (self.sim_word_prob[i][l] + self.laplace_alpha) / (self.laplace_alpha * self.total_tag_count[l])

        label = []
        for i in self.total_tag_count.keys():
            label.append(i)

        for i in self.count_dic.keys():
            p = []
            for j in self.sim_word_prob[i].keys():
                p.append(self.sim_word_prob[i][j])
            ind = p.index(max(p))
            self.sim_word_label[i] = (label[ind], max(p))

    def calculateInitialProbabilities(self, data):
        for line in data:
            word = line[0][0]
            if word not in self.initial_probs:
                self.initial_probs[word] = 1
            else:
                self.initial_probs[word] += 1

        for k, v in self.initial_probs.items():
            self.initial_probs[k] = (v + 1) / (self.individual_word_count(k) + 2)

    def individual_word_count(self, word):
        count = 0
        for i in self.count_dic[word].keys():
            count += self.count_dic[word][i]

        return count

    def hmm_train(self, data):
        label_list = [k for k in self.tags_count.keys()]
        state = []
        for line in data:
            for i in range(len(line[0])):
                p = []
                for l in label_list:
                    if len(state) == 0:
                        transition_prob = self.initial_probs[line[0][i]]
                    else:
                        transition_prob = self.transition_probs[state[-1]][l]
                    emission_prob = self.emission_probs[line[0][i]][l]
                    s_prob = transition_prob * emission_prob
                    p.append(s_prob)

                label = label_list[p.index(max(p))]
                state.append(label)

                self.hmm_word_prob[line[0][i]] = max(p)
                self.hmm_word_labels[line[0][i]] = label

    # Functions for each algorithm. Right now this just returns nouns -- fix this!
    #
    def simplified(self, sentence):
        label_list = []

        for word in sentence:
            if word not in self.sim_word_label.keys():
                self.sim_word_label[word] = ("noun", 1)

            label_list.append(self.sim_word_label[word][0])

        return label_list

    def hmm_viterbi(self, sentence):
        label_list = []

        for word in sentence:
            if word not in self.hmm_word_labels.keys():
                self.hmm_word_labels[word] = "noun"
                self.hmm_word_prob[word] = 1.0

            label_list.append(self.hmm_word_labels[word])

        return label_list

    def calcTransitionProbabilities(self, data):
        temp = []
        for line in data:
            tags = line[1]
            i = 0
            while i < len(tags) - 1:
                temp = self.transition_probs[tags[i]]
                if tags[i + 1] not in temp:
                    temp[tags[i + 1]] = 1
                else:
                    temp[tags[i + 1]] += 1
                self.transition_probs[tags[i]] = temp
                i += 1

        rs = {}

        for k, v in self.transition_probs.items():
            rs[k] = sum(v.values())

        for k, v in self.transition_probs.items():
            for k_, v_ in v.items():
                self.transition_probs[k][k_] = (v_ + self.laplace_alpha) / (rs[k] * self.laplace_alpha)

    def emission_dictionary(self, data):
        for line in data:
            for word in line[0]:
                self.emission_probs[word] = copy.deepcopy(self.tags_count)

    def calcEmissionProbabilities(self, data):
        self.emission_dictionary(data)
        for line in data:
            for word, tag in zip(list(line[0]), list(line[1])):
                self.emission_probs[word][tag] += 1

        for k, v in self.emission_probs.items():
            for k_, v_ in self.emission_probs[k].items():
                self.emission_probs[k][k_] = (v_ + self.laplace_alpha) / (self.laplace_alpha * self.total_tag_count[k_])
    
    def cal_transition2_probablitites(self,data) :
        
        for line in data :
            for i in range(2,len(line[1])) :
                self.transition2_probs[line[1][i-2]][line[1][i-1]][line[1][i]] += 1

        for i in self.transition2_probs.keys() :
            for j in self.transition2_probs[i].keys() :
                for k in self.transition2_probs[i][j].keys() :
                    if self.transition2_probs[i][j][k] != 0 :
                        self.transition2_probs[i][j][k] = self.transition2_probs[i][j][k] / sum(self.transition2_probs[i][j].values())
                    else :
                        self.transition2_probs[i][j][k] = 10 ** (-5)
        
    def complex_mcmc_prob(self,sentence,tags) :
        
        a = self.total_tag_count[tags[0]] / sum(self.total_tag_count.values())
        b = 1
        c = 1
        d = 1

        for i in range(len(tags)) :
            if sentence[i] in self.count_dic.keys() :
                b += self.emission_probs[sentence[i]][tags[i]]
            if i != 0 :
                c += self.transition_probs[tags[i-1]][tags[i]]
            if i != 0 and i != 1 :
                d += self.transition2_probs[tags[i-2]][tags[i-1]][tags[i]]

        return a*b*c*d 

    def sample_generation(self,sentence,sample) :
        labels = [i for i in self.tags_count.keys()]

        for ind in range(len(sentence)) :
            prob_array = copy.deepcopy(self.tags_count)

            for i in range(len(labels)) :
                sample[ind] = labels[i]
                prob_array[labels[i]] = self.complex_mcmc_prob(sentence,sample)

            min_prob = min(prob_array.values())

            for i in prob_array.keys() :
                prob_array[i] /= min_prob

            prob_sum = sum(prob_array.values())

            p = []
            for i in prob_array.keys() :
                p.append(prob_array[i] /prob_sum)

            r = random.random()
            x = 0
            for i in range(len(p)) :
                x += p[i]
                if r < x :
                    sample[ind] = labels[i]
                    break

        return sample

    def mcmc(self,sentence) :
        sample = self.hmm_viterbi(sentence)
        samples = []
        iterations = 100
        throw_iteration = 30

        for i in range(iterations) :
            sample = self.sample_generation(list(sentence),sample)
            if i >= throw_iteration and i % 10 == 0 :
                samples.append(sample)

        
        labels_list = []
        for word in sentence :
            sample_tags_count = copy.deepcopy(self.tags_count)
            for sample in samples :
                sample_tags_count[sample[list(sentence).index(word)]] += 1
            l = max(sample_tags_count, key = sample_tags_count.get)
            labels_list.append(l)

        return labels_list
    
    def complex_mcmc(self, sentence):
        return self.mcmc(sentence)

    # This solve() method is called by label.py, so you should keep the interface the
    #  same, but you can change the code itself. 
    # It should return a list of part-of-speech labelings of the sentence, one
    #  part of speech per word.
    #
    def solve(self, model, sentence):
        if model == "Simple":
            return self.simplified(sentence)
        elif model == "HMM":
            return self.hmm_viterbi(sentence)
        elif model == "Complex":
            return self.complex_mcmc(sentence)
        else:
            print("Unknown algo!")
