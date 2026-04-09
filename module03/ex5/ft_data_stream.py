import random

def gen_event():
    """
    Infinite generator as defined in the exercise.
    Returns (name, action) tuples.
    """
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))

def consume_event(event_list):
    """
    Generator that consumes a list by randomly picking and removing items.
    """
    while event_list:
        event = random.choice(event_list)
        # Note: remove() removes the first occurrence. 
        # Since events can be identical, we use index-based removal or 
        # rely on the fact that removing one instance satisfies the requirement.
        event_list.remove(event)
        yield event

def main():
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()
    
    # Execute loop a thousand times as requested
    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    # Build list of 10 events
    ten_events = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    # Consume events directly in for .. in construct
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")

if __name__ == "__main__":
    main()
