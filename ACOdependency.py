import random
import math
import copy
from random import uniform, randint, shuffle, sample
def encoding_population(initial_population):
    dict = {
        'a' : 0,
        'c' : 1,
        'g' : 2,
        't' : 3
    }
    l=[]
    for i in initial_population:
        k=''
        for j in i:
            k+=str(dict[j])
        l.append(k)
    return l

def insert_symbol(src_string, inserted_string, pos):
    """
    Insert the inserted_string into the src_string at the specified position.

    Parameters:
    - src_string (str): The source string where the insertion will occur.
    - inserted_string (str): The string to be inserted.
    - pos (int): The position at which the inserted_string will be inserted.

    Returns:
    - str: The resulting string after insertion.
    """
    return ''.join(src_string[:pos] + inserted_string + src_string[pos:])


def supersequence_generate(set_of_strings):
    """
    Generate a supersequence from a set of strings using random insertions.

    Parameters:
    - set_of_strings (list): A list of strings to be combined into a supersequence.

    Returns:
    - str: The generated supersequence.
    """
    copied_set_of_strings = copy.deepcopy(set_of_strings)
    supersequence = ''.join(copied_set_of_strings.pop(random.randint(0, len(set_of_strings) - 1)))

    for i in range(len(copied_set_of_strings)):
        counter = 0
        for j in copied_set_of_strings[i]:
            inserted_pos = random.randint(counter, len(supersequence))

            if inserted_pos == len(supersequence) or j != supersequence[inserted_pos]:
                supersequence = insert_symbol(supersequence, j, inserted_pos)
            counter = inserted_pos + 1

    return supersequence


def population_generation(pop_size, set_of_strings):
    """
    Generate a population of supersequences.

    Parameters:
    - pop_size (int): The size of the population.
    - set_of_strings (list): A list of strings to be combined into supersequences.

    Returns:
    - list: A list of generated supersequences.
    """
    population = []

    while len(population) < pop_size:
        population.append(supersequence_generate(set_of_strings))

    return population
