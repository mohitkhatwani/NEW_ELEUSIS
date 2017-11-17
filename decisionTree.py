from collections import defaultdict, Counter
import populateDecisionTable

class Node():
    def __init__(self, child = None):
        if child == None:
            self.child = []
        else:
            self.child = child
        self.path = None
        self.id = None
    def setID(self, id):
        self.id = id
    def setChildren(self, children):
        self.child = children
    def getChildren(self):
        return self.child
    def setPath(self, path):
        self.path = path


class decisionTree():
    def __init__(self):
        self.attributes = defaultdict(list)
        self.result = []
        self.root = Node()
        self.rules_list = []

    def build_decision_tree(self,curr,prev,prev2, decision):
        self.rules_list = []
        self.attributes, self.result = populateDecisionTable.populate_attribute(self.attributes, curr, prev, prev2, self.result, decision)
        self.createDecisiontree(self.attributes,[], self.result)

    def getRoot(self):
        return self.root

    def print_tree(self,root):
        print(root.id)
        if root.id != True and root.id != False:
            children = root.getChildren()
            for child in children:
                self.print_tree(child)

    def createDecisiontree(self, attributes,node, result):
        split_attributes, minimum_information_gain = self.getSplitAttributes(attributes, result)
        #print("split",split_attributes)
        if minimum_information_gain == 0:
            for split_attr in split_attributes:
                temp = []
                if node != []:
                    temp.extend(node)
                temp.append(split_attr)
                self.rules_list.append(temp)
        else:
            for attrs in split_attributes:
                tables, results = self.splitTableWithAttribute(attributes, attrs, result)
                self.createDecisiontree(tables[0], attrs, results[0])
                self.createDecisiontree(tables[1], attrs, results[1])


    def splitTableWithAttribute(self,attributes, split_attribute, result):
        table_true = []
        result_true = []
        table_false = []
        result_false = []
        for i in range(len(attributes[split_attribute])):
            if attributes[split_attribute][i] is True:
                table_true.append(attributes[split_attribute][i])
                result_true.append(result[i])
            else:
                table_false.append(attributes[split_attribute][i])
                result_false.append(result[i])
        tables = [table_true, table_false]
        results = [result_true, result_false]
        return tables, results


    def getSplitAttributes(self, attributes, result):
        mini = 9999
        split_attrs = []
        for attr in attributes:
            information_gain = self.getInformationGain(attributes, attr, result)
            if information_gain < mini:
                mini = information_gain
        for attr in attributes:
            information_gain = self.getInformationGain(attributes, attr, result)
            if information_gain == mini:
                split_attrs.append(attr)
        return split_attrs, mini

    def getInformationGain(self, attributes, attr, result):
        count = 0
        for i in range(len(attributes[attr])):
            if attributes[attr][i] != result[i]:
                count += 1
        # if count == len(result):
        #     return 0
        return abs(count)

    def is_leaf(self, result):
        count = Counter(result)
        if count[True] == 0 or count[False] == 0:
            return True
        else:
            return False

    def getRules(self):
        final_rules = []
        if len(self.rules_list) == 1:
            final_rule = ""
            final_rule += "iff(" + str(self.rules_list[0]) + ",True)"
            final_rules.append(final_rule)
        else:
            for rule in self.rules_list:
                temp_rule = ""
                if len(rule) != 1:
                    temp_rule = "andf("
                    for i in range(len(rule)):
                        temp_rule += str(rule[i])
                        if i != len(rule) - 1:
                            temp_rule += ','
                        else:
                            temp_rule += ")"
                else:
                    temp_rule = rule[0]
                final_rules.append(temp_rule)
        return final_rules


