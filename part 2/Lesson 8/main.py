import psycopg2
import re

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect(
    dbname="payments",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

# Получаем данные
cursor.execute("SELECT id, reason, reason_correct FROM payments")
rows = cursor.fetchall()

# Функция нормализации строки


def normalize_reason(reason):
    # нижний регистр и удаление лишних пробелов
    reason = reason.lower().strip()
    reason = reason.replace('\\', '/')
    reason = re.sub(r'[_]', ' ', reason)          # подчёркивания → пробелы
    reason = re.sub(r'[^\d/.\s]', ' ', reason)    # только цифры, /, ., пробелы
    # удаляем точки не между цифрами
    reason = re.sub(r'(?<!\d)\.(?!\d)', '', reason)
    reason = re.sub(r'\s*от\s*', ' от ', reason)  # нормализация "от"
    reason = re.sub(r'(\d{2})\s*\.\s*(\d{2})\s*\.\s*(\d{4})',
                    r'\1.\2.\3', reason)  # дата
    # множественные пробелы → один
    reason = re.sub(r'\s+', ' ', reason)
    return reason.strip()


# Подсчёт совпадений
total = len(rows)
matched = 0

for row in rows:
    row_id, reason, reason_correct = row
    transformed = normalize_reason(reason)
    if transformed == reason_correct.lower():
        matched += 1
    else:
        print(
            f"❌ ID {row_id}\n  Исходное:   {reason}\n  Приведено:  {transformed}\n  Ожидается: {reason_correct}\n")

# Результат
match_percent = (matched / total) * 100 if total else 0
print(f"\nИтого записей: {total}")
print(f"Совпадений: {matched}")
print(f"Процент совпадений: {match_percent:.2f}%")

cursor.close()
conn.close()
