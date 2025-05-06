import re
import os

def analyze_log_file(log_file_path, output_folder_path, output_filename="status_code_results.txt"):

    status_codes = {}
    full_output_path = os.path.join(output_folder_path, output_filename)

    try:
        with open(log_file_path, 'r') as infile:
            for line in infile:
                match = re.search(r'" (\d{3}) ', line)
                if match:
                    code = match.group(1)
                    status_codes[code] = status_codes.get(code, 0) + 1
        try:
            os.makedirs(output_folder_path, exist_ok=True)

            with open(full_output_path, 'w') as outfile:
                outfile.write("Статистика кодів відповіді HTTP:\n")
                if status_codes:
                    for code, count in status_codes.items():
                        outfile.write(f"Код {code}: {count} разів\n")
                else:
                    outfile.write("Коди відповіді у файлі не знайдено або файл порожній.\n")
            print(f"Результати аналізу лог-файлу збережено у '{full_output_path}'")
        except IOError:
            print(f"Помилка: Не вдалося записати у файл '{full_output_path}'. Перевірте права доступу.")
            return {}
        except Exception as e:
            print(f"Непередбачена помилка при записі файлу: {e}")
            return {}

    except FileNotFoundError:
        print(f"Помилка: Вхідний файл '{log_file_path}' не знайдено.")
        return {}
    except IOError:
        print(f"Помилка: Не вдалося прочитати вхідний файл '{log_file_path}'.")
        return {}
    return status_codes

print("--- Аналізатор лог-файлів ---")
input_log_path = input("Введіть шлях до вхідного лог-файлу (наприклад, C:/logs/apache_logs.txt): ")
output_folder = input("Введіть шлях до папки для збереження результатів (наприклад, C:/results): ")

default_filename_task1 = "status_code_analysis.txt"

results = analyze_log_file(input_log_path, output_folder, default_filename_task1)

if results:
    print("\nАналіз завершено. Результати також виведено нижче:")
    for code, count in results.items():
        print(f"Код {code}: {count}")
else:
    print("Аналіз не дав результатів через помилки або відсутність даних.")