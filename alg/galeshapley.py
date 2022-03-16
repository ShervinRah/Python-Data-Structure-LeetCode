'''
Dictionary

py_dict = { key1: 'value1', key2: 'value2', key3: 'value3', .... keyN: 'valueN'


'''

import collections

# The women that men prefer
preferred_ranking_men = {
    'ryan': ['lizzy', 'sarah', 'zoey', 'daniella'],
    'josh': ['sarah', 'lizzy', 'daniella', 'zoey'],
    'blake': ['sarah', 'daniella', 'zoey', 'lizzy'],
    'connor': ['lizzy', 'sarah', 'zoey', 'daniella']
}

# The men that the women prefer
preferred_rankings_women = {
    'lizzy': ['ryan', 'blake', 'josh', 'connor'],
    'sarah': ['ryan', 'blake', 'connor', 'josh'],
    'zoey': ['connor', 'josh', 'ryan', 'blake'],
    'daniella': ['ryan', 'josh', 'connor', 'blake']
}

# Keeps track of the people that "may" end up together
temp_engagements = []
# List of men who are free
free_men = []


# For loop to store keys of preferred_ranking_men to free_men = []
# append() -> this method adds an element to free_men list

def init_free_men():
    for man in preferred_ranking_men:
        free_men.append(man)


# while list is not empty go through each man and call matching function
def stable_matching():
    while len(free_men) > 0:
        for man in free_men:
            begin_matching(man)


# %s format for string, %d format for numbers
# taken_match = [couple for couple in temp_engagements if woman in couple]
def begin_matching(man):
    print('Dealing with %s' % man)
    for woman in preferred_ranking_men[man]:

        taken_match = []

        for couple in temp_engagements:
            if woman in couple:
                taken_match.append(couple)

        if len(taken_match) == 0:
            temp_engagements.append([man, woman])
            free_men.remove(man)
            print('%s is no longer a free man and is temporarily engaged to %s ' % (man, woman))
            break
        elif len(taken_match) > 0:
            print('%s is taken already ... ' % woman)

            current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            if current_guy < potential_guy:
                print('She is satisfied with %s... ' % (taken_match[0][0]))
            else:
                print('%s is better than %s' % (man, taken_match[0][0]))
                print('Making %s free again... and then temporarily accept dance between %s and %s ' % (
                    taken_match[0][0], man, woman))

                free_men.remove(man)

                free_men.append(taken_match[0][0])

                taken_match[0][0] = man
                break


def main():
    init_free_men()
    stable_matching()

    print('COMPLETE LIST OF DANCE ACCEPTANCES')
    print(temp_engagements)


if __name__ == "__main__":
    main()
