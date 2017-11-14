'''
This file deals with populating the decision table
called when a new card is played
'''
#structure would be a dict with key as strnig value of function and value as tuple of
# function and arguments



'''
//TODO: insert hypothesis using plus1 and minus1 functions

'''
from collections import defaultdict
import new_eleusis


def populate_attribute(attributes, curr, prev, prev2, valid):

    #single card attributes
    #color, even, suit, royal

    cards = [curr,prev,prev2]
    cards_names = ["current",'prev','prev2']
    function_names = [ "even", "is_royal","odd"]
    functions = [new_eleusis.even, new_eleusis.is_royal, new_eleusis.odd]

    for card,card_name in zip(cards,cards_names):
        for func_names,func in zip(function_names,functions):
            attributes[func_names + "('"+str(card_name)+"')"].append(func(card))

    #value list
    values = range(1,14)

    #suit list
    suits = ['C','D', 'H', 'S']

    #color list
    colors = ['B','R']

    function_names_two = ['equal', 'less', 'greater']
    functions_two = [new_eleusis.equal, new_eleusis.less, new_eleusis.greater]
    #double card attributes
    for card,card_name in zip(cards,cards_names):
        for func_name_two,func_two in zip(function_names_two,functions_two):
            for value in values:
                if func_name_two == 'equal':
                    attributes[func_name_two + "(value('"+card_name+"')," + str(value)+")"].append(func_two(new_eleusis.value(card),value))
                    attributes[func_name_two + "(plus1(value('"+card_name+"'))," + str(value)+")"].append(func_two(new_eleusis.plus1(str(new_eleusis.value(card))),value))
                    attributes[func_name_two + "(minus1(value('" + card_name + "'))," + str(value) + ")"].append(func_two(new_eleusis.minus1(str(new_eleusis.value(card))), value))
                if func_name_two == 'less':
                    if value != 1 and value != 13:
                        attributes[func_name_two + "(value('" + card_name +"')," +str(value)+")"].append(func_two(str(new_eleusis.value(card)),value))
                        attributes[func_name_two + "(plus1((value('" + card_name + "'))," + str(value) + ")"].append(func_two(str(new_eleusis.plus1(str(new_eleusis.value(card)))),str(value)))
                        attributes[func_name_two + "(minus1((value('" + card_name + "'))," + str(value) + ")"].append(func_two(str(new_eleusis.minus1(str(new_eleusis.value(card)))), value))
                if func_name_two == "greater":
                    if value != 13 and value != 1:
                        attributes[func_name_two + "(value('" + card_name +"'),"+str(value)+")"].append(func_two(str(new_eleusis.value(card)),str(value)))
                        attributes[func_name_two+ "(plus1(value('" + card_name +"')," + str(value) + ")"].append(func_two(str(new_eleusis.plus1(str(new_eleusis.value(card)))),str(value)))
                        attributes[func_name_two + "(minus1(value('" + card_name + "')," + str(value) + ")"].append(func_two(str(new_eleusis.minus1(str(new_eleusis.value(card)))), str(value)))
            for suit in suits:
                if func_name_two == 'equal':
                    attributes[func_name_two + "(suit('" + card_name + "'),'" + suit+"')"].append(func_two(new_eleusis.suit(card),suit))
                    if suit != 'S' and new_eleusis.suit(card) != 'S':
                        attributes[func_name_two + "(plus1(suit('" + card_name + "'),'" + suit + "')"].append(func_two(new_eleusis.plus1(new_eleusis.suit(card)),suit))
                    if suit != 'C' and new_eleusis.suit(card) != 'C':
                        attributes[func_name_two + "(minus1(suit('" + card_name + "'),'" + suit + "')"].append(func_two(new_eleusis.minus1(new_eleusis.suit(card)), suit))
                if func_name_two == 'less':
                    if suit != 'C' and suit != 'S':
                        attributes[func_name_two + "(suit('" +card_name+"'),'" +suit+ "')"].append(func_two(str(new_eleusis.suit(card)),suit))
                        if suit != 'S' and new_eleusis.suit(card) != 'S':
                            attributes[func_name_two + "(plus1(suit('" + card_name + "'),'" + suit + "')"].append(func_two(new_eleusis.plus1(new_eleusis.suit(card)), suit))
                        if suit != 'C' and new_eleusis.suit(card) != 'C':
                            attributes[func_name_two + "(minus1(suit('" + card_name + "'),'" + suit + "')"].append(func_two(new_eleusis.minus1(new_eleusis.suit(card)), suit))
                if func_name_two == 'greater':
                    if suit != 'S' and suit != 'C':
                        attributes[func_name_two + "(suit('" +card_name+"')," +suit+"')"].append(func_two(str(new_eleusis.suit(card)),str(suit)))
                        if suit != 'S' and new_eleusis.suit(card) != 'S':
                            attributes[func_name_two + "(plus1(suit('" + card_name + "'),'" + suit + "')"].append(func_two(new_eleusis.plus1(new_eleusis.suit(card)), suit))
                        if suit != 'C' and new_eleusis.suit(card) != 'C':
                            attributes[func_name_two + "(minus1(suit('" + card_name + "'),'" + suit + "')"].append(func_two(new_eleusis.minus1(new_eleusis.suit(card)), suit))
            for color in colors:
                if func_name_two == 'equal':
                    attributes[func_name_two + "(color("+card_name+"),'"+str(color)+"')"].append(func_two(new_eleusis.color(card),str(color)))
                    attributes[func_name_two + "(plus1(color(" + card_name + ")),'" + str(color) + "')"].append(func_two(new_eleusis.plus1(new_eleusis.color(card)),str(color)))
                    attributes[func_name_two + "(minus1(color(" + card_name + ")),'" + str(color) + "')"].append(func_two(new_eleusis.minus1(new_eleusis.color(card)), str(color)))



    for i in range(len(cards)-1):
        for j in range(i+1,len(cards)):
            for func_name_two,func_two in zip(function_names_two,functions_two):
                attributes[func_name_two + "(" + cards_names[i]+","+cards_names[j]+")"].append(func_two(cards[i],cards[j]))
                attributes[func_name_two + "(value('"+cards_names[i]+"'),value('"+cards_names[j]+"'))"].append(func_two(str(new_eleusis.value(cards[i])), str(new_eleusis.value(cards[j]))))
                attributes[func_name_two + "(color('" + cards_names[i] + "'),color('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.color(cards[i])), str(new_eleusis.color(cards[j]))))
                attributes[func_name_two + "(suit('" + cards_names[i] + "'),suit('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.suit(cards[i])), str(new_eleusis.suit(cards[j]))))

                attributes[func_name_two + "(plus1(" + cards_names[i] + ")," + cards_names[j] + ")"].append(func_two(cards[i], cards[j]))
                attributes[func_name_two + "(plus1(value('" + cards_names[i] + "')),value('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.value(cards[i])), str(new_eleusis.value(cards[j]))))
                attributes[func_name_two + "(plus1(color('" + cards_names[i] + "')),color('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.color(cards[i])), str(new_eleusis.color(cards[j]))))
                attributes[func_name_two + "(plus1(suit('" + cards_names[i] + "')),suit('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.suit(cards[i])), str(new_eleusis.suit(cards[j]))))

                attributes[func_name_two + "(minus1(" + cards_names[i] + ")," + cards_names[j] + ")"].append(func_two(cards[i], cards[j]))
                attributes[func_name_two + "(minus1(value('" + cards_names[i] + "')),value('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.value(cards[i])), str(new_eleusis.value(cards[j]))))
                attributes[func_name_two + "(minus1(color('" + cards_names[i] + "')),color('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.color(cards[i])), str(new_eleusis.color(cards[j]))))
                attributes[func_name_two + "(minus1(suit('" + cards_names[i] + "')),suit('" + cards_names[j] + "'))"].append(func_two(str(new_eleusis.suit(cards[i])), str(new_eleusis.suit(cards[j]))))




    if valid == False:
        for attr in attributes:
            if attributes[attr] == False:
                attributes[attr] = True
            elif attributes[attr] == True:
                attributes[attr] = False

    # for attr in attributes:
    #     if attributes[attr][0] == True:
    #         print(attr,attributes[attr])
    print("this is count",len(attributes))
    return attributes