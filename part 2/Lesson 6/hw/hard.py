import sqlite3
import pandas as pd

# Подключаемся к базе данных
conn = sqlite3.connect("med_data.db")

# Загружаем справочники из базы
med_an_name = pd.read_sql("SELECT * FROM med_an_name",
                          conn).set_index("id").to_dict("index")
med_name = pd.read_sql("SELECT * FROM med_name",
                       conn).set_index("id").to_dict("index")

conn.close()

# Чтение данных из Excel
df = pd.read_excel("medicine.xlsx", sheet_name="hard")
df.columns = ['patient_id', 'test_code', 'value']
df['value'] = pd.to_numeric(df['value'], errors='coerce')

results = []

# Группировка по пациентам
for patient_id in df['patient_id'].unique():
    patient_data = df[df['patient_id'] == patient_id]
    deviations = []

    for _, row in patient_data.iterrows():
        test_code = row['test_code']
        val = row['value']

        # Проверка значений для других анализов
        if test_code in med_an_name:
            an_info = med_an_name[test_code]
            name = an_info['name']
            is_simple = an_info['is_simple']
            min_val = an_info['min_value']
            max_val = an_info['max_value']

            # Для простых анализов
            if is_simple == 'N':
                # Для других анализов с числовыми значениями
                if val < min_val:
                    deviations.append((name, 'Понижен'))
                elif val > max_val:
                    deviations.append((name, 'Повышен'))
            else:
                if str(val).strip().lower() in ['+', 'полож.', 'положительно']:
                    deviations.append((name, 'Положитнльно'))
                else:
                    deviations.append((name, 'Отрицательно'))

    # Печать отклонений для каждого пациента
    print(f"Пациент {patient_id} имеет следующие отклонения: {deviations}")

    # Добавляем результат, если два или более отклонений
    if len(deviations) >= 2 and patient_id in med_name:
        patient_info = med_name[patient_id]
        for name, status in deviations:
            results.append(
                [patient_info['name'], patient_info['phone'], name, status])

# Сохраняем результаты
if results:
    result_df = pd.DataFrame(
        results, columns=['Имя', 'Телефон', 'Анализ', 'Заключение'])
    result_df.to_excel("result_hard.xlsx", index=False)
    print("Файл result_hard.xlsx успешно создан.")
else:
    print("Нет отклонений для пациентов.")
