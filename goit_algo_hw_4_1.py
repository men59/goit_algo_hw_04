def total_salary(path):
    try:
        with open(path, "r", encoding= 'UTF-8') as fh:
            salary = []
            while True:
                line = fh.readline()
                if not line:
                    break
                _line = line.split(',')
                salary.append(int(_line[1]))  # Перше число в кожному рядку
            total = sum(salary)
            count = len(salary)
            average = total / count
            return total, average
    except FileNotFoundError:
        print("Файл не знайдено")
        return None, None
total, average = total_salary("file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
