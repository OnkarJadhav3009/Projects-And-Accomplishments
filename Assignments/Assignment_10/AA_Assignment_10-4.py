import heapq


def get_travel_plan(cities, priorities):
    priorityDictionary = {}
    city_priorities = {}

    travel_plan = []

    for city in cities:
        city_priorities[city] = 0

    for city1, city2 in priorities:
        priorityDictionary[city1] = city2

    for city1, city2 in priorities:
        visited = set()
        while True:
            city_priorities[city1] += 1
            if city1 in visited:
                return []
            visited.add(city1)
            if city1 not in priorityDictionary:
                city_priorities[city1] += 2
                break
            city1 = priorityDictionary[city1]

    res = []
    for k, v in city_priorities.items():
        heapq.heappush(res, (v, k))

    while res:
        travel_plan.append(heapq.heappop(res))

    return [city for priority, city in travel_plan]



