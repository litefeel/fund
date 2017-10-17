#!/usr/bin/python3
#

import json
import os

from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor

with open('data/162411.js', encoding='utf-8') as f:
    data = f.read()


def get_raw_value(tree, var_name):
    found = False
    for node in nodevisitor.visit(tree):
        # print(node)
        if found:
            return node.to_ecma()
        if isinstance(node, ast.Identifier):
            if node.value == var_name:
                found = True
    return None


# print(data)
parser = Parser()
tree = parser.parse(data)
# print(tree)

# 单位净值走势 equityReturn-净值回报 unitMoney-每份派送金
# [{x:time, y:money}]
# netWorthTrend = get_raw_value(tree, 'Data_netWorthTrend')
# 累计净值走势
# [[time, money]] Data_netWorthTrend == Data_ACWorthTrend
acWorthTrend = get_raw_value(tree, 'Data_ACWorthTrend')


# net_worth = json.loads(netWorthTrend)
ac_worth = json.loads(acWorthTrend)
# print(len(net_worth))
# print(len(ac_worth))
# for i, v in enumerate(net_worth):
#     if v['x'] != ac_worth[i][0]:
#         print('not')
#     if v['y'] != ac_worth[i][1]:
#         print('not y')
    

# and node.value == 'i':
# node.value = 'hello'

def get_xy():
    xs = []
    ys = []
    for v in ac_worth:
        xs.append(v[0])
        ys.append(v[1])
    return xs, ys