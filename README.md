# cipher_solitaire
implementation of the solitaire cipher

This implementation does not claim to be perfect.The function Crypt() is responsible for encryption, receives a word in Latin letters at the input and an array consisting of a mixed deck of cards. The program has a random deck generation function called random_set_of_cards().It is not necessary to use it; you can get a sequence of cards from a real deck.
Function Crypt() calls a gamma generation function called gamma_generation(). Next is the addition modulo 26 of the plaintext translated into numbers and gamma.
The first version does not take into account many nuances, in the future the program will be improved

