def frequency_sort(freq):
    more_then_one = True

    for i in freq:
        if freq.count(i) > 1 :
            more_then_one = True
        else:
            more_then_one = False

    counts_of_elem = []

    for j in freq:
        if freq.count(j) not in counts_of_elem:
            counts_of_elem.append(freq.count(j))

    

    if more_then_one:
        if len(counts_of_elem) > 1:                 ### in this section i have to return revesr sort if the counts of elem are difrent
            freq = sorted(freq, reverse=True)
            return sorted(freq, key=freq.count, reverse=True)
        else:
            freq = sorted(freq, reverse=False)
            return sorted(freq, key=freq.count, reverse=True)

    else:
        return freq




frequency_sort([1,2,2,1])





