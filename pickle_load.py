#! /usr/bin/env python3

import pprint, pickle

with open('data.pkl', 'rb') as pkl:
    data1 = pickle.load(pkl)
    pprint.pprint(data1)
    data2 = pickle.load(pkl)
    pprint.pprint(data2)