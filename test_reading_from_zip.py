import zipfile
import pytest
from pypdf import PdfReader
import csv

from conftest import TMP_DIR


def test_checking_archive_csv(create_archive):
    with zipfile.ZipFile(TMP_DIR+'/test.zip') as zip_file:  # открываем архив
        with zip_file.open('ТестовыйCSV.csv') as csv_file:  # открываем файл в архиве
            content = csv_file.read().decode(
                'utf-8-sig')  # читаем содержимое файла и декодируем его если в файле есть символы не из английского алфавита
            csvreader = list(csv.reader(content.splitlines(), delimiter=';'))  # читаем содержимое файла и преобразуем его в список
            second_row = csvreader[1]  # получаем вторую строку
            print(second_row)

            assert second_row[0] == 'OU002'
            assert second_row[1] == 'OU001'
