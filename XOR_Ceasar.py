text_task =  r'Yx`7cen7v7ergrvc~yp:|rn7OXE7t~g.re97R9p97~c7d.xb{s7cv|r7v7dce~yp75.r{{x7`xe{s57vys;7p~ary7c.r7|rn7~d75|rn5;7oxe7c.r7q~edc7{rccre75.57`~c.75|5;7c.ry7oxe75r57`~c.75r5;7c.ry75{57`~c.75n5;7vys7c.ry7oxe7yroc7t.ve75{57`~c.75|57vpv~y;7c.ry75x57`~c.75r57vys7dx7xy97Nxb7zvn7bdr7vy7~ysro7xq7tx~yt~srytr;7_vzz~yp7s~dcvytr;7\vd~d|~7rovz~yvc~xy;7dcvc~dc~tv{7crdcd7xe7`.vcrare7zrc.xs7nxb7qrr{7`xb{s7d.x`7c.r7urdc7erdb{c9'

# # пройтись подстановкой 256 байт
text_b = bytes(text_task, encoding='ascii')


# func calculate score
def score_of_message (input_bytes):
    english_letter_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([english_letter_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])


def XOR_math(encrypted_text, single_key_value):
    output_XOR = b''
    for i in encrypted_text:
        output_XOR += bytes([i ^ single_key_value])
    return output_XOR

def result_out(encrypted_text):
    result_search = []
    for i in range(256):
        decrypted_text = XOR_math(encrypted_text,i)
        score_of_text = score_of_message(decrypted_text)
        helper_search = {'text_res':decrypted_text, 'score_res':score_of_text,'key_res':i }
        result_search.append(helper_search)
    s =[]
    for i in range(256):
        s.append(result_search[i]['score_res'])
    result_dict = result_search[s.index(max(s))]
    return (result_dict)

def main():
    res = result_out(text_b)
    print(res)


if __name__ == '__main__':
    main()