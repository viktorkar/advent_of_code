from time import time

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


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Function {func.__name__!r} executed in {(t2 - t1):.4f}s")
        return result

    return wrap_func


def get_data():
    almanac = {}

    with open("input.txt") as f:
        for key_id, data in enumerate(f.read().split("\n\n")):
            key = ALMANAC_KEYS[key_id]
            almanac[key] = []

            for line in data.split("\n")[1:]:
                values = [int(number) for number in line.split(" ")]

                if key == SEEDS:
                    almanac[key] = [(x, x + y) for x, y in zip(values[::2], values[1::2])]
                else:
                    destination_start, source_start, length = values[0], values[1], values[2]
                    source_end = source_start + length
                    almanac[key].append((source_start, source_end, destination_start))

            almanac[key].sort(key=lambda tup: tup[0])

    return almanac


def convert(ranges, mapping):
    new_ranges = []

    for m_s1, m_s2, m_d in mapping:
        kept_ranges = []

        while ranges:
            (r_s, r_e) = ranges.pop()

            before = (r_s, min(r_e, m_s1))
            inter = (max(r_s, m_s1), min(r_e, m_s2))
            after = (max(m_s2, r_s), r_e)

            # If a part of the range is before the mapping starts, keep that part as it is
            if before[1] > before[0]:
                kept_ranges.append(before)

            # If a part of the range intersects, convert that part to the new range and save it
            if inter[1] > inter[0]:
                new_ranges.append((inter[0] - m_s1 + m_d, inter[1] - m_s1 + m_d))

            # If a part of the range is after the mapping ends, keep that part as it is
            if after[1] > after[0]:
                kept_ranges.append(after)

        ranges = kept_ranges

    return new_ranges + ranges


@timer_func
def solve():
    almanac = get_data()
    seed_ranges = almanac[SEEDS]

    for key_id in range(1, len(ALMANAC_KEYS)):
        seed_ranges = convert(seed_ranges, almanac[ALMANAC_KEYS[key_id]])

    return min(seed_ranges, key=lambda tup: tup[0])[0]


if __name__ == "__main__":
    print("Answer Task 2: {}".format(solve()))