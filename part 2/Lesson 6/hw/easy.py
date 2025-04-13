import sqlite3
import pandas as pd

# Подключение к базе данных
conn = sqlite3.connect("med_data.db")
cursor_an_name = conn.cursor()
cursor_name = conn.cursor()

# Получение данных из таблиц
cursor_an_name.execute("SELECT * FROM med_an_name")
cursor_name.execute("SELECT * FROM med_name")

# Словари для расшифровки
med_an_name = {row[0]: (row[1], row[2], row[3], row[4])
               for row in cursor_an_name.fetchall()}
med_name = {row[0]: (row[1], row[2]) for row in cursor_name.fetchall()}

cursor_an_name.close()
cursor_name.close()
conn.close()


# Чтение данных из Excel (лист easy)
df = pd.read_excel("medicine.xlsx", sheet_name="easy")
df.columns = ['patient_id', 'test_code', 'value']
df['value'] = pd.to_numeric(df['value'], errors='coerce')

results = []

# Поиск отклонений
for patient_id in df['patient_id'].unique():
    patient_data = df[df['patient_id'] == patient_id]

    for _, row in patient_data.iterrows():
        test_code = row['test_code']
        val = row['value']

        if pd.isna(val) or test_code not in med_an_name:
            continue

        name, is_simple, min_val, max_val = med_an_name[test_code]

        # Только количественные анализы
        if is_simple == 'N':
            if min_val is not None and val < min_val:
                results.append(
                    [med_name[patient_id][0], med_name[patient_id][1], name, 'Понижен'])
            elif max_val is not None and val > max_val:
                results.append(
                    [med_name[patient_id][0], med_name[patient_id][1], name, 'Повышен'])

# Сохранение результатов
if results:
    result_df = pd.DataFrame(
        results, columns=['Имя', 'Телефон', 'Анализ', 'Заключение'])
    result_df.to_excel('result_easy.xlsx', index=False)
    print("Файл result_easy.xlsx успешно создан.")
else:
    print("Нет пациентов с плохими анализами.")
