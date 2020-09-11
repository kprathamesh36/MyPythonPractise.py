def breakingRecords(n, scores):
    highest = scores[0]
    lowest = scores[0]
    highbreak = 0
    lowbreak = 0
    for i in scores[1:]:
        if i > highest:
            highest = i
            highbreak = highbreak + 1

        if i < lowest:
            lowest = i
            lowbreak = lowbreak + 1

    print(highbreak, lowbreak)


n = int(input())

scores = list(map(int, input().rstrip().split()))

breakingRecords(n, scores)
