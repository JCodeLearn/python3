#! /usr/bin/env python3

data1 = {'a': [1, 2.0, 3, 4 + 6j],
         'b': ('string', u'Unicode string'),
         'c': None} 

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

with open('data.pkl', 'wb') as pkl:
    import pickle
    pickle.dump(data1, pkl)
    pickle.dump(selfref_list, pkl, -1)