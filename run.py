from src.caesar_cipher import CaesarCipher


caesar_cipher = CaesarCipher(shift_to_right=4)

word_encript = caesar_cipher.encript('ronildo o melhor de todos')
print(word_encript)

word_decript = caesar_cipher.decript(text=word_encript)
print(word_decript)
