#4
def unique_cities(cities):
    result = set()
    for city in cities:
        clean = city.strip().casefold()
        if clean == "":
            continue
        result.add(clean)
    return result
#5
def attendance(roster, present):
    set_roster = set(roster)
    set_present = set(present)
    attended = set_roster & set_present
    absent = set_roster - set_present
    guests = set_present - set_roster
    return {"attended": attended, "absent": absent, "guests": guests}
#6
def compare_checks(before, after):
    set_before = set(before)
    set_after = set(after)
    added = set_after - set_before
    removed = set_before - set_after
    common = set_before & set_after
    return {"added": added, "removed": removed, "common": common}
#7
def can_run(required, available):
    return required.issubset(available)
#8
def duplicate_ids(ids):
    seen = set()
    repeated = set()
    for id in ids:
        if id in seen:
            repeated.add(id)
        seen.add(id)
    return repeated
#9
def unique_in_order(values):
    seen = set()
    result = []
    for value in values:
        if value not in seen:
            result.append(value)
        seen.add(value)
    return result