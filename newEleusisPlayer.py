'''
This module deals with functions of player
selecting the best next card
adding to board state
popuating decision table
'''


'''
initialize board state and call populate_table for those cards and see if hypothesis comes to be true

'''


import populateDecisionTable
from collections import defaultdict
from operator import itemgetter

board = [('10S',[]),('3H',[]),('6C',['KS','9C']),('6H',[]),('7D',[]),('9S',['AS'])]

attributes = defaultdict(list)
for i in range(2,len(board)):
    curr = board[i][0]
    prev = board[i-1][0]
    prev2 = board[i-2][0]
    attributes = populateDecisionTable.populate_attribute(attributes, curr, prev, prev2, valid = True)
    if board[1] != []:
        for curr in board[i][1]:
            attributes = populateDecisionTable.populate_attribute(attributes, curr, board[i][0], board[i-1][0], valid = False)
def get_information_gain(attributes, attr):
    count = 0
    check_list = attributes[attr]
    for check in check_list:
        if check == True:
            count += 1
    if count == 0:
        return 0.0
    return count/len(check_list)
#get best attribute
attributes_list = []
for attr in attributes:
    info_gain = get_information_gain(attributes, attr)
    attributes_list.append((attr,info_gain))
attributes_list.sort(key=itemgetter(1),reverse=True)
for attr in attributes:
    if get_information_gain(attributes,attr) != 0.0:
        print("[------------------------]")
        print(attr, "---------", attributes[attr],"_----_",get_information_gain(attributes,attr))