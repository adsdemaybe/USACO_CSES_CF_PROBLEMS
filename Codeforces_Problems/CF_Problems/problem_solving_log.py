import sys

def main():

    cases = int(sys.stdin.readline().strip("\n"))
    results = []

    for i in range(cases):
        letters = int(sys.stdin.readline().strip("\n"))
        string = sys.stdin.readline().strip("\n")
        letter_counts = get_letter_counts([0]*26, letters, string)

        count = 0
        for i in range(letters):
            if letter_counts[i] >= i + 1:
                count += 1

        results.append(count)
    
    for i in results:
        print(i)   

    sys.exit(1)     

def get_letter_counts(letter_counts, letters, string):
    for i in range(letters):
        letter_counts[ord(string[i]) - 65] += 1

    return letter_counts

main()