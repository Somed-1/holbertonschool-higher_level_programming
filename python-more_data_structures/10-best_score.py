#!/usr/bin/python3
def best_score(a_dicitionary):
    return max(a_dicitionary, key=a_dicitionary.get) if a_dicitionary else None
