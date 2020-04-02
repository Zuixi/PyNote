import collections

Card = collections.namedtuple('Card', ['rank','suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]



class PyValue:
    # string witl 3 fun
    # use ''
    def __onequote__(self):
        print('Hello,use \' to indicate a string')
    
    def __twoquote__(self):
        print("Hello,use \" to indicate a string")
    
    def __threequote__(self):
        print('''Hello, use three \' to indicate a string''')

    # integer
    def __Int__(self):
        int1 = 1
        int2 = 300
        int3 = -12322
        int4 = 0

        print(int3)

    # float is similar with integer

    # boolean ,just has True or False ,and not or

    # null
    


deck = FrenchDeck()
#print(deck._cards)
print(len(deck))  

value = PyValue()
value.__Int__()
value.__onequote__()
value.__threequote__()

    