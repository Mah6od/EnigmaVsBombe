class BombeMachine:
    def __init__(self):
        pass

    def is_english_word(self, word):
        common_words = ["the", "and", "is", "are", "a", "to", "of", "it", "in", "that" , "Heil", "Hitler"]
        return any(word.lower() == common.lower() for common in common_words)

    def decrypt_message(self, encrypted_message):
        for rotor1 in range(26):
            for rotor2 in range(26):
                for rotor3 in range(26):
                    decrypted_message = ""
                    for char in encrypted_message:
                        decrypted_message += self.shift_letter(char, -(rotor1 + rotor2 + rotor3) % 26)

                    words = decrypted_message.split()
                    if any(self.is_english_word(word) for word in words):
                        return decrypted_message, [rotor1, rotor2, rotor3]

        return None

    def shift_letter(self, letter, shift):
        if letter.isalpha():
            ascii_offset = ord('A') if letter.isupper() else ord('a')
            return chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            return letter

# Example usage:
bombe = BombeMachine()

encrypted_message = "zujge oy yatte. Nkor Nozrkx"

result = bombe.decrypt_message(encrypted_message)

if result:
    decrypted_message, rotor_settings = result
    print(f"Encrypted message: {encrypted_message}")
    print(f"Decrypted message: {decrypted_message}")
    print(f"Rotor settings: {rotor_settings}")
else:
    print("Decryption failed.")
