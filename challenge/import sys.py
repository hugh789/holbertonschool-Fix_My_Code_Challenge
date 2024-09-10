import sys

def solution(N):
    # Print the vertical part of the "L"
    for i in range(N - 1):
        sys.stdout.write("L\n")
    
    # Print the horizontal part of the "L"
    sys.stdout.write("L" * N + "\n")
