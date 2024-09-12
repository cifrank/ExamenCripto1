def decrypt_caesar_cipher(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.lower() == 'ñ':
                shift_amount = 164  # Código ASCII para 'ñ'
                decrypted_text += chr((ord(char) - shift_amount - shift) % 27 + shift_amount)
            else:
                shift_amount = 65 if char.isupper() else 97
                decrypted_text += chr((ord(char) - shift_amount - shift) % 26 + shift_amount)
        else:
            decrypted_text += char
    return decrypted_text

cipher_text = "Qyyn zsvqbsw, iye ny gbyxq iyeb rkxn dyy wemr, Grsmr wkxxobvi nofydsyx crygc sx drsc; Pyb cksxdc rkfo rkxnc drkd zsvqbswc’ rkxnc ny dyemr, Kxn zkvw dy zkvw sc ryvi zkvwobc’ uscc"
for shift in range(27):
    print(f"TEXTO 1: Shift {shift}: {decrypt_caesar_cipher(cipher_text, shift)}")