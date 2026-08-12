class Planet:
    def __init__(self, name, mass, distance, moons):
        self.name = name
        self.mass = mass          # in kg
        self.distance = distance  # avg distance to the sun, in km
        self.moons = moons        # major moon list

mercury = Planet("Mercury", 3.3011e23, 57.9e6, [])
venus   = Planet("Venus",   4.8675e24, 108.2e6, [])
earth   = Planet("Earth",   5.9724e24, 149.6e6, ["Moon"])
mars    = Planet("Mars",    6.4171e23, 227.9e6, ["Phobos", "Deimos"])
jupiter = Planet("Jupiter", 1.8982e27, 778.5e6, ["Io", "Europa", "Ganymede", "Callisto"])
saturn  = Planet("Saturn",  5.6834e26, 1433.5e6, ["Titan", "Rhea", "Iapetus", "Dione", "Tethys", "Enceladus", "Mimas"])
uranus  = Planet("Uranus",  8.6810e25, 2872.5e6, ["Titania", "Oberon", "Umbriel", "Ariel", "Miranda"])
neptune = Planet("Neptune", 1.02413e26, 4495.1e6, ["Triton"])

planets = [
    mercury,
    venus,
    earth,
    mars,
    jupiter,
    saturn,
    uranus,
    neptune
]