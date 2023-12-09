SEEDS = "seeds"
SEED_TO_SOIL = "seed_to_soil"
SOIL_TO_FERTILIZER = "soil_to_fertilizer"
FERTILIZER_TO_WATER = "fertilizer_to_water"
WATER_TO_LIGHT = "water_to_light"
LIGHT_TO_TEMPERATURE = "light_to_temperature"
TEMPERATURE_TO_HUMIDITY = "temperature_to_humidity"
HUMIDITY_TO_LOCATION = "humidity_to_location"

ALMANAC_KEYS = {
    0: SEEDS,
    1: SEED_TO_SOIL,
    2: SOIL_TO_FERTILIZER,
    3: FERTILIZER_TO_WATER,
    4: WATER_TO_LIGHT,
    5: LIGHT_TO_TEMPERATURE,
    6: TEMPERATURE_TO_HUMIDITY,
    7: HUMIDITY_TO_LOCATION,
}


def get_data():
    almanac = {}

    with open("input.txt") as f:
        for key_id, data in enumerate(f.read().split("\n\n")):
            key = ALMANAC_KEYS[key_id]
            almanac[key] = []

            for line in data.split("\n")[1:]:
                values = [int(number) for number in line.split(" ")]

                if key == SEEDS:
                    almanac[key] = values
                else:
                    destination_start, source_start, length = values[0], values[1], values[2]
                    source_end = source_start + length
                    almanac[key].append((source_start, source_end, destination_start))

    return almanac


def convert(value, mapping):
    for source_start, source_end, destination_start in mapping:
        if value >= source_start and value <= source_end:
            return destination_start + (value - source_start)

    return value


def solve(part2=False):
    almanac = get_data()
    locations = []
    
    seeds = almanac[SEEDS]

    for seed in seeds:
        for key_id in range(1, len(ALMANAC_KEYS)):
            seed = convert(seed, almanac[ALMANAC_KEYS[key_id]])
            print(seed)

        locations.append(seed)

    return min(locations)


if __name__ == "__main__":
    print("Answer Task 1: {}".format(solve()))
    print("Answer Task 2: {}".format(solve(part2=True)))
