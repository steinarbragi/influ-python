#!/usr/bin/env python
import csv
import sys
from sklearn.model_selection import train_test_split


# input: digg_friends.csv
# output grpah.txt

print("digg_friends.csv -> graph.txt")
fin_link = open('digg/raw/digg_friends.csv')
fout_graph = open("digg/learn/graph_dir.txt", "w")
fout_graph_un = open("digg/learn/graph_undir.txt", "w")
user_set = set()
num_edges = 0
for row in csv.reader(fin_link):
    row[0] = row[0].strip('\n')
    row = row[0].split(' ')
    #mutual = int(row[0])
    timestamp = int(row[2].split('\t')[1])
    u = int(row[0])
    v = int(row[1])
    user_set.add(u)
    user_set.add(v)
    num_edges = num_edges + 1
    fout_graph.write("%d %d %d\n" % (u, v, timestamp))
    fout_graph_un.write("%d %d %d\n" % (u, v, timestamp))
    #if mutual == 1:
    #    fout_graph.write("%d %d %d\n" % (v, u, timestamp))
fin_link.close()
fout_graph.close()
fout_graph_un.close()
print("Number of users: ", len(user_set))
print("Number of directed edges: ", num_edges)

# input: votes.timed.txt
# output: action_logs.txt
print("digg_votes1.csv -> action_logs.txt")
fin_vote = open("digg/raw/digg_votes1.csv", "r")
story_set = set()
action_logs = []
user_set = set()
for row in csv.reader(fin_vote):
    row[0] = row[0].strip('\n')
    row = row[0].split(' ')
    timestamp = int(row[2].split('\t')[1])
    user = row[0]
    story = row[1]
    story_set.add(story)
    user_set.add(user)
    action_logs.append([user, story, timestamp])
fin_vote.close()
print("Number of action logs: ", len(action_logs))
print("Number of stories: ", len(story_set))
print("Number of users voted: ", len(user_set))


train_actions, test_actions = train_test_split(action_logs, test_size=0.2)

story_set_train = set()
story_set_test = set()

for line in train_actions:
    story_set_train.add(line[1])

for line in test_actions:
    story_set_test.add(line[1])

# Sort action logs and output
print("Sorting train_action_logs...")
action_logs = sorted(train_actions, key = lambda t:(t[1],t[0],t[2]))

print("Writing action_logs_train...")
fout_action_train = open("digg/learn/action_logs_train.txt", "w")
for line in train_actions:
    fout_action_train.write("%s %s %s\n" % (line[0], line[1], line[2]))
fout_action_train.close()

print("Writing action_logs_test...")
fout_action_test = open("digg/learn/action_logs_test.txt", "w")
for line in test_actions:
    fout_action_test.write("%s %s %s\n" % (line[0], line[1], line[2]))
fout_action_test.close()


# Output all train action-ids
fout_actionid = open("digg/learn/action_ids_train.txt", "w")
for id in story_set_train:
    fout_actionid.write("%s\n" % id)
fout_actionid.close()


# Output all test action-ids
fout_actionid = open("digg/learn/action_ids_test.txt", "w")
for id in story_set_test:
    fout_actionid.write("%s\n" % id)
fout_actionid.close()
