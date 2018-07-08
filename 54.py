CARD_VALS = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
SUITS = ['C','H','S','D']

class Card(object):    
    def __init__(self, string):
        self.val = CARD_VALS.index(string[0]) + 2
        self.suit = string[1]
        
    def __lt__(self, other):
        if self.val == other.val:
            return self.suit < other.suit
        return self.val < other.val
    
    def __eq__(self, other):
        return self.suit == other.suit and self.val == other.val
    
    def __str__(self):
        return CARD_VALS[self.val-2]+self.suit
    

def get_major_suit(hand):
    cnt = {}
    for suit in SUITS:
        cnt[suit] = 0
    for card in hand:
        cnt[card.suit] += 1
    
    max_freq = max(cnt.values())
    for suit in SUITS:
        if cnt[suit] == max_freq:
            return suit
        
def get_val_freqs(hand):
    freqs = {}
    for card in hand:
        if not freqs.has_key(card.val):
            freqs[card.val] = 0
        freqs[card.val] += 1
    return freqs


def get_ordered_vals(hand):
    vals = []
    for card in hand:
        vals.append(card.val)
    vals.sort()
    vals.reverse()
    return vals
    
    
def royal_flush(hand):
    suit = get_major_suit(hand)
    for val in ['T','J','Q','K','A']:
        req = Card(val+suit)
        #print req
        if req not in hand:
            return 0
    return hand[-1].val


def straight_flush(hand):
    for i in xrange(len(hand)-1):
        if hand[i+1].suit != hand[i].suit:
            return 0
        dif = hand[i+1].val - hand[i].val
        if dif != 1:
            return 0
    return hand[-1].val


def four_kind(hand):
    freqs = get_val_freqs(hand)
    if max(freqs.values()) == 4:
        val = 0
        for item in freqs.keys():
            if freqs[item]  == 1:
                val += item
            elif freqs[item] == 4:
                val += 100*item
        return val
    else:
        return 0
    
def full_house(hand):
    freqs = get_val_freqs(hand)
    blah = freqs.values()
    blah.sort()
    if blah == [2,3]:
        vals = [0,0]
        for val in freqs.keys():
            if freqs[val] == 3:
                vals[0] = val
            elif freqs[val] == 2:
                vals[1] = val
        return vals
    else:
        return 0


def flush(hand):
    suit = get_major_suit(hand)
    for card in hand:
        if card.suit != suit:
            return 0
    return get_ordered_vals(hand)


def straight(hand):
    for i in xrange(len(hand)-1):
        dif = hand[i+1].val - hand[i].val
        if dif != 1:
            return 0
    return hand[-1].val  


def three_kind(hand):
    freqs = get_val_freqs(hand)
    blah = freqs.values()
    blah.sort()    
    if blah == [1,1,3]:
        vals = [0]
        for val in freqs.keys():
            if freqs[val] == 3:
                vals[0] = val
            else:
                vals.append(val)
        assert len(vals) == 3
        if vals[1] < vals[2]:
            vals[1],vals[2] = vals[2],vals[1]
        return vals
    else:
        return 0
    
    
def two_pair(hand):
    freqs = get_val_freqs(hand)
    blah = freqs.values()
    blah.sort()
    if blah == [1,2,2]:
        vals = [0]
        for val in freqs.keys():
            if freqs[val] == 1:
                vals[0] = val
            else:
                vals.append(val)
        assert len(vals) == 3
        vals[0],vals[2] = vals[2],vals[0]
        if vals[0] < vals[1]:
            vals[0],vals[1] = vals[1],vals[0]
        return vals
    else:
        return 0
    
def one_pair(hand):
    freqs = get_val_freqs(hand)
    blah = freqs.values()
    blah.sort()
    if blah == [1,1,1,2]:
        vals = []
        for val in freqs.keys():
            if freqs[val] == 2:
                pair = val
            else:
                vals.append(val)
        assert len(vals) == 3
        vals.sort()
        vals.reverse()
        vals.insert(0, pair)
        return vals
    else:
        return 0  
    
    
def high_card(hand):
    return get_ordered_vals(hand)
    

def print_hand(hand):
    for card in hand:
        print card,
    print ""
    

hand_funcs = [royal_flush, straight_flush, four_kind, full_house, flush, straight, three_kind, two_pair, one_pair, high_card]
    
poker = open("54.txt")
ans = 0
for line in poker:
    cards = line.split()
    hand1 = []
    hand2 = []
    for item in cards[:5]:
        hand1.append(Card(item))
    for item in cards[5:]:
        hand2.append(Card(item))
    hand1.sort()
    hand2.sort()

    for func in hand_funcs:
        v1 = func(hand1)
        v2 = func(hand2)
        if v1 > v2:
            ans += 1
            '''print cards
            print func
            print v1, v2
            print "Winner: 1"'''
            break
        elif v2 > v1:
            '''print cards
            print func
            print v1, v2
            print "Winner: 2"'''
            break
print ans