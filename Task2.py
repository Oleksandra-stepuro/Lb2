# Цей скрипт генерує SHA-256 хеші для вказаних файлів і записує результати у файл file_hashes.txt.

import hashlib
import os

def generate_file_hashes(*file_paths_tuple, output_folder_path, output_filename="file_hashes_results.txt"):

    file_hashes = {}
    if not file_paths_tuple:
        print("Попередження: Не вказано жодного файлу для хешування.")
        return {}

    full_output_path = os.path.join(output_folder_path, output_filename)

    for file_path in file_paths_tuple:
        try:
            with open(file_path, 'rb') as file:
                file_content = file.read()
                sha256_hash = hashlib.sha256()
                sha256_hash.update(file_content)
                hex_digest = sha256_hash.hexdigest()
                file_hashes[file_path] = hex_digest
                print(f"Хеш для файлу '{file_path}' успішно згенеровано.")
        except FileNotFoundError:
            print(f"Помилка: Файл '{file_path}' не знайдено.")
        except IOError:
            print(f"Помилка: Не вдалося прочитати файл '{file_path}'.")

    if file_hashes:
        try:
            os.makedirs(output_folder_path, exist_ok=True)

            with open(full_output_path, 'w') as outfile:
                outfile.write("SHA-256 хеші файлів:\n")
                for path, hash_value in file_hashes.items():
                    outfile.write(f"{path}: {hash_value}\n")
            print(f"\nРезультати хешування збережено у '{full_output_path}'")
        except IOError:
            print(f"Помилка: Не вдалося записати у файл '{full_output_path}'.")
        except Exception as e:
            print(f"Непередбачена помилка при записі файлу: {e}")
    elif file_paths_tuple:
        print("\nНе було згенеровано жодного хешу (можливо, через помилки читання або файли не знайдено).")

    return file_hashes

print("\n--- Генератор хешів файлів ---")
files_to_hash_list = []
try:
    num_files = int(input("Скільки файлів ви хочете хешувати? Введіть число: "))
    if num_files < 0:
        print("Кількість файлів не може бути від'ємною.")
        num_files = 0
except ValueError:
    print("Некоректне введення. Будь ласка, введіть ціле число.")
    num_files = 0

for i in range(num_files):
    file_path_input = input(f"Введіть шлях до файлу {i+1}: ")
    files_to_hash_list.append(file_path_input)

if files_to_hash_list:
    output_folder_hashes = input("Введіть шлях до папки для збереження хешів (наприклад, C:/results/hashes): ")
    default_filename_task2 = "generated_hashes.txt"

    hash_results = generate_file_hashes(*files_to_hash_list,
        output_folder_path=output_folder_hashes,
        output_filename=default_filename_task2)

    if hash_results:
        print("\nГенерація хешів завершена. Результати також виведено нижче:")
        for path, hash_value in hash_results.items():
            print(f"{path}: {hash_value}")
    elif files_to_hash_list:
        print("Хешування не дало результатів.")
else:
    print("Не було вказано файлів для хешування.")