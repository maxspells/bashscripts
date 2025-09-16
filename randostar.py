import random

# --- FACTION SETUP ---
class Faction:
    def __init__(self, name, government, ideology, power_level):
        self.name = name
        self.government = government
        self.ideology = ideology
        self.power_level = power_level

    def __str__(self):
        return f"{self.name} ({self.government}, Power: {self.power_level}) - {self.ideology}"

# Sample faction data
FACTION_NAMES = [
    "Zentar Hegemony", "Sable Concordat", "Azure Collective", "Dominion of Vesk",
    "Nova Trade League", "Crimson Ascendancy", "Holy Synod of Kaarn"
]

GOVERNMENTS = ["Autocracy", "Republic", "Theocracy", "Corporate State", "Technocracy", "Feudal Union"]
IDEOLOGIES = [
    "Expansionist and militaristic",
    "Peaceful but technologically dominant",
    "Believes in divine right to rule",
    "Profit-driven and manipulative",
    "Seeks to uplift primitive worlds",
    "Isolationist and xenophobic"
]

def generate_factions(n=4):
    factions = []
    for _ in range(n):
        name = random.choice(FACTION_NAMES)
        FACTION_NAMES.remove(name)  # Avoid duplicates
        gov = random.choice(GOVERNMENTS)
        idea = random.choice(IDEOLOGIES)
        power = random.randint(1, 10)
        factions.append(Faction(name, gov, idea, power))
    return factions

# --- PLANET, STAR, SECTOR SETUP ---
planet_types = ['rocky', 'gas giant', 'ice', 'ocean', 'desert', 'jungle', 'lava']
planet_descriptions = {
    'rocky': 'A solid planet with mountainous terrain.',
    'gas giant': 'A massive planet with thick clouds and storms.',
    'ice': 'A frigid world of glaciers and frozen oceans.',
    'ocean': 'A planet covered in endless water.',
    'desert': 'A dry, arid world with little vegetation.',
    'jungle': 'A lush, verdant planet teeming with life.',
    'lava': 'A volcanic world with rivers of molten rock.'
}

class Planet:
    def __init__(self, name, planet_type, description, faction=None):
        self.name = name
        self.planet_type = planet_type
        self.description = description
        self.faction = faction

    def __str__(self):
        faction_info = f" Controlled by: {self.faction.name}" if self.faction else ""
        return f"    {self.name} ({self.planet_type}): {self.description}{faction_info}"

class Star:
    def __init__(self, name, x, y, planets):
        self.name = name
        self.x = x
        self.y = y
        self.planets = planets

    def __str__(self):
        return f"Star: {self.name} at ({self.x}, {self.y})\n" + "\n".join(str(p) for p in self.planets)

def generate_star_name():
    syllables = ["Al", "Be", "Cor", "Dra", "El", "Fa", "Gor", "He", "Ix", "Jo", "Ka", "Lu", "My", "Nu", "Or", "Pi", "Qua", "Ra", "Sa", "Tu", "Ur", "Va", "Xe", "Yo", "Za"]
    return random.choice(syllables) + random.choice(syllables) + random.choice(syllables)

def generate_planet_name(star_name, index):
    return f"{star_name}-{index + 1}"

def generate_sector(width, height, factions):
    sector = []
    for _ in range(width * height):
        if random.random() < 0.1:  # 10% chance a star is present
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            star_name = generate_star_name()
            num_planets = random.randint(1, 8)
            planets = []

            for i in range(num_planets):
                planet_type = random.choice(planet_types)
                description = planet_descriptions[planet_type]
                planet_name = generate_planet_name(star_name, i)

                # 30% chance planet is controlled by a faction
                faction = random.choice(factions) if random.random() < 0.3 else None
                planets.append(Planet(planet_name, planet_type, description, faction))

            sector.append(Star(star_name, x, y, planets))
    return sector

# --- GENERATE EVERYTHING ---
factions = generate_factions(7)
sector = generate_sector(20, 20, factions)

# Print factions
print("=== FACTIONS ===")
for faction in factions:
    print(f"- {faction}")

# Print sector
print("\n=== STAR SYSTEMS ===")
for star in sector:
    print(star)
    print()
