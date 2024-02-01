import sys
import re
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    """Парсинг рядка логу та повернення розібраного запису."""
    parts = re.split(r'\s+', line.strip())
    timestamp = parts[0] + " " + parts[1]
    level = parts[2]
    message = ' '.join(parts[3:])
    return {'timestamp': timestamp, 'level': level, 'message': message}

def load_logs(file_path: str) -> list:
    """Завантаження логів з файлу."""
    logs = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
                logs.append(parse_log_line(line))
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
    except Exception as e:
        print(f"Сталася помилка під час читання файлу: {e}")
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    """Фільтрація логів за рівнем."""
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    """Підрахунок записів за рівнем логування."""
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    """Виведення результатів підрахунку в читабельній формі."""
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<17}| {count}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Введіть шлях до файлу логів як аргумент командного рядка.")
        sys.exit(1)

    log_file_path = sys.argv[1]
    logs = load_logs(log_file_path)

    if len(sys.argv) == 3:
        log_level = sys.argv[2]
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        counts = count_logs_by_level(filtered_logs)
        display_log_counts(counts)
    else:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)
