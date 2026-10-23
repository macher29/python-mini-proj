To_do_things = ["Gaming" , "Playing" , "Programming" , "Studying" , "Workout"]

def add(thing):
    To_do_things.append(thing)
    print(" ")
    print(f"{thing} is added in your to do list")
    print(" ")
    print(f"Update to do list: {To_do_things}")
    print(" ")

def remove(work):
    To_do_things.remove(work)
    print(" ")
    print(f"{work} is Removed from your to do list")
    print(" ")
    print(f"Update to do list: {To_do_things}")
    print(" ")

def show_list():
    print(" ")
    print(To_do_things)
    print(" ")











