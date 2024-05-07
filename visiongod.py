import os
import subprocess
from colorama import Fore, Style

# Получаем путь к директории главного скрипта
script_dir = os.path.dirname(os.path.abspath(__file__))

# Имя папки с инструментами
tools_folder = "Tools"

# Список инструментов
tools = {
    1: "Пробив по номеру телефона (VG_number.py)",
    2: "Пробив по IP (VG_IP.py)",
    3: "Пробив по MAC (VG_MAC.py)",
    4: "Пробив по GMAIL (VG_GMAIL.py)",
    5: "Пробив по паспорту (VG_Passport.py)",
    6: "Пробив по номеру машины (VG_Car.py)"
}

# Функция для вывода меню
def print_menu():
    print(Fore.CYAN + "=" * 50)
    print(Fore.CYAN + f" VisionGOD Инструменты")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
    for key, value in tools.items():
        print(f"{key}. {value}")
    print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

# Функция для выбора
def select_tool():
    while True:
        try:
            choice = int(input("Выберите инструмент (1-6): "))
            if choice in tools:
                return choice
            else:
                print(Fore.RED + "Неверный выбор. Попробуйте еще раз." + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "Введите число от 1 до 6." + Style.RESET_ALL)

# Функция для поиска и запуска VG_number.py
def run_vg_number_script():
    vg_number_path = os.path.join(script_dir, tools_folder, "number.py")
    if os.path.isfile(vg_number_path):
        try:
            subprocess.run(["python", vg_number_path], check=True)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Ошибка при запуске инструмента number.py: {e}" + Style.RESET_ALL)
    else:
        print(Fore.RED + f"Скрипт number.py не найден в папке {tools_folder}." + Style.RESET_ALL)

# Главная функция
def main():
    print_menu()
    choice = select_tool()
    if choice == 1:
        run_vg_number_script()
    else:
        tool_name = list(tools.values())[choice - 1].split("(")[1][:-1]  # Извлекаем имя скрипта из описания
        tool_path = os.path.join(script_dir, tools_folder, tool_name)
        try:
            subprocess.run(["python", tool_path], check=True)
        except subprocess.CalledProcessError as e:
            print(Fore.RED + f"Ошибка при запуске инструмента {tool_name}: {e}" + Style.RESET_ALL)

if __name__ == "__main__":
    main()