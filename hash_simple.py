# Hash function takes a 16 byte input and gives a 16 byte output. It uses multiplication (*), bit-wise exclusive OR (XOR)
# and modulo (%) to calculate an element of the digest based on elements of the input message:

#digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256

#For the first element, the value of message[-1] is 0.

#For example, if message[0] - 1 and message[1] = 129, then:
#For digest[0]:
# 129*message[0] = 129
#129 XOR message[-1] = 129
#129 % 256 = 129
#Thus digest[0] = 129.

#For digest[1]:
#129*message[1] = 16641
#16641 XOR message[0] = 16640
#16640 % 256 = 0
#Thus digest[1] = 0.

def answer(digest):
    # digest [i] = ( (129 * message[i]) XOR message[i-1]) % 256
    # digest1 = ((129 * 0) ^ 0) % 256
    # SO: 0 = ((129 * ?) ^ 0) % 256

    output = []

    for i in range(len(digest)):
        hash = 0  # message -1
        d = digest[i]
        m = ((129 * hash) ^ 0) % 256

        while d != m:
            hash += 1
            if i != 0:
                m = ((129 * hash) ^ output[i - 1]) % 256
            else:
                m = ((129 * hash) ^ 0) % 256

        if hash > 255:
            hash = 0
        elif hash < 0:
            hash = 255

        output.append(hash)

    return output


# test
digest1 = [0, 129, 3, 129, 7, 129, 3, 129, 15, 129, 3, 129, 7, 129, 3, 129]
print answer(digest1)
# Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]


digest2 = [0, 129, 5, 141, 25, 137, 61, 149, 113, 145, 53, 157, 233, 185, 109, 165]
print answer(digest2)
# Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225]

digest3 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print answer(digest3)

digest3 = [255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255, 255]
print answer(digest3)


#digest2 = ((129 * 1) ^ 0) % 256
    #digest3 = ((129 * 2) ^ 1) % 256
    #digest4 = ((129 * 3) ^ 2) % 256
    #digest5 = ((129 * 4) ^ 3) % 256
    #digest6 = ((129 * 5) ^ 4) % 256
    #digest7 = ((129 * 6) ^ 5) % 256
    #digest8 = ((129 * 7) ^ 6) % 256
    #digest9 = ((129 * 8) ^ 7) % 256
    #digest10 = ((129 * 9) ^ 8) % 256
    #digest11 = ((129 * 10) ^ 9) % 256
    #digest12 = ((129 * 11) ^ 10) % 256
    #digest13 = ((129 * 12) ^ 11) % 256
    #digest14 = ((129 * 13) ^ 12) % 256
    #digest15 = ((129 * 14) ^ 13) % 256
    #digest16 = ((129 * 15) ^ 14) % 256

