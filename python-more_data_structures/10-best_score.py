#!/usr/bin/python3
def best_score(a_dicitionary):
    return max(a_dicitionary.items())[0] if a_dicitionary else None


a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))
