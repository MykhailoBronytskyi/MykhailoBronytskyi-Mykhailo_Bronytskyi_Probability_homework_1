'''Module for compearing sort algorithms'''
from time import time
import random

global NUM_OF_COMPARES
NUM_OF_COMPARES = 0

def selection_sort(some_list):
    '''Selection sort'''
    length = len(some_list)

    for i in range(length-1):
        place = i
        for j in range(i, length):
            
            global NUM_OF_COMPARES
            NUM_OF_COMPARES += 1
            if some_list[j] < some_list[place]:
                place = j

        some_list[i], some_list[place] = some_list[place], some_list[i]
    return some_list


def insertion_sort(some_list):
    length = len(some_list)

    for idx in range(1, length):
        pos = idx - 1
        val = some_list[idx]

        global NUM_OF_COMPARES
        NUM_OF_COMPARES += 1
        while pos > -1 and some_list[pos] > val:
            some_list[pos+1] = some_list[pos]
            pos -= 1

            
            NUM_OF_COMPARES += 1

        some_list[pos+1] = val
    return some_list


def merge(list_1, list_2) -> list:
    pos_1 = 0
    pos_2 = 0
    new_list = []
    while pos_1 != len(list_1) or pos_2 != len(list_2):

        global NUM_OF_COMPARES
        NUM_OF_COMPARES += 4

        if (len(list_1) == pos_1) or (len(list_2) != pos_2) and (list_1[pos_1] > list_2[pos_2]):
            new_list.append(list_2[pos_2])
            pos_2 += 1

        else:
            new_list.append(list_1[pos_1])
            pos_1 += 1

    return new_list


def merge_sort(some_list):

    if len(some_list) <= 1:
        return some_list

    middle = len(some_list)//2
    left = some_list[:middle]
    right = some_list[middle:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def shell_sort(some_list):
    length = len(some_list)
    step = 1
    
    while step < length // 3:
        step = step * 3 + 1   

    while step > 0:

        for idx in range(step, length):

            pointer = idx - step
            value = some_list[idx]

            global NUM_OF_COMPARES
            NUM_OF_COMPARES += 1
            while (pointer > -1) and (some_list[pointer] > value):

                NUM_OF_COMPARES += 1

                some_list[pointer + step] = some_list[pointer]
                pointer -= step
            some_list[pointer + step] = value

        step //= 3

    return some_list


def compare_sort_algorithms():
    '''The function to compare 4 sorting algorithms
    in various situations on lists of different size. 

    Write information about time complexity and number
    of comperisons to a file.'''

    def ascending_order(the_range: int):
        '''Create a list with values in ascending order'''
        return [num for num in range(the_range)]

    def descending_order(the_range: int):
        '''Create a list with values in descending order'''
        return [the_range - num for num in range(the_range)]

    def random_values(the_range: int):
        '''Create a list with random values'''
        return [random.randrange(the_range) for num in range(the_range)]

    def only_1_2_3(the_range: int):
        '''Create a list with values: 1, 2, 3 in random order'''
        return [random.choice([1,2,3]) for num in range(the_range)]
    


    all_algorithms = {'Selection_sort' : selection_sort, 'Insertion_sort' : insertion_sort,
                                       'Merge_sort' : merge_sort,'Shell_sort' : shell_sort}

    four_experiments = { ascending_order: 1, descending_order: 1, random_values: 5, only_1_2_3: 3}

    with open('FILE_WITH_STATISTICCS_ON_SORTING_ALGORITMS_5', 'a') as file:

        for list_type, num_of_repets in four_experiments.items():

            file.write(f'{list_type.__name__.capitalize()}\n\n')
            print(f'\n{list_type.__name__.capitalize()} ')

            experiment_results = {}
            for name_of_algorithm, sort_algorithm in all_algorithms.items():

                random.seed = 7 
                # file.write(f'\n{name_of_algorithm} ')
                print(f'\n{name_of_algorithm}\n')

                experiment_results[name_of_algorithm] = []
                for power in range(7, 16):

                    global NUM_OF_COMPARES
                    NUM_OF_COMPARES = 0
                    
                    sum_time = 0

                    for repeat in range(num_of_repets):

                        the_list = list_type(2 ** power)

                        now = time()
                        sort_algorithm(the_list)
                        sum_time += time() - now
                    
                    experiment_results[name_of_algorithm].append((f' {sum_time/num_of_repets:8.7f} ', f' {NUM_OF_COMPARES/num_of_repets:.0f} '))



                    # file.write(f'2^{power:2.0f} list: {sum_time/num_of_repets:8.7f} (sec) compares: {NUM_OF_COMPARES/num_of_repets:.0f}\n')
                    print(f'2^{power:2.0f} list: {sum_time/num_of_repets:8.7f} (sec) compares: {NUM_OF_COMPARES/num_of_repets:.0f}')
            

            for algorithm in experiment_results:

                file.write(f'{algorithm} ')

                for the_time in experiment_results[algorithm]:
                    file.write(f'{str(the_time[0]).replace("." , ",")} ')
                file.write('\n')
            
            file.write('\n')

            for algorithm in experiment_results:

                file.write(f'{algorithm} ')

                for num_of_comperisons in experiment_results[algorithm]:
                    file.write(f'{str(num_of_comperisons[1]).replace("." , ",")} ')
                file.write('\n')
            file.write('\n')

if __name__=='__main__':

    compare_sort_algorithms()
    # with open('FILE_WITH_STATISTICCS_ON_SORTING_ALGORITMS.txt', 'a') as file:
    #     file.write('hello world of file')
    # print(f'time for 2^{10} list: {12.345:10.0f} compares: {100.10:100.0f}')
