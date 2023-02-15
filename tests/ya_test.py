import unittest
from ya import createfolder, get_folder_info

DIRNAME = 'testdir'

class YandexAPITest(unittest.TestCase):
    def test_createfolder(self):
        result = createfolder(DIRNAME)
        self.assertTrue(result == 201, f'Ответ сервера: {result}')

    def test_get_folder_info(self):
        self.assertTrue(get_folder_info(DIRNAME) == 'testdir')