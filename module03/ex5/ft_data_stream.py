import random


def gen_event():
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim", "use", "release"]
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(event_list):
    while event_list:
        event = random.choice(event_list)
        event_list.remove(event)
        yield event


def main():
    print("=== Game Data Stream Processor ===")
    event_gen = gen_event()

    for i in range(1000):
        name, action = next(event_gen)
        print(f"Event {i}: Player {name} did action {action}")

    ten_events = [next(event_gen) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
