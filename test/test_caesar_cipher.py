def test_encript_caesar_cipher_with_word_exists_in_alphabet():

    from src.caesar_cipher import CaesarCipher

    caesar_cipher = CaesarCipher(shift_to_right=4)
    word_encript = caesar_cipher.encript("ronildo o melhor de todos")

    assert word_encript == "vsrmphssqiplsvhixshsw"


def test_decript_caesar_cipher_with_word_exists_in_alphabet():

    from src.caesar_cipher import CaesarCipher

    caesar_cipher = CaesarCipher(shift_to_right=4)
    word_encript = "ronildo o melhor de todos"

    word_decript = caesar_cipher.decript(text=word_encript)
    assert word_decript == "ronildoomelhordetodos"


# TODO
# create falue test
def test_encript_caesar_cipher_with_word_does_not_exists_in_alphabet():

    from src.caesar_cipher import CaesarCipher

    caesar_cipher = CaesarCipher(shift_to_right=4)

    try:
        caesar_cipher.encript("ronildo o melhor de todos 123")
    except Exception as e:
        assert str(e) == "Valor não encontrado no alfabeto"


# TODO
# create falue test
def test_decript_caesar_cipher_with_word_does_not_exists_in_alphabet():
    from src.caesar_cipher import CaesarCipher

    caesar_cipher = CaesarCipher(shift_to_right=4)

    try:
        caesar_cipher.decript("ronildo o @# de todos 123")
    except Exception as e:
        assert str(e) == "Valor não encontrado no alfabeto"
