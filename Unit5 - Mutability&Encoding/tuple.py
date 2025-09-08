#immutable sequences             
s = (1, 2, 3, 4)
s_ = (2,)
s_2 = s + s_

#tuple is unchangebel -> allowed to use as key
#immutable sequence change binding not value itself
#an immutable sequence may still change if it contains a mutable value as an element