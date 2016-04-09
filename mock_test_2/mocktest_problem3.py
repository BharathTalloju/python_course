__author__ = 'Kalyan'

max_marks = 25

problem_notes = '''
You're given a text file containing names of movie actors and films they've acted in - delimited
by comma followed by space.

Format:
{actor name}, {movie name 1}, {movie name 2}, {movie name 3}

Input:
File containing movies info and a number 'n', which represents the number of lines from top of file.

Output:
For each actor in the first n lines, you must return the chemistry record with 
the co-actor with which they have most movies in common.

So you have to return a maximum of n records (if every actor has someone he has worked with in the records).
In the case where no actors have any common movies, you return 0 records.

Example:
if a1 and a2 have c1 as common movie
and a1 and a3 have c1, c2, c3
and a1 has no common movies with any other actor, then you must return [a1, a3, [c1, c2, c3]] as the
max chemistry record for a1.

If a given actor has same count of common movies with multiple co-actors, choose the
first one in alphabetical order.

If a given actor has no common movies with any other, then do not emit any chemistry record for that actor.

Notes:
1. See if you can decompose this problem into meaningful subroutines.
2. Submit the movies.txt file into dropbox too. ** Do not modify the movies.txt file! **

'''
import inspect
import os

# represents the chemistry between two actors and the common movies between them.
# movies is a set of common movies, the actor and co_actor are name strings
class Chemistry(object):
    def __init__(self, actor, co_actor, movies):
        if not actor: raise ValueError("actor is not valid name")
        if not co_actor: raise ValueError("co-actor is not valid name")

        self.actor = actor
        self.co_actor = co_actor
        self.movies = movies

    def __hash__(self):
        return hash(self.actor)

    def __eq__(self, other):
        return (self.actor == other.actor) \
               and (self.co_actor == other.co_actor) \
               and (self.movies == other.movies)

    def __repr__(self):
        return str((self.actor, self.co_actor, self.movies))


# returns a set of Chemistry objects that represent the max chemistry of each actor.
# It is as if the file has only first n lines.
# Important: Use the helper routine given (open_input_file) to open the file to open the file which should
# be in same directory as this file.
def actors_chemistry(input_file, n):
    f = open_input_file(input_file)
    chemistry_list = []
    movies_dict = dict()
    for x in xrange(n):
        line = f.readline().strip().split(", ")
        actor = line[0]
        movies_dict[actor] = set(line[1:])

    for actor1 in movies_dict:
        max = set()
        best_buddy = None
        for actor2 in movies_dict:
            if actor1 == actor2:
                continue
            common_movies = movies_dict[actor1] & movies_dict[actor2]
            if common_movies == set():
                continue
            if len(common_movies) > len(max):
                print actor1, "and", actor2, "have", common_movies
                best_buddy = actor2
                max = common_movies
            elif len(common_movies) == len(max):
                if len(common_movies) == 0:
                    continue
                if best_buddy[0] > actor2[0]:
                    best_buddy = actor2
                    max = common_movies
        if best_buddy is not None:
            print actor1, "and", actor2, "have", common_movies
            chemistry_list.append(Chemistry(actor1, best_buddy, max ))
            chemistry_list.append(Chemistry(best_buddy, actor1, max))
    return set(chemistry_list)



def test_actors_chemistry():
    assert {Chemistry('Leonardo Di Caprio', 'Tom Hardy', {'Inception', 'The Revenant'}),
            Chemistry('Tom Hardy', 'Leonardo Di Caprio', {'Inception', 'The Revenant'})} == actors_chemistry('movies.txt', 5)
    assert {Chemistry('Leonardo Di Caprio', 'Tom Hardy', {'Inception', 'The Revenant'}),
            Chemistry('Tom Hardy', 'Leonardo Di Caprio', {'Inception', 'The Revenant'}),
            Chemistry('Sylvester Stallone', 'Julianne Moore', {'Assassins'}),
            Chemistry('Julianne Moore', 'Sylvester Stallone', {'Assassins'})} == actors_chemistry('movies.txt', 6)
    assert {Chemistry('Leonardo Di Caprio', 'Tom Hardy', {'Inception', 'The Revenant'}),
            Chemistry('Tom Hardy', 'Leonardo Di Caprio', {'Inception', 'The Revenant'}),
            Chemistry('Sylvester Stallone', 'Julianne Moore', {'Assassins'}),
            Chemistry('Julianne Moore', 'Sylvester Stallone', {'Assassins'}),
            Chemistry('Tim Roth', 'Bruce Willis', {'Pulp Fiction'}),
            Chemistry('Bruce Willis', 'Tim Roth', {'Pulp Fiction'})} == actors_chemistry('movies.txt', 7)
    assert {Chemistry('Leonardo Di Caprio', 'Tom Hardy', {'Inception', 'The Revenant'}),
            Chemistry('Tom Hardy', 'Leonardo Di Caprio', {'Inception', 'The Revenant'}),
            Chemistry('Sylvester Stallone', 'Julianne Moore', {'Assassins'}),
            Chemistry('Julianne Moore', 'Sylvester Stallone', {'Assassins'}),
            Chemistry('Tim Roth', 'Michael Madsen', {'Reservoir Dogs','The Hateful Eight'}),
            Chemistry('Bruce Willis', 'Tim Roth', {'Pulp Fiction'}),
            Chemistry('Michael Madsen', 'Tim Roth', {'Reservoir Dogs','The Hateful Eight'})} == actors_chemistry('movies.txt', 8)

def get_module_dir():
    mod_file = inspect.getfile(inspect.currentframe())
    mod_dir = os.path.dirname(mod_file)
    return mod_dir


def open_input_file(file, mode="rt"):
    mod_dir = get_module_dir()
    test_file = os.path.join(mod_dir, file)
    return open(test_file, mode)
