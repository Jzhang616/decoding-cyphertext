# decoding-cyphertext
a function that decodes a string of cyphertext (some encrypted English text) into a string of legible plaintext.

The following encryption scheme is used:
• The nth plaintext alphabetic letter, for n > 1, is encrypted to the letter whose lexical
position is the sum modulo 26 of the ordinal value of the nth letter with the sum of the
ordinal values of all the letters that precede it in the plaintext.
• The first plaintext alphabetic letter of the message is encrypted to the letter whose lexical
position in the alphabet is the sum modulo 26 of the ordinal value of the first letter plus
the integer 59.
• Calculate the lexical position of the ciphertext letter as the letter at the position between 0
and 25, with‘a’ at 0, ‘b’ at 1, ..., ‘z’ at 25.
• Calculate the ordinal value of a letter by passing the character to the ord() function.
The integer returned is the ordinal value of the letter.
• To simplify matters the only alphabetic characters contained in the plaintext message will
be lowercase. No uppercase characters will be used.
• Leave non-alphabetic characters, including whitespace, punctuation, numbers, etc.
unchanged.
