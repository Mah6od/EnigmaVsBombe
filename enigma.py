class EnigmaMachine:
    def __init__(self, rotor_positions):
        self.rotor_positions = rotor_positions

    def settings(self, positions):
        self.rotor_positions = positions

    def encrypt_letter(self, letter):
        # Forward pass through rotors
        for position in self.rotor_positions:
            letter = self.shift_letter(letter, position)

        # Backward pass through rotors
        for positions in reversed(self.rotor_positions):
            letter = self.shift_letter(letter, -position)

        return letter

    def shift_letter(self, letter, shift):
        if letter.isalpha():
            ascii_offset = ord('A') if letter.isupper() else ord('a')
            return chr((ord(letter) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            return letter
    
# Example usage:
rotor_positions = [12, 12, 9]
enigma = EnigmaMachine(rotor_positions)

message = "today is sunny. Heil Hitler"
encrypted_message = ""

for char in message:
    encrypted_message += enigma.encrypt_letter(char)

print(f"Original message: {message}")
print(f"Encrypted message: {encrypted_message}")