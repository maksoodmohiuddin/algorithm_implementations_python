class Sudoku():
    def __init__(self):
        #self.row =
        self.grids = [[None] * 9] * 9
        self.number = [[1, 2, 3, 4, 5, 6, 2]]


s = Sudoku()
#t = s.grids[0][0]
#print t

dict = {'a': 1, 'b': 2}
dict['c'] = 10
dict['d'] = 20

for key, value in dict.iteritems():
    print key
    print value


#IsSudokuValid(s.grids)

second = set(sorted(s.number[0]))

classes = [1, 1, 0, 0, 1, 2, 0]

ones = [x for x in classes if x == 1]
print ones

#for s in second:
#    if s == 1:
#        print 100
#    elif s == 7:
#	    #continue
#    else:
#        #print s

sentence = 'It is raining cats and dogs'

#print sentence.split()

#print map(lambda word: word + "Test", sentence.split())


a = 10
b = float(a)
c = str(a)
d = "20"
e = int(d)
#print a
#print b
#print c
#print d
#print e


g = lambda x: x * 2

print g(2)


