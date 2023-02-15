import unittest
from main import check_document_existance, get_doc_owner_name, add_new_shelf
from parameterized import parameterized


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_check_document_existance(self, input_, actual_):
        self.assertEqual(check_document_existance(input_), actual_)

    @parameterized.expand([
        ["2207 876234", True],
        ["11-2", True],
        ["10006", True],
        ["19906", False]
    ])
    def test_check_document_existance(self, input_, actual_):
        self.assertEqual(check_document_existance(input_), actual_)

    @parameterized.expand([
            ["2207 876234", "Василий Гупкин"],
            ["11-2", "Геннадий Покемонов"],
            ["10006", "Аристарх Павлов"],
            ["19906", None]
        ])
    def test_get_doc_owner_name(self, input_, actual_):
        self.assertEqual(get_doc_owner_name(input_), actual_)

    @parameterized.expand([
        ['4', ('4', True)],
        ['5', ('5', True)],
        ['3', ('3', False)]
        ]
    )
    def test_add_new_shelf(self, input_, actual_):
        self.assertEqual(add_new_shelf(input_), actual_)


result_p = 'Геннадий Покемонов'
result_a = 'документ 11-2 уже существует!'
result_d = 'Документ удален'


