import sys

def main():
    # get threshold and limit arguments from command-line
    arguments = sys.argv[1:]

    threshold = float(arguments[0]) # number between 0.0 and 1,000,000,000.0
    limit = float(arguments[1]) # number between 0.0 and 1,000,000,000.0

    cumsum = 0.0

    for line in sys.stdin:
        input = float(line.strip()) # convert input line str to float

        remainder = max(0.0, input - threshold) # remainder = 0.0 if input < threshold, else remainder = input - threshold

        # include limit constraint into remainder
        output = min(remainder, limit - cumsum) # output is remainder or whatever is left from limit
        print(output)

        cumsum += output

    print(cumsum)

if __name__ == "__main__":
    main()