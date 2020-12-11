
def XOR_math (line1,line2):
    """Find min len from this 2 str. Then make XOR."""
    min_line = min(line1,line2,key=len)
    # print('Line with min lenght is {}'.format(min_line))
    output = b''
    for i in range(len(min_line)):
        output += bytes([line1[i] ^ line2[i]])
    return output


def word_search_XOR(word,xored_res):
    b_word = bytes(word,encoding='ascii')
    for i in range(len(xored_res)-len(word)-1):
        xored_res_part = xored_res[i:len(word)+i]
        test = XOR_math(b_word,xored_res_part)
        print(word,xored_res_part,test.decode(encoding='UTF-8',errors='strict'))
        # if bytes(word,encoding='ascii')==test:
        #     print("Was founded word {},{},{}".format(word,xored_res_part, test))


def main ():
    line_n1 = b'ad924aefaad4af341fb0c3f0143ea8a728c1275b05bdff4916f92eccb6d6c286994672a9bd2356f15224cab9d1'
    line_n2 = b'ad924af7a9cdaf3a1bb0c3f51227aaf37cde2b0f18f3e04911b267d8aacc85c89b4179fcbd29'
    output_XOR_lines = XOR_math(line_n1,line_n2)
    word_search_XOR('minute',output_XOR_lines)
    print(output_XOR_lines.decode('ascii'))
'''
    most_popular_words = ['time', 'be', 'good', 'to', 'the', 'person', 'have', 'new', 'of', 'and', 'year', 'do', 'first', 'in', 'a', 'way', 'say', 'last',
                          'for', 'that' , 'day', 'get', 'long', 'on', 'I', 'thing', 'make', 'great'  ,  'with'   , 'it', 'man', 'go', 'little', 'at', 'not',
                          'world', 'know', 'own', 'by', 'he', 'life', 'take', 'other', 'from', 'as', 'hand', 'see', 'old', 'up', 'you', 'part', 'come',
                          'right', 'about', 'this', 'child', 'think', 'big', 'into', 'but', 'eye', 'look', 'high', 'over', 'his', 'woman', 'want', 'different',
                          'after', 'they', 'place', 'give', 'small', 'her', 'work', 'use', 'large', 'she', 'week', 'find', 'next', 'or', 'case', 'tell', 'early',
                          'an', 'point', 'ask', 'young', 'will', 'government', 'work', 'important', 'my', 'company'  ,  'seem'  ,  'few', 'one', 'number', 'feel',
                          'public', 'all', 'group', 'try', 'bad', 'would', 'problem', 'leave', 'same', 'there', 'fact', 'call', 'able', 'their', 'is', 'are', 'am', 'it', 'can', 'could',
                          'may', 'If', 'if ']
    for i in most_popular_words:
        word_search_XOR(i,output_XOR_lines) '''


if __name__ == '__main__':
    main()


