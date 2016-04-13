__author__ = 'Kalyan'

problem = """
 We are going to revisit unit4 assignment2 for this problem.

 Given an input file of words (mixed case). Group those words into anagram groups and write them
 into the destination file so that words in larger anagram groups come before words in smaller anagram sets.

 With in an anagram group, order them in case insensitive ascending sorting order.

 If 2 anagram groups have same count, then set with smaller starting word comes first.

 For e.g. if source contains (ant, Tan, cat, TAC, Act, bat, Tab), the anagram groups are (ant, Tan), (bat, Tab)
 and (Act, cat, TAC) and destination should contain Act, cat, TAC, ant, Tan, bat, Tab (one word in each line).
 the (ant, Tan) set comes before (bat, Tab) as ant < bat.

 At first sight, this looks like a big problem, but you can decompose into smaller problems and crack each one.

 This program should be written as a command line script. It takes one argument the input file of words and outputs
 <input>-results.txt where <input>.txt is the input file of words.
"""
import sys
import string




def anagrams(source, destination):
    source = open(source)
    words_list = read_words(source)

    anagrams_list = get_anagrams_list(words_list)

    for group in anagrams_list:
        group.sort(key = string.lower)

    anagrams_list.sort(key = lambda e: (len(e), min(e)))

    source.close()

    destination = open(destination, "w")
    for group in anagrams_list:
        for word in group:
            destination.write(word+'\n')


def read_words(source):
    words_list = [x.strip() for x in source.readlines()]
    words_list = [x for x in words_list if len(x) != 0 and x[0] != '#' ]
    return words_list

def get_anagrams_list(words_list):

    anagram_list = []
    completed = []
    for i in xrange(len(words_list)):
        completed.append(False)

    for i in xrange(len(words_list)):
        anagram_group = [words_list[i]]
        completed[i] = True
        for x in xrange(len(words_list)):
            if not completed[x]:
                if (set(words_list[i]) - set(words_list[x])) == set():
                    anagram_group.append(words_list[x])
                    completed[x] = True
        anagram_list.append(anagram_group)

    return anagram_list

if len(sys.argv) == 2:
    anagrams(sys.argv[1], str(sys.argv[1][:-4])+"-results.txt")
else:
    print "Invalid arguments"

if __name__ == "__main__":
    pass
    #sys.exit(main())