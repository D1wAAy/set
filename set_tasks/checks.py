from set_tasks import (
    unique_cities,
    attendance,
    compare_checks,
    can_run,
    duplicate_ids,
    unique_in_order,
)
# 4.
def check_unique_cities():
    cities = [" Алматы ", "алматы", "Астана", "", " "]
    cities_copy = cities.copy()
    assert unique_cities(cities) == {"алматы", "астана"}
    assert cities == cities_copy
    result = unique_cities([])
    assert result == set()
    assert isinstance(result, set)
    assert unique_cities(["", "   "]) == set()
# 5.
def check_attendance():
    roster = ["Айдар", "Алина", "Данияр", "Мадина"]
    present = ["Алина", "Данияр", "Данияр", "Ерлан"]
    roster_copy = roster.copy()
    present_copy = present.copy()
    result = attendance(roster, present)
    assert result["attended"] == {"Алина", "Данияр"}
    assert result["absent"] == {"Айдар", "Мадина"}
    assert result["guests"] == {"Ерлан"}
    assert roster == roster_copy
    assert present == present_copy
    assert attendance([], []) == {
        "attended": set(),
        "absent": set(),
        "guests": set(),
    }
    assert attendance(["Айдар", "Алина"], []) == {
        "attended": set(),
        "absent": {"Айдар", "Алина"},
        "guests": set(),
    }
# 6.
def check_compare_checks():
    before = ["login", "profile", "logout", "login"]
    after = ["login", "profile", "search", "search"]
    before_copy = before.copy()
    after_copy = after.copy()
    result = compare_checks(before, after)
    assert result["added"] == {"search"}
    assert result["removed"] == {"logout"}
    assert result["common"] == {"login", "profile"}
    assert before == before_copy
    assert after == after_copy
    assert compare_checks(["a", "b", "c"], ["c", "a", "b"]) == {
        "added": set(),
        "removed": set(),
        "common": {"a", "b", "c"},
    }
    assert compare_checks([], ["login"]) == {
        "added": {"login"},
        "removed": set(),
        "common": set(),
    }
# 7.
def check_can_run():
    required = {"python", "git"}
    available = {"python", "git", "json"}
    required_copy = required.copy()
    available_copy = available.copy()
    assert can_run(required, available) is True
    assert required == required_copy
    assert available == available_copy
    assert can_run({"python", "git"}, {"python", "json"}) is False
    assert can_run(set(), set()) is True
    assert can_run(set(), {"python"}) is True
# 8.
def check_duplicate_ids():
    ids = [1, 4, 1, 7, 4, 4, 9]
    ids_copy = ids.copy()
    assert duplicate_ids(ids) == {1, 4}
    assert ids == ids_copy
    result = duplicate_ids([])
    assert result == set()
    assert isinstance(result, set)
    assert duplicate_ids([5]) == set()
    assert duplicate_ids([5, 5, 5]) == {5}
# 9
def check_unique_in_order():
    values = ["git", "python", "git", "json", "python"]
    values_copy = values.copy()
    assert unique_in_order(values) == ["git", "python", "json"]
    assert values == values_copy
    result = unique_in_order([])
    assert result == []
    assert isinstance(result, list)
    assert unique_in_order(["git", "git"]) == ["git"]

check_unique_cities()
check_attendance()
check_compare_checks()
check_can_run()
check_duplicate_ids()
check_unique_in_order()

print("OK: все проверки прошли")