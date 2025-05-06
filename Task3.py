# Цей скрипт фільтрує IP-адреси з файлу apache_logs.txt,
# рахує кількість входжень дозволених IP і записує результат у файл filtered_ips.txt

import re
from collections import Counter
import os

def filter_ips(input_file_path, output_folder_path, allowed_ips_list, output_filename="filtered_ip_results.txt"):

    ip_counts = Counter()
    full_output_path = os.path.join(output_folder_path, output_filename)

    try:
        with open(input_file_path, 'r') as infile:
            for line in infile:
                parts = line.split()
                if parts:
                    ip_address = parts[0]
                    if ip_address in allowed_ips_list:
                        ip_counts[ip_address] += 1
        try:
            os.makedirs(output_folder_path, exist_ok=True)

            with open(full_output_path, 'w') as outfile:
                outfile.write("Статистика входжень дозволених IP-адрес:\n")
                if ip_counts:
                    for ip, count in ip_counts.items():
                        outfile.write(f"{ip} - {count}\n")
                else:
                    outfile.write("Дозволених IP-адрес у лог-файлі не знайдено або список дозволених порожній.\n")
            print(f"Результати фільтрації IP-адрес збережено у '{full_output_path}'")
        except IOError:
            print(f"Помилка: Не вдалося записати у файл '{full_output_path}'.")
        except Exception as e:
            print(f"Непередбачена помилка при записі файлу: {e}")

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл '{input_file_path}' не знайдено.")
    except IOError:
        print(f"Помилка: Не вдалося прочитати вхідний файл '{input_file_path}'.")

print("\n--- Фільтрація IP-адрес ---")
input_log_path_ip = input("Введіть шлях до вхідного лог-файлу для фільтрації IP: ")
output_folder_filtered_ips = input("Введіть шлях до папки для збереження відфільтрованих IP: ")

allowed_ips_config = []
print("\nТепер введіть дозволені IP-адреси. Введіть 'готово', коли закінчите.")
while True:
    ip_input = input("Додайте IP-адресу (або 'готово'): ")
    if ip_input.lower() == 'готово':
        break
    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip_input):
        allowed_ips_config.append(ip_input)
    else:
        print("Некоректний формат IP-адреси. Спробуйте ще раз.")

if not allowed_ips_config:
    print("Список дозволених IP-адрес порожній. Фільтрація не матиме результатів.")

default_filename_task3 = "allowed_ips_report.txt"
filter_ips(input_log_path_ip, output_folder_filtered_ips, allowed_ips_config, default_filename_task3)

print("\nРобота всіх скриптів завершена.")
