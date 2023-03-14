def badge_maker(name):
    badge = (f"Hello, my name is {name}.")
    return badge

def batch_badge_creator(names):
    badge_batch = []
    for name in names:
        badge_batch.append(f"Hello, my name is {name}.")
    return badge_batch

def assign_rooms(names):
    badge_rooms = []
    int=1
    for name in names:
        badge_rooms.append(f"Hello, {name}! You'll be assigned to room {int}!")
        int += 1
    return badge_rooms

def printer(names):
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)