"""Создание файлов и папок"""

import openpyxl
from openpyxl import Workbook
import shutil
import os
from pathlib import Path
import locale

# Устанавливаем русскую локаль
locale.setlocale(locale.LC_TIME, "ru_RU.UTF-8")
parent_dir = Path("w")  
workbook = openpyxl.load_workbook("w/Заявки ВОЛС 2022 - 2025.xlsx")
sheet = workbook["2025"] 
# Проходим по всем строкам и столбцам
for row in sheet.iter_rows(min_row=45, max_row=56, min_col=1, max_col=sheet.max_column):
    date = row[3].value.strftime("%d.%m.%Y")
    time = row[3].value.strftime("%H:%M")
    date_folder = row[3].value.strftime("%m_%Y")
    date_full = row[3].value.strftime("%d %B %Y")
    folder_name = (str(row[2].value)+' '+str(date)+' '+str(row[5].value))
    print(folder_name)
    operator =  row[1].value
    photo = 'фото'
    child_dir = parent_dir / operator / "АВР_ДР" / date_folder /"на оформлении" / folder_name 
    child_dir.mkdir(parents=True, exist_ok=True) 
    child_photo = parent_dir / operator / "АВР_ДР" / date_folder / "на оформлении"/ folder_name / photo
    child_photo.mkdir(parents=True, exist_ok=True) 
    if (operator == 'Мегафон'):
        # Исходный файл и путь назначения
        source_file = "w/megafon.xlsx"  # Укажите путь к исходному файлу
        destination_folder = child_dir  # Укажите путь к папке назначения
        new_filename = f"{folder_name}.xlsx"  # Новое имя файла
        # Проверяем, существует ли папка назначения
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)
        # Полный путь к новому файлу
        destination_file = os.path.join(destination_folder, new_filename)
        # Копируем и переименовываем файл
        shutil.copy2(source_file, destination_file)
        # Открываем файл для редактирования
        wb = openpyxl.load_workbook(destination_file)
        # Выбираем нужный лист (например, "ВедомостьВР")
        sheet_name = "ВедомостьВР" 
        sheet_name_akt = "11Акт"# Название листа
        sheet_name_dr = "Акт ДР"# Название листа
        if sheet_name in wb.sheetnames:
            ws = wb[sheet_name]
            ws_akt = wb[sheet_name_akt]
            ws_dr = wb[sheet_name_dr]
        else:
            print(f"Ошибка: Лист '{sheet_name}' не найден. Доступные листы: {wb.sheetnames}")
            wb.close()
            exit()       
        # Вносим изменения 
        ws["C10"] = str(row[2].value) + " от " + date
        mileage = input("Километраж заявке № " +  str(row[2].value) + " от "+date+" введите(км) ")
        ws["D45"] = mileage
        ws_akt["B2"] = " от " + date_full
        ws_akt["B7"] = f"1. {date} г. Исполнитель оказал, а Заказчик принял работы по договору № РТК-ВОЛС-24-26 от 15.03.2024 г., а именно:"
        ws_dr["E4"] = ws_dr["D15"] = ws_dr["D17"] = date_full
        ws_dr["E15"] = time     
        # Сохраняем файл
        wb.save(destination_file)
        wb.close()
workbook.close()

