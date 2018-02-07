import sys
from bs4 import BeautifulSoup


def word_in_list(list_words, word):
    candit = []
    for w in list_words:
        if(word in w):
            candit.append(w)
    return candit


def last_exact_list(list_words, word, i, f):
    candit = []
    for w in list_words:
        if(word == w):
            candit.append([w, i, f])
    return candit


def insert_link(phrase, text, last_exact, dict_words):

    part1 = '<a data-cke-saved-href="'
    part2 = '" href="'
    part3 = '" target="">'
    part4 = '</a>'

    pos = 0
    if(phrase[last_exact[0][1]] == ','):
        pos = 1

    link = part1 + dict_words[last_exact[0][0]] + \
        part2 + dict_words[last_exact[0][0]] + \
        part3 + phrase[last_exact[0][1]+pos:last_exact[0][2]+1] + \
        part4

    if(phrase[last_exact[0][1]+pos] == ' '):
        pos += 1

    phrase = phrase[:last_exact[0][1]+pos] + link + phrase[last_exact[0][2]+1:]
    return phrase, last_exact[0][1]+len(link)


def search_word(dict_words, list_words, phrase):
    post_token = 0
    concat = True
    super_concat = False
    while(post_token < len(phrase)):
        last_post_token = 0
        word = ''
        text = ''

        post_token_val = False
        last_post_token = post_token
        new_list_words = list(list_words)
        last_exact = []
        for i in range(post_token, len(phrase)):
            if('<h1 ' in phrase[post_token:post_token+5] or
               '<h2>' in phrase[post_token:post_token+5]):
                super_concat = True
            if('</h1>' in phrase[post_token:post_token+5] or
               '</h2>' in phrase[post_token:post_token+5]):
                super_concat = False
            if(phrase[i] == '.' and concat is True):
                if(len(last_exact) == 1):
                    phrase, post_token = insert_link(phrase,
                                                     text,
                                                     last_exact,
                                                     dict_words)
                    if(super_concat is False):
                        list_words.remove(last_exact[0][0])
                    last_exact = []
                text = ''
                break

            if(phrase[i] == '>'):
                concat = True
                text = ''
                post_token = i + 1
                break

            if(phrase[i] == '<'):
                if(len(last_exact) == 1):
                    phrase, post_token = insert_link(phrase,
                                                     text,
                                                     last_exact,
                                                     dict_words)
                    if(super_concat is False):
                        list_words.remove(last_exact[0][0])
                    last_exact = []
                text = ''
                if(i == post_token):
                    concat = False
                break

            if(concat):
                if(phrase[i] not in [' ', '.', ',']):
                    word += phrase[i]
                if(i != len(phrase)-1):
                    if(phrase[i+1] in [' ', '<', '.', ':', ','] and
                       phrase[i] not in [' ', '.', ',']):
                        if(text == ''):
                            text += word
                        else:
                            text += ' ' + word
                        word = ''
                        if(post_token_val is False):
                            post_token_val = True
                            post_token = i+1
                        new_list_words = word_in_list(new_list_words,
                                                      text.lower())
                        res = last_exact_list(new_list_words,
                                              text.lower(),
                                              last_post_token,
                                              i)

                        if(len(res) > 0):
                            last_exact = res
                        if(len(new_list_words) == 0 and len(last_exact) == 0):
                            break
                        if(len(new_list_words) == 0 and len(last_exact) == 1):
                            phrase, post_token = insert_link(phrase,
                                                             text,
                                                             last_exact,
                                                             dict_words)
                            if(super_concat is False):
                                list_words.remove(last_exact[0][0])
                            last_exact = []
                            break
        if(post_token == last_post_token):
            post_token += 1

    return phrase


def unwrap(soup):
    for i in ['h1', 'h2']:
        for s in soup.find_all(i):
            while(s.find('a')):
                s.a.unwrap()
    return soup


def main():
    name_file = sys.argv[1]
    name_out = sys.argv[2]
    name_links = sys.argv[3]

    body = open(name_file).read()
    uids = open(name_links, 'r')

    dicionario = {}
    list_words = []

    for u in uids:
        uid, title = u.replace('\n', '').replace(',', '').split(' ', 1)
        dicionario[title.lower()] = uid
        list_words.append(title.lower())

    phrase = search_word(dicionario, list_words, body)
    soup = unwrap(BeautifulSoup(phrase, 'html.parser'))

    open(name_out, 'w').write(str(soup.contents[0]))


main()
