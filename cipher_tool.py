class ScanCipherYogaGymn:
    def shift_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result

    def substitution_cipher(self, text, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        key = key.lower()
        trans = str.maketrans(alphabet, key)
        return text.translate(trans)

    def vignere_cipher(self, text, key):
        result = []
        key_length = len(key)
        key_int = [ord(i) - 97 for i in key.lower()]
        text_int = [ord(i) - 97 for i in text.lower()]

        for i in range(len(text_int)):
            value = (text_int[i] + key_int[i % key_length]) % 26
            result.append(chr(value + 97))
        return ''.join(result)

    def affine_cipher(self, text, a, b):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((a * (ord(char) - shift_base) + b) % 26 + shift_base)
            else:
                result += char
        return result

    def hill_cipher(self, text, key_matrix):
        import numpy as np
        text = text.replace(" ", "").lower()
        if len(text) % len(key_matrix) != 0:
            text += 'x' * (len(key_matrix) - len(text) % len(key_matrix))

        text_vector = [ord(char) - 97 for char in text]
        text_matrix = np.array(text_vector).reshape(-1, len(key_matrix)).T
        key_matrix = np.array(key_matrix)

        encrypted_matrix = np.dot(key_matrix, text_matrix) % 26
        encrypted_text = ''.join(chr(num + 97) for num in encrypted_matrix.flatten())
        return encrypted_text

    def transposition_cipher(self, text, key):
        text = text.replace(" ", "")
        n = len(key)
        text_matrix = [''] * n
        for index in range(n):
            for char in text[index::n]:
                text_matrix[index] += char
        return ''.join(text_matrix)


def main():
    cipher_tool = ScanCipherYogaGymn()

    while True:
        print("\nPilih Cipher:")
        print("1. Shift Cipher")
        print("2. Substitution Cipher")
        print("3. Vigenère Cipher")
        print("4. Affine Cipher")
        print("5. Hill Cipher")
        print("6. Transposition Cipher")
        print("7. Keluar")

        choice = input("Masukkan pilihan (1-7): ")

        if choice == '1':
            text = input("Masukkan teks: ")
            shift = int(input("Masukkan nilai shift: "))
            hasil = cipher_tool.shift_cipher(text, shift)
            print("Hasil:", hasil)  # Output hasil di sini

        elif choice == '2':
            text = input("Masukkan teks: ")
            key = input("Masukkan kunci: ")
            hasil = cipher_tool.substitution_cipher(text, key)
            print("Hasil:", hasil)  # Output hasil di sini

        elif choice == '3':
            text = input("Masukkan teks: ")
            key = input("Masukkan kunci: ")
            hasil = cipher_tool.vignere_cipher(text, key)
            print("Hasil:", hasil)  # Output hasil di sini

        elif choice == '4':
            text = input("Masukkan teks: ")
            a = int(input("Masukkan a: "))
            b = int(input("Masukkan b: "))
            hasil = cipher_tool.affine_cipher(text, a, b)
            print("Hasil:", hasil)  # Output hasil di sini

        elif choice == '5':
            text = input("Masukkan teks: ")
            hill_key = []
            for _ in range(2):  # Misal 2x2 matrix
                row = list(map(int, input("Masukkan baris kunci (dipisah spasi): ").split()))
                hill_key.append(row)
            hasil = cipher_tool.hill_cipher(text, hill_key)
            print("Hasil:", hasil)  # Output hasil di sini

        elif choice == '6':
            text = input("Masukkan teks: ")
            key = input("Masukkan kunci: ")
            hasil = cipher_tool.transposition_cipher(text, key)
            print("Hasil:", hasil)  # Output hasil di sini

        elif choice == '7':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
