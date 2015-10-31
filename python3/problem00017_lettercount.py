'''
If the numbers 1 to 5 are written out in words:

    one, two, three, four, five,

then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. 342 (three hundred and forty-two) contains
23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
"and" when writing out numbers is in compliance with British usage.
'''

dictionary = {0: ''}

dictionary.update({i: s for i, s in enumerate('''
one two three four five six seven eight nine ten eleven twelve thirteen
fourteen fifteen sixteen seventeen eighteen nineteen
'''.split(), 1)})

dictionary.update({10*i: s for i, s in enumerate('''
twenty thirty forty fifty sixty seventy eighty ninety
'''.split(), 2)})

def humanize(n):
    M, C, X, I = [int(d) for d in str(n).zfill(4)]
    string = dictionary[X*10+I] if X<2 else dictionary[X*10]+dictionary[I]
    if string and C: string = 'and' + string
    if C: string = dictionary[C]+'hundred' + string
    if M: string = dictionary[M]+'thousand' + string
    return string

ans = sum(len(humanize(n)) for n in range(1, 1001))
print(ans)
