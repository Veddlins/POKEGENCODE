import qrcode
import os
import random
import shutil

shutil.rmtree("qr_codes")


file_name = 'input.txt'

w = int(input("Введите количество кодов для генерации: "))

with open(file_name, 'a', encoding='utf-8') as file:
    for i in range(w):
        while True:
            code = [random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(3)]
            code1 = [random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(4)]
            code3 = [random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(3)]
            code4 = [random.choice('1234567890QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(3)]

            if not (code[0].isdigit() and code[1].isdigit() and code[2].isdigit() or
                    code1[0].isdigit() and code1[1].isdigit() and code1[2].isdigit() and code1[3].isdigit() or
                    code3[0].isdigit() and code3[1].isdigit() and code3[2].isdigit() or
                    code4[0].isdigit() and code4[1].isdigit() and code4[2].isdigit()):
                break

        fin_code = ''.join((''.join(code), '-', ''.join(code1), '-', ''.join(code3), '-', ''.join(code4)))

        file.write(fin_code + '\n')

print("Генерация кодов завершена.")


def create_qr_code(data, output_file):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=50,
        border=1,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(output_file)


input_file = 'input.txt'

output_folder = 'qr_codes'


if not os.path.exists(output_folder):
    os.makedirs(output_folder)


with open(input_file, 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if line:
            output_file = os.path.join(output_folder, f"{line}.png")
            create_qr_code(line, output_file)

print("Генерация QR-кодов завершена.")

os.remove("input.txt")

