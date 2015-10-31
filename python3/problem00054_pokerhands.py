'''
In the card game poker, a hand consists of five cards and are ranked, from
lowest to highest, in the following way:

    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest
value wins; for example, a pair of eights beats a pair of fives. But if two
ranks tie, for example, both players have a pair of queens, then highest cards
in each hand are compared (see example 4 below); if the highest cards tie then
the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players.
Each line of the file contains ten cards (separated by a single space): the
first five are Player 1's cards and the last five are Player 2's cards. You can
assume that all hands are valid (no invalid characters or repeated cards), each
player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

ranking = 'edcba98765432 e5432'
mapping = str.maketrans("TJQKA", "abcde")
# reverse-sort-join helper
rsj = lambda g: ''.join(sorted(g, reverse=True))

def rank(string):
    values = string[::2].translate(mapping)
    suits = string[1::2]

    high_card       = ordering = rsj(values)
    one_pair        = rsj(i for i in set(values) if values.count(i)==2)
    two_pair        = one_pair if len(one_pair) == 2 else ''
    three_kind      = rsj(i for i in set(values) if values.count(i)==3)
    straight        = ordering if not one_pair and ordering in ranking else ''
    flush           = len(set(suits))==1
    full_house      = three_kind+one_pair if three_kind and one_pair else ''
    four_kind       = rsj(i for i in set(values) if values.count(i)==4)
    straight_flush  = ordering if straight and flush else ''
    royal_flush     = flush and ranking.startswith(ordering)

    return (royal_flush, straight_flush, four_kind, full_house,
            flush, straight, three_kind, two_pair, one_pair, high_card)


ans = 0
with open('../resources/p054_poker.txt') as fp:
    for string in fp.read().strip().replace(' ', '').split('\n'):
        ans += rank(string[:10]) > rank(string[10:])

print(ans)
