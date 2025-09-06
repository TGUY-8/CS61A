suits = ['coin', 'string', 'myriad']
original_suits = suits
suits.pop()
suits.remove('string')
#suits - ['coin']
suits.append('cup')
suits.extend(['sword', 'club'])
#['coin', 'cup', 'sword', 'club']
suits[2] = 'spade'
suits[0:2] = ['heart', 'diamond']
#suits - ['hearts', 'diamond', 'spade', 'club']
print(original_suits)

#only objects of mutable types can change: lists & dictionaries