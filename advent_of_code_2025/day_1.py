def main():
    with open("advent_of_code_2025/inputact.txt", "r") as f:
        lines = f.readlines()

    counts = 0
    start = 50

    for raw in lines:
        action = raw.strip()
        if not action:
            continue

        if action[0] == "R":
            start = (start + int(action[1:])) % 100
        elif action[0] == "L":
            start = (start - int(action[1:])) % 100

        if start == 0: 
            counts += 1

    print(counts)

main()