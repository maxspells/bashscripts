# Saving the updated simulation code into a reusable format for a persistent loop

import random
import time

# Define constants
NAMES = ["Vega", "Talon", "Milo", "Orion", "Rex", "Juno", "Zara", "Lyra", "Cass", "Nova"]
ROLES = ["Pilot", "Engineer", "Scientist", "Medic", "Security"]
PERSONALITIES = ["Friendly", "Hotheaded", "Shy", "Brave", "Paranoid"]
QUIRKS = ["Sleepwalker", "Prankster", "Neat Freak", "Germaphobe", "Loud"]
DESIRES = ["Explore", "Make friends", "Prove self", "Avoid conflict", "Control things"]
TASKS = ["Analyze data", "Check systems", "Rest in quarters", "Repair hull", "Chat in mess hall"]

# CrewMember class
class CrewMember:
    def __init__(self, name, role, personality, quirk, desire):
        self.name = name
        self.role = role
        self.personality = personality
        self.quirk = quirk
        self.desire = desire
        self.relationships = {}
        self.state = "idle"

    def choose_task(self):
        if self.desire == "Explore":
            return random.choice(["Analyze data", "Check systems"])
        elif self.desire == "Make friends":
            return "Chat in mess hall"
        elif self.desire == "Prove self":
            return random.choice(["Repair hull", "Check systems"])
        elif self.desire == "Avoid conflict":
            return "Rest in quarters"
        elif self.desire == "Control things":
            return "Check systems"
        else:
            return random.choice(TASKS)

    def interact(self, other):
        if other.name not in self.relationships:
            self.relationships[other.name] = 0
        if self.name not in other.relationships:
            other.relationships[self.name] = 0

        score = 0
        if self.personality == "Friendly":
            score += 2
        if self.personality == "Hotheaded":
            score -= 2
        if self.quirk == "Prankster" and other.quirk == "Germaphobe":
            score -= 3
        if self.desire == "Make friends":
            score += 1
        if self.personality == other.personality:
            score += 1

        self.relationships[other.name] += score
        other.relationships[self.name] += score

        if score > 1:
            print(f"{self.name} and {other.name} had a great chat! (+{score})")
        elif score < -1:
            print(f"{self.name} and {other.name} got into an argument! ({score})")
        else:
            print(f"{self.name} and {other.name} had a neutral chat. ({score})")

    def perform_turn(self, crew):
        task = self.choose_task()
        self.state = task
        print(f"{self.name} is doing task: {task}")
        if task == "Chat in mess hall":
            other = random.choice([c for c in crew if c.name != self.name])
            self.interact(other)

# Function to create crew
def create_crew():
    random.shuffle(NAMES)
    return [CrewMember(
        name=NAMES[i],
        role=random.choice(ROLES),
        personality=random.choice(PERSONALITIES),
        quirk=random.choice(QUIRKS),
        desire=random.choice(DESIRES)
    ) for i in range(10)]

# Function to run the simulation for a given number of days
def run_simulation(crew, days=10, pause=1):
    for day in range(1, days + 1):
        print(f"\n=== Day {day} on the Ship ===")
        for member in crew:
            member.perform_turn(crew)
        time.sleep(pause)  # simulate real-time delay

    print("\n=== Final Relationship Scores ===")
    for member in crew:
        print(f"{member.name}'s relationships:")
        for other, score in member.relationships.items():
            print(f"  with {other}: {score}")

# Create crew and run persistent simulation loop (e.g., 10 days with 1s pause)
crew = create_crew()
run_simulation(crew, days=10, pause=0.5)

