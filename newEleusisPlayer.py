
import new_eleusis
import random
import decisionTree

class Player():
    def __init__(self, board, god_rule):
        self.board = board
        self.cards_played = 3
        self.god_rule = god_rule
        self.predictedRule = "iff(equal(True,False))"
        self.dt = decisionTree.decisionTree()

    def scientist(self):
        self.dt.build_decision_tree(self.board[-1][0], self.board[-2][0], self.board[-3][0], True)
        self.predictedRule = self.dt.getRules()[0]
        while self.cards_played < 200:
            card = self.select_card()
            result = self.play(card)
            if len(self.board) > 50:
                self.predictedRule = self.dt.getRules()[0]
                print("GOT IT!!")
                return self.predictedRule
            #print("debug",card, self.board[-1][0], self.board[-2][0], result)
            self.dt.build_decision_tree(card, self.board[-1][0], self.board[-2][0], result)
            self.predictedRule = self.dt.getRules()[0]


    def play(self, card):
        rule_tree = new_eleusis.parse(self.god_rule)
        result = rule_tree.evaluate((self.board[-2][0], self.board[-1][0], card))
        self.cards_played += 1
        if result == True:
            self.board.append((card,[]))
            return True
        else:
            self.board[-1][1].append(card)
            return False


    def select_card(self):
        num_correct = len(self.board)
        num_incorrect = self.cards_played - num_correct
        print("debug", self.predictedRule, num_correct, num_incorrect)
        total_cards = self.getDeck()
        if num_correct < num_incorrect:
            for card in total_cards:
                rule_tree = new_eleusis.parse(self.predictedRule)
                result = rule_tree.evaluate((self.board[-2][0], self.board[-1][0], card))
                if result == True:
                    return card
        else:
            for card in total_cards:
                rule_tree = new_eleusis.parse(self.predictedRule)
                #print("here",self.board[-2][0], self.board[-1][0], card)
                #print("here",rule_tree)
                if not rule_tree.evaluate((self.board[-2][0], self.board[-1][0], card)):
                    return card


    def getDeck(self):
        deck = []
        for suit in ['C', 'D', 'H', 'S']:
            for i in range(1, 14):
                deck.append(new_eleusis.number_to_value(i) + suit)
        random.shuffle(deck)
        return deck
