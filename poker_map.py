import string

def tuple_sort(max_hash):
    max_tuple = max_hash[0]

    for i in range(1, len(max_hash)):
        for j in range(26):
            value = max_hash[i][j]
            if max_tuple[j] > value:
                break
            elif value > max_tuple[j]:
                max_tuple = max_hash[i]

    return max_tuple

def most_likely_hand(D, k):
    alpha_string = string.ascii_lowercase
    alpha_dict = {char:index for index, char in enumerate(alpha_string)}

    freq = 26 * [0]
    hand_freq = {}
    hand = []

    max_freq = 0
    max_hash = []
    hash_vals = {}

    for i in range(len(D)):
        if i == 0:
            for j in range(k):
                freq[alpha_dict[D[j]]] += 1
        else:
            freq[alpha_dict[D[i-1]]] += -1
            freq[alpha_dict[D[(i+k-1) % len(D)]]] += 1

        freq_tuple = ()
        for i in freq:
            freq_tuple += (i,)

        hash_value = hash(freq_tuple)
        hand.append(hash_value)

        if hash_value in hand_freq:
            hand_freq[hash_value] += 1

            if hand_freq[hash_value] > max_freq:
                max_freq = hand_freq[hash_value]
                max_hash = [freq_tuple]
            elif hand_freq[hash_value] == max_freq:
                max_hash.append(freq_tuple)
        else:
            hand_freq[hash_value] = 1

            if hand_freq[hash_value] > max_freq:
                max_freq = hand_freq[hash_value]
                max_hash = [freq_tuple]
            elif hand_freq[hash_value] == max_freq:
                max_hash.append(freq_tuple)

        hash_vals[hash_value] = freq_tuple

    max_tuple = tuple_sort(max_hash)
    hand = ""

    for i in range(len(max_tuple)):
        value = max_tuple[i]
        while value > 0:
            hand += alpha_string[i]
            value += -1

    return hand
