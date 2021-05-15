import sys
print("Python Version: ", sys.version)

array = [['a', 'b', 'c', 'd'], ['1', '2', '3']]

out = []
for ii, rule in enumerate(array): # a rule
    for ij, valR, in enumerate(rule): # each element in a rule
        out.append([valR])
        for ik, rule2 in enumerate(array): # all other rules
            if (ik != ii):
                for il, valL, in enumerate(rule): # each element in all other rules
                    out.append([valR, valL])
                
print(out)