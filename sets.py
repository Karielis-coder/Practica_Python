def remove_duplicae(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def with_set(some_list):
    return list(set(some_list))

def run():
    random_list=[1, 2, 2, 4, 1, 4, 5, 4, 6, 8, 7, 2, 5, 4, 6, 8, 2, 1, 3]
    print(remove_duplicae(random_list))
    print(with_set(random_list))



if __name__ == '__main__':
    run()