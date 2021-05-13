import unittest
import error_code_handler as hander


class TestMath(unittest.TestCase):

    def test_type1(self):
        result = hander.ErrorCode.error_1.value
        self.assertEqual((1, 'error_example'), result)

    def test_type2(self):
        result = hander.error_code_packer(
            hander.ErrorCode.error_2, {'group_id': '12345'})
        self.assertEqual((2, 'example: 12345'), result)

    def test_type3(self):
        error_msg = "others error example"
        result = hander.error_code_packer(
            hander.ErrorCode.others, {'msg': error_msg})
        self.assertEqual((10001, 'others error example'), result)


if __name__ == '__main__':
    unittest.main()
