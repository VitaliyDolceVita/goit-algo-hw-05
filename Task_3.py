import sys
from collections import defaultdict

def parse_log_line(line: str) -> dict:
    parts = line.split(' ', maxsplit=3)
    return {
        'date': parts[0],
        'time': parts[1],
        'level': parts[2],
        'message': parts[3].strip()
    }

def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, 'r') as file:
        for line in file:
            logs.append(parse_log_line(line))
    return logs

def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log['level'] == level]

def count_logs_by_level(logs: list) -> dict:
    counts = defaultdict(int)
    for log in logs:
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print("Рівень логування | Кількість")
    print("-----------------|----------")
    for level, count in counts.items():
        print(f"{level:<16} | {count:<10}")

def main(file_path: str, log_level: str = None):
    logs = load_logs(file_path)
    counts = count_logs_by_level(logs)
    print(" ")
    display_log_counts(counts)
    print(" ")
    if log_level:
        filtered_logs = filter_logs_by_level(logs, log_level.upper())
        print(f"Деталі логів для рівня '{log_level.upper()}':")
        for log in filtered_logs:
            print(f"{log['date']} {log['time']} - {log['message']}")
    print(" ")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Використання: python script.py path/to/logfile.log [log_level]")
        sys.exit(1)
    file_path = sys.argv[1]
    log_level = sys.argv[2] if len(sys.argv) > 2 else None
    main(file_path, log_level)
