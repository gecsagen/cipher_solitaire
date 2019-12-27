import string
import random
from itertools import *

FACE_CARDS = ('J', 'Q', 'K', 'A')  # designations for jack, queen, king and ace
SUITS = ('H', 'D', 'C', 'S')  # card suits

card_sequence = list(product(chain(range(2, 11), FACE_CARDS), SUITS, ))
card_sequence.append(('$', 1))  # add the first joker to the deck
card_sequence.append(('$', 2))  # add a second joker to the deck
card_sequence1 = [str(x) + str(y) for x, y in card_sequence]

# dictionary letter: number, used for function convert_a_string_into_numbers
alphabet = {y: x + 1 for (x, y) in enumerate(string.ascii_lowercase.upper())}
# dictionary number: letter, used for function convert_from_numbers_to_string
alphabet_two = {x + 1: y for (x, y) in enumerate(string.ascii_lowercase.upper())}


# string to digit function
def convert_a_string_into_numbers(word):
    res = [alphabet[x] for x in word if x in alphabet]
    return res


# digit to string conversion function
def convert_from_numbers_to_string(list_numbes):
    res = [alphabet_two[x] for x in list_numbes if x in alphabet_two]
    return res


# random deck function
def random_set_of_cards():
    # shuffle the deck randomly
    random.shuffle(card_sequence1)
    return card_sequence1


# gamma generation function
def gamma_generation(mixed_deck_of_cards, gamma_lenght):
    gamma = []
    deck = []
    deck1 = []
    while gamma_lenght > 0:
        # swap the first joker with the next card
        for (y, x) in enumerate(mixed_deck_of_cards):
            if '$1' in x:
                deck = mixed_deck_of_cards[0:y] + [mixed_deck_of_cards[y + 1]] + [
                    mixed_deck_of_cards[y]] + mixed_deck_of_cards[y + 2:]
                break
        # swap the second joker with two subsequent cards
        for (y, x) in enumerate(deck):
            if '$2' in x:
                deck1 = deck[0:y] + deck[y + 1:y + 3] + [deck[y]] + deck[y + 3:]
                break
        # make a triple cut of the deck
        pos_one = 0
        pos_two = 0
        for (y, x) in enumerate(deck1):
            if '$1' in x:
                pos_one = y
            if '$2' in x:
                pos_two = y
        deck2 = deck1[pos_two + 1:] + deck1[pos_one:pos_two] + [deck1[pos_two]] + deck1[0:pos_one]

        # We take the bottom card and assign it a number
        value_cards = {x: y + 1 for y, x in enumerate(card_sequence1)}
        value_cards.update({"$2": 53})
        last_card = value_cards[deck2[-1]]
        fourth_step = deck2[last_card: -1] + deck2[0: last_card] + [deck2[-1]]

        # find the first card and assign it a number
        first_card = value_cards[fourth_step[0]]
        search_card = value_cards[fourth_step[first_card]]
        if search_card >= 26:
            search_card -= 26
        gamma.append(search_card)
        mixed_deck_of_cards = fourth_step
        gamma_lenght -= 1
    return [gamma, mixed_deck_of_cards]


# encryption function (modulo 26 addition)
def crypt(open_text, mixed_deck_of_cards1):
    result = []
    open_text = convert_a_string_into_numbers(open_text)
    gamma = gamma_generation(mixed_deck_of_cards1, len(open_text))
    for (k, v) in zip(open_text, gamma[0]):
        res = k + v
        if res >= 26:
            res -= 26
        result.append(res)
    result_str_mass = convert_from_numbers_to_string(result)
    final_result = ''.join(result_str_mass)
    print('The current state of the deck after encryption:', gamma[1])
    my_file = open('save_state_deck_crypt.txt', 'w')
    my_file.write(str('The current state of the deck after encryption:' + str(gamma[1])))
    my_file.close()
    return final_result


# decryption function, subtraction modulo 26
def decrypt(close_text, mixed_deck_of_cards1):
    result = []
    close_text = convert_a_string_into_numbers(close_text)
    gamma = gamma_generation(mixed_deck_of_cards1, len(close_text))
    for (k, v) in zip(close_text, gamma[0]):
        res = k - v
        if res <= 0:
            res += 26
        result.append(res)
    result_str_mass = convert_from_numbers_to_string(result)
    final_result = ''.join(result_str_mass)
    print('The current state of the deck after decryption:', gamma[1])
    my_file = open('save_state_deck_decrypt.txt', 'w')
    my_file.write(str('The current state of the deck after decryption:' + str(gamma[1])))
    my_file.close()
    return final_result


# Self test module
if __name__ == '__main__':
    print(crypt('HELLO',
                ['10S', '10C', '8C', '10D', '3S', '$1', 'QH', '9H', '8S', 'QC', 'KH', '2S', '6D', '2D', '$2', '6H',
                 '5D',
                 '5S', '9D', '10H', '6C', '8H', '$2', '7C', '7H', 'KS', 'JD', '4S', 'JC', '7S', '7D', '5H', '9S', '7C',
                 'AD', '4C', '4H', '3C', 'QD', 'QS', '3H', 'KD', '5C', '6S', '2C', '9C', 'AH', 'JH', '2H', '4D', 'AS',
                 '3D',
                 'JS', '8D', '10S', '10C', '8C', '10D', '7H', 'KS', 'JD', '4S', 'JC', '7S', '7D', '5H', '9S', 'AD',
                 '4H',
                 '3C', 'QD', 'QS', '3H', 'KD', '5C', '6S', '2C', '9C', 'AH', 'JH', '2H', '4D', 'KC', 'AS', '3D', 'JS',
                 '8D',
                 'AC']))
    print(decrypt('HCHDV',
                  ['10S', '10C', '8C', '10D', '3S', '$1', 'QH', '9H', '8S', 'QC', 'KH', '2S', '6D', '2D', '$2', '6H',
                   '5D',
                   '5S', '9D', '10H', '6C', '8H', '$2', '7C', '7H', 'KS', 'JD', '4S', 'JC', '7S', '7D', '5H', '9S',
                   '7C',
                   'AD', '4C', '4H', '3C', 'QD', 'QS', '3H', 'KD', '5C', '6S', '2C', '9C', 'AH', 'JH', '2H', '4D', 'AS',
                   '3D',
                   'JS', '8D', '10S', '10C', '8C', '10D', '7H', 'KS', 'JD', '4S', 'JC', '7S', '7D', '5H', '9S', 'AD',
                   '4H',
                   '3C', 'QD', 'QS', '3H', 'KD', '5C', '6S', '2C', '9C', 'AH', 'JH', '2H', '4D', 'KC', 'AS', '3D', 'JS',
                   '8D',
                   'AC']))
