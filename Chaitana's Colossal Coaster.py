"""Functions to manage and organize queues at Chaitana's roller coaster."""


def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):

    if ticket_type >= 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue

def find_my_friend(queue, friend_name):

    index = queue.index(friend_name)
    return index

def add_me_with_my_friends(queue, index, person_name):

    queue.insert(index, person_name)
    return queue
    
def remove_the_mean_person(queue, person_name):

    queue.remove(person_name)
    return queue


def how_many_namefellows(queue, person_name):

    return queue.count(person_name)

def remove_the_last_person(queue):
    return queue[-1]


def sorted_names(queue):
    return sorted(queue)


# to print out the return value.

add_me = add_me_to_the_queue(['Tony', 'Bruce'], ['RobotGuy', 'WW'], 0, 'HawkEye')
find_friend = find_my_friend(['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 'Natasha')
add_me_with_friend = add_me_with_my_friends(['Natasha', 'Steve', 'Tchalla', 'Wanda', 'Rocket'], 0, 'Bucky')
remove_person = remove_the_mean_person(['Natasha', 'Steve', 'Ultron', 'Wanda', 'Rocket'], 'Ultron')
times_name_appars = how_many_namefellows(['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'], 'Bucky')
remove_last = remove_the_last_person(['Natasha', 'Steve', 'Ultron', 'Natasha', 'Rocket'])
sort_queue = sorted_names(['Steve', 'Ultron', 'Natasha', 'Rocket'])


# Output
print('| Add a person to queue:', add_me, 
      '| find person in queue:', find_friend, 
      '| Add person with friend to the queue:', add_me_with_friend, 
      '| removed person from queue:', remove_person, 
      '| how many times the name appears:', times_name_appars, 
      '| removed last person fromq queue:', remove_last,
      '| sort the queue:', sort_queue,)

