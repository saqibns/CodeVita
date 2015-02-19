def run(start, stops, stations):
    length = len(stops)
    fuel = 0
    fuel += stations[start - 1]
    idx = start - 1
    while True:
        fuel -= stops[idx]
        if fuel < 0:
            break
        idx += 1
        if idx >= length:
            break
        fuel += stations[idx]
    print(idx + 1)

def update(stations, at, value):
    stations[at] = value


def main():
    input()
    stops = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            update(stations, query[1] - 1, query[2])
        else:
            run(query[1], stops, stations)

main()