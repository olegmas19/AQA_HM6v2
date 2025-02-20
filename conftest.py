import zipfile
import pytest
import os.path
import shutil

CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
TMP_DIR = os.path.join(CURRENT_DIR, "tmp")



@pytest.fixture(scope="function", autouse=True)
def create_archive():
    if not os.path.exists('tmp'):
        os.mkdir('tmp')
    with zipfile.ZipFile('test.zip', 'w') as zf:
        for file in 'ТестовыйCSV.csv', 'ТестовыйPDF.pdf', 'ТестовыйXLSX.xlsx':
            add_file = os.path.join(TMP_DIR,file)
            zf.write(add_file, os.path.basename(add_file))
    shutil.move("test.zip", TMP_DIR)
    yield
    os.remove(TMP_DIR+'/test.zip')






