class ScanCipherYogaGymn:
    # Shift Cipher: Menggeser setiap huruf dalam teks sebanyak 'shift' posisi dalam alfabet
    def shift_cipher(self, text, shift):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                result += char
        return result

    # Substitution Cipher: Mengganti setiap huruf dengan huruf lain sesuai kunci
    def substitution_cipher(self, text, key):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        # Perpanjang kunci agar panjangnya sama dengan alphabet (26 karakter)
        key = (key * (len(alphabet) // len(key) + 1))[:len(alphabet)]
        trans = str.maketrans(alphabet, key)
        return text.translate(trans)

    # Vigenère Cipher: Menggunakan kunci untuk menggeser huruf berdasarkan posisi huruf dalam kunci
    def vignere_cipher(self, text, key):
        result = []
        key_length = len(key)
        key_int = [ord(i) - 97 for i in key.lower()]
        text_int = [ord(i) - 97 for i in text.lower()]

        for i in range(len(text_int)):
            value = (text_int[i] + key_int[i % key_length]) % 26
            result.append(chr(value + 97))
        return ''.join(result)

    # Affine Cipher: Memodifikasi teks menggunakan fungsi linear (a*x + b) mod 26
    def affine_cipher(self, text, a, b):
        result = ""
        for char in text:
            if char.isalpha():
                shift_base = ord('A') if char.isupper() else ord('a')
                result += chr((a * (ord(char) - shift_base) + b) % 26 + shift_base)
            else:
                result += char
        return result

    # Hill Cipher: Enkripsi berdasarkan operasi matriks menggunakan matriks kunci
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

    # Transposition Cipher: Mengacak huruf dalam teks berdasarkan urutan kunci
    def transposition_cipher(self, text, key):
        text = text.replace(" ", "")
        n = len(key)
        text_matrix = [''] * n
        for index in range(n):
            for char in text[index::n]:
                text_matrix[index] += char
        return ''.join(text_matrix)

    # Enkripsi lengkap menggunakan gabungan algoritma
    def encrypt(self, text, shift, sub_key, vignere_key, affine_a, affine_b, hill_key, trans_key):
        # Langkah enkripsi berlapis
        step1 = self.shift_cipher(text, shift)  # Shift Cipher
        step2 = self.substitution_cipher(step1, sub_key)  # Substitution Cipher
        step3 = self.vignere_cipher(step2, vignere_key)  # Vigenère Cipher
        step4 = self.affine_cipher(step3, affine_a, affine_b)  # Affine Cipher
        step5 = self.hill_cipher(step4, hill_key)  # Hill Cipher
        step6 = self.transposition_cipher(step5, trans_key)  # Transposition Cipher
        return step6

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
        print("7. Enkripsi Lengkap")
        print("8. Keluar")

        choice = input("Masukkan pilihan (1-8): ")

        if choice == '1':
            text = input("Masukkan teks: ")
            shift = int(input("Masukkan nilai shift: "))
            hasil = cipher_tool.shift_cipher(text, shift)
            print("Hasil:", hasil)

        elif choice == '2':
            text = input("Masukkan teks: ")
            key = input("Masukkan kunci (alfabet, misal: yoga): ")
            hasil = cipher_tool.substitution_cipher(text, key)
            print("Hasil:", hasil)

        elif choice == '3':
            text = input("Masukkan teks: ")
            key = input("Masukkan kunci Vigenère: ")
            hasil = cipher_tool.vignere_cipher(text, key)
            print("Hasil:", hasil)

        elif choice == '4':
            text = input("Masukkan teks: ")
            a = int(input("Masukkan a (Affine Cipher): "))
            b = int(input("Masukkan b (Affine Cipher): "))
            hasil = cipher_tool.affine_cipher(text, a, b)
            print("Hasil:", hasil)

        elif choice == '5':
            text = input("Masukkan teks: ")
            hill_key = []
            for _ in range(2):  # Misal 2x2 matrix
                row = list(map(int, input("Masukkan baris kunci Hill (dipisah spasi): ").split()))
                hill_key.append(row)
            hasil = cipher_tool.hill_cipher(text, hill_key)
            print("Hasil:", hasil)

        elif choice == '6':
            text = input("Masukkan teks: ")
            key = input("Masukkan kunci Transposition: ")
            hasil = cipher_tool.transposition_cipher(text, key)
            print("Hasil:", hasil)

        elif choice == '7':
            text = input("Masukkan teks: ")
            shift = int(input("Masukkan nilai shift: "))
            sub_key = input("Masukkan kunci substitusi (misal: yoga): ")
            vignere_key = input("Masukkan kunci Vigenère: ")
            affine_a = int(input("Masukkan a (Affine Cipher): "))
            affine_b = int(input("Masukkan b (Affine Cipher): "))
            hill_key = []
            for _ in range(2):  # Misal 2x2 matrix
                row = list(map(int, input("Masukkan baris kunci Hill (dipisah spasi): ").split()))
                hill_key.append(row)
            trans_key = input("Masukkan kunci Transposition: ")

            hasil = cipher_tool.encrypt(text, shift, sub_key, vignere_key, affine_a, affine_b, hill_key, trans_key)
            print("Hasil enkripsi lengkap:", hasil)

        elif choice == '8':
            print("Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()
