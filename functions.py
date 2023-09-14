def print_my_name(name):
    print(name)

print_my_name('Bob')

def trip_planner(start, end, duration, mode):
    print(f"It looks like you're starting your trip to {start}")
    print(f"You are planning to get to {end}")
    print(f"It should take about {duration} hours")
    print(f"I see you are taking a {mode}")

trip_planner('paradigm', 'CheeseLand', 2, 'plane')