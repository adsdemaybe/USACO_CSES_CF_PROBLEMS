import sys

# 1 2 4 3
# 2 4 1 3
# 3 1 2 3
# 1 2 3 4

def main():
    file_in = open("sleepy.in", 'r')
    sys.stdout = open("sleepy.out", 'w')
    
    