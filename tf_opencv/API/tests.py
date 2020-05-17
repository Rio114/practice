import unittest

from generate_sr_image import SrImage

class TestStringMethods(unittest.TestCase):

    def test_jpg(self):
        image_file = 'test.jpg'
        obj = SrImage()
        self.assertEqual(obj.generate(image_file), 'test_r.jpg')

    def test_txt(self):
        image_file = 'test.txt'
        obj = SrImage()
        self.assertEqual(obj.generate(image_file), False)

    def test_nofile(self):
        image_file = 'hoge.jpg'
        obj = SrImage()
        self.assertEqual(obj.generate(image_file), False)

if __name__ == '__main__':
    unittest.main()