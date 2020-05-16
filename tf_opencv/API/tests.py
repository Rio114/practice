import unittest

from gen_sr_image import SrImage

class TestStringMethods(unittest.TestCase):

    def test_jpg(self):
        image_file = 'test.jpg'
        obj = SrImage(image_file)
        self.assertEqual(obj.generate(), 'test_r.jpg')

    def test_txt(self):
        image_file = 'test.txt'
        obj = SrImage(image_file)
        self.assertEqual(obj.generate(), False)

    def test_nofile(self):
        image_file = 'hoge.jpg'
        obj = SrImage(image_file)
        self.assertEqual(obj.generate(), False)

if __name__ == '__main__':
    unittest.main()