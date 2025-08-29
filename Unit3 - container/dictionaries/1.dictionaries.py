numerals = {'U': 1, 'C': 2, 'B': 3}

#common pattern - lookup value through key
numerals['B']
#3

list(numerals)
#['U', 'C', 'B'] -> use for statement to iterate

list(numerals.values())
#[1, 2, 5]

list(numerals.items())
#[('U', 1), ('C', 2), ('B', 3)] , list made up of tuples

#limitation of dictionaries
#1.mutable types can't be used as keys
#2.two keys can't be equal