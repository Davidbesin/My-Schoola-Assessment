from Planets import planets
import Lists


def get_planet_name(query):
    words = query.split()          

    for word in words:              
        cleaned = word.strip(".,?!:;\"'")
        for i in range(len(Lists.planet_names)):
            if cleaned.lower().capitalize() == Lists.planet_names[i]:
                return (Lists.planet_names[i])

    return None


def get_mass(query):
    q = query.lower()

    for phrase in Lists.mass_equivalent:
        if phrase in q:
            return True

    return False


def get_distance(query):
    q = query.lower()

    for phrase in Lists.distance_equivalent:
        if phrase in q:
            return True
        
    return False;    

def get_moons(query):
    q = query.lower()
    can_continue = False

    for phrase in Lists.moon_equivalent:
        if phrase in q:
            can_continue = True
            break

    if can_continue:
        return "moon" in q
    return False

""" def get_mooons_list(query):
    q = query.lower()
    can_continue = False

    for phrase in Lists.moon_equivalent:
        if phrase in q:
            can_continue = True
            break

    if can_continue:
        return "moons" in q
    return False """

def get_every_info(query):
    q = query.lower()

    for phrase in Lists.summary_equivalent:
        if phrase in q:
            return True
        
    return False; 

class QueryInfo:
    def __init__(self, query):
        self.query = query
        self.planet = get_planet_name(query)
        self.asks_mass = get_mass(query)
        self.asks_distance = get_distance(query)
        self.asks_moons = get_moons(query)
        self.ask_all_info = get_every_info(query)

    def get_answer(self):
        if not self.planet:
            return "I couldn't figure out which planet you're asking about."

        planet_obj = None
        for p in planets:
            if p.name == self.planet:
                planet_obj = p
                break

        if not planet_obj:
            return f"I don't have data for {self.planet}."

        wants_mass = self.asks_mass or self.ask_all_info
        wants_distance = self.asks_distance or self.ask_all_info
        wants_moons = self.asks_moons or self.ask_all_info

        if not (wants_mass or wants_distance or wants_moons):
            return f"I found {planet_obj.name}, but I'm not sure what you want to know about it."

        parts = []

        if wants_mass:
            parts.append(f"{planet_obj.name}'s mass is {planet_obj.mass} kg.")

        if wants_distance:
            parts.append(f"{planet_obj.name} is {planet_obj.distance} km from the Sun.")

        if wants_moons:
            if planet_obj.moons:
                moon_list = ", ".join(planet_obj.moons)
                parts.append(f"{planet_obj.name} has {len(planet_obj.moons)} major moon(s): {moon_list}.")
            else:
                parts.append(f"{planet_obj.name} has no major moons.")

        return " ".join(parts)