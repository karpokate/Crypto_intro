from XOR_Ceasar import *


def make_chunks(key_size, text):
    chunks_list = [text[i:i + key_size] for i in range(0, len(text), key_size)]
    return chunks_list


def ascii_to_hex(string):
    return string.encode("hex")

def count_Hamming_distance(chunk1, chunk2):
    distance_val = sum(c1 != c2 for c1, c2 in zip(chunk1, chunk2))
    return distance_val


def find_possible_key_size(min_size_key_lenght, max_size_key_lenght,
                           text):  # Brute-force keysize(num of bytes) from 2 -> 41
    mean_dist = []
    for key in range(min_size_key_lenght, max_size_key_lenght):
        # chunck for key-lenght
        chunks_list = make_chunks(key, text)
        # print(chunks_list)
        # value for counting mean of count_Hamming_distance for each possible key_size
        distance = []
        for index in range(len(chunks_list) - 1):
            normalising_dist = count_Hamming_distance(chunks_list[index], chunks_list[index + 1]) / float(key)
            distance.append(normalising_dist)
        result = {
            'key': key,
            'distance': sum(distance)/len(distance)
        }
        print(result)
        mean_dist.append(result)
    # print(mean_dist)
    maybe_keysize = sorted(mean_dist, key=lambda x: x['distance'])
    return maybe_keysize[0]['key']


def first_byte_blocks(chuncks_list):
    block_for_every_key_letter = []
    for index in range(len(chuncks_list[0]) - 1):
        first_byte_str = ''
        for chunck in chuncks_list:
            first_byte_str += str(chunck[index])
        block_for_every_key_letter.append(first_byte_str)
    return block_for_every_key_letter


def result_answer():
    pass


def main():
    text = '1c41023f564b2a130824570e6b47046b521f3f5208201318245e0e6b40022643072e13183e51183f5a1f3e4702245d4b285a1b23561965133f2413192e571e28564b3f5b0e6b50042643072e4b023f4a4b24554b3f5b0238130425564b3c564b3c5a0727131e38564b245d0732131e3b430e39500a38564b27561f3f5619381f4b385c4b3f5b0e6b580e32401b2a500e6b5a186b5c05274a4b79054a6b67046b540e3f131f235a186b5c052e13192254033f130a3e470426521f22500a275f126b4a043e131c225f076b431924510a295f126b5d0e2e574b3f5c4b3e400e6b400426564b385c193f13042d130c2e5d0e3f5a086b52072c5c192247032613433c5b02285b4b3c5c1920560f6b47032e13092e401f6b5f0a38474b32560a391a476b40022646072a470e2f130a255d0e2a5f0225544b24414b2c410a2f5a0e25474b2f56182856053f1d4b185619225c1e385f1267131c395a1f2e13023f13192254033f13052444476b4a043e131c225f076b5d0e2e574b22474b3f5c4b2f56082243032e414b3f5b0e6b5d0e33474b245d0e6b52186b440e275f456b710e2a414b225d4b265a052f1f4b3f5b0e395689cbaa186b5d046b401b2a500e381d4b23471f3b4051641c0f2450186554042454072e1d08245e442f5c083e5e0e2547442f1c5a0a64123c503e027e040c413428592406521a21420e184a2a32492072000228622e7f64467d512f0e7f0d1a'
    key_size = 12
    min_size_key = 2
    max_size_key = 10
    keysize = find_possible_key_size(min_size_key, max_size_key, text)
    print(keysize)
    #
    # test = make_chunks(keysize,text)
    #
    #
    # print(test)
    # blocks_list = first_byte_blocks(test)
    #
    #
    #
    # for i in range(keysize-1):
    #     answer = result_out(bytes(blocks_list[i],encoding='ascii'))
    #     print(answer["text_res"].decode())
    # for res in range(keysize):
    #     pass


if __name__ == '__main__':
    main()
