import os
import shutil
import tempfile
import unittest

import library1
import library2
import library3
import manipulation

TESTWATERMARK = "test"
TESTFILE = "assets/test.png"


class BaseTestCases:

    class TestWatermarkMethods(unittest.TestCase):

        def watermark_function(self, function, argv = []):
            pass

        def test(self):
            self.assertEqual(self.watermark_function(lambda x: x), TESTWATERMARK, "Watermark not matching!")

        def test_rotate(self):
            self.assertEqual(self.watermark_function(manipulation.rotate, [30]), TESTWATERMARK, "Watermark not matching!")

        def test_jpegcompress(self):
            self.assertEqual(self.watermark_function(manipulation.jpeg_compress), TESTWATERMARK, "Watermark not matching!")

        def test_noise(self):
            self.assertEqual(self.watermark_function(manipulation.noise), TESTWATERMARK, "Watermark not matching!")

        def test_brightness(self):
            self.assertEqual(self.watermark_function(manipulation.brightness), TESTWATERMARK, "Watermark not matching!")

        def test_overlay(self):
            self.assertEqual(self.watermark_function(manipulation.overlay), TESTWATERMARK, "Watermark not matching!")

        def test_mask(self):
            self.assertEqual(self.watermark_function(manipulation.mask), TESTWATERMARK, "Watermark not matching!")

        def test_crop(self):
            self.assertEqual(self.watermark_function(manipulation.crop), TESTWATERMARK, "Watermark not matching!")

        def test_resize(self):
            self.assertEqual(self.watermark_function(manipulation.resize), TESTWATERMARK, "Watermark not matching!")


class TestLibrary1(BaseTestCases.TestWatermarkMethods):

    def watermark_function(self, function, argv = []):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy file to temporary directory
            os.makedirs(os.path.dirname(os.path.join(tmpdir, TESTFILE)), exist_ok=True)
            shutil.copyfile(TESTFILE, os.path.join(tmpdir, TESTFILE))
            # embed the watermark
            img = library1.encode_text(os.path.join(tmpdir, TESTFILE), TESTWATERMARK)
            # manipulate the watermarked file
            img = function(img, *argv)
            img.save(os.path.join(tmpdir, "test.png"))
            # try to decode the watermark
            watermark = library1.decode_text(os.path.join(tmpdir, "test.png"))

        return watermark[:len(TESTWATERMARK)]


class TestLibrary2a(BaseTestCases.TestWatermarkMethods):

    def watermark_function(self, function, argv = []):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy file to temporary directory
            os.makedirs(os.path.dirname(os.path.join(tmpdir, TESTFILE)), exist_ok=True)
            shutil.copyfile(TESTFILE, os.path.join(tmpdir, TESTFILE))
            # embed the watermark
            img = library2.encode(os.path.join(tmpdir, TESTFILE), TESTWATERMARK, "dwtDct")
            # manipulate the watermarked file
            img = function(img, *argv)
            img.save(os.path.join(tmpdir, "test.png"))
            # try to decode the watermark
            watermark = library2.decode(os.path.join(tmpdir, "test.png"), "dwtDct")

        return watermark[:len(TESTWATERMARK)]


class TestLibrary2b(BaseTestCases.TestWatermarkMethods):

    def watermark_function(self, function, argv = []):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy file to temporary directory
            os.makedirs(os.path.dirname(os.path.join(tmpdir, TESTFILE)), exist_ok=True)
            shutil.copyfile(TESTFILE, os.path.join(tmpdir, TESTFILE))
            # embed the watermark
            img = library2.encode(os.path.join(tmpdir, TESTFILE), TESTWATERMARK, "dwtDctSvd")
            # manipulate the watermarked file
            img = function(img, *argv)
            img.save(os.path.join(tmpdir, "test.png"))
            # try to decode the watermark
            watermark = library2.decode(os.path.join(tmpdir, "test.png"), "dwtDctSvd")

        return watermark[:len(TESTWATERMARK)]


class TestLibrary2c(BaseTestCases.TestWatermarkMethods):

    def watermark_function(self, function, argv = []):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy file to temporary directory
            os.makedirs(os.path.dirname(os.path.join(tmpdir, TESTFILE)), exist_ok=True)
            shutil.copyfile(TESTFILE, os.path.join(tmpdir, TESTFILE))
            # embed the watermark
            img = library2.encode(os.path.join(tmpdir, TESTFILE), TESTWATERMARK, "rivaGan")
            # manipulate the watermarked file
            img = function(img, *argv)
            img.save(os.path.join(tmpdir, "test.png"))
            # try to decode the watermark
            watermark = library2.decode(os.path.join(tmpdir, "test.png"), "rivaGan")

        return watermark[:len(TESTWATERMARK)]


class TestLibrary3(BaseTestCases.TestWatermarkMethods):

    def watermark_function(self, function, argv = []):
        with tempfile.TemporaryDirectory() as tmpdir:
            # copy file to temporary directory
            os.makedirs(os.path.dirname(os.path.join(tmpdir, TESTFILE)), exist_ok=True)
            shutil.copyfile(TESTFILE, os.path.join(tmpdir, TESTFILE))
            # embed the watermark
            img = library3.encode(os.path.join(tmpdir, TESTFILE), TESTWATERMARK)
            # manipulate the watermarked file
            img = function(img, *argv)
            img.save(os.path.join(tmpdir, "test.png"))
            # try to decode the watermark
            watermark = library3.decode(os.path.join(tmpdir, "test.png"))

        return watermark[:len(TESTWATERMARK)]


# class TestExportImages(BaseTestCases.TestWatermarkMethods):

#     def watermark_function(self, function, argv = []):
#         from PIL import Image
#         img = Image.open(TESTFILE)
#         img = function(img, *argv)
#         img.save(f"{function}.png")
#         return TESTWATERMARK


if __name__ == '__main__':
    unittest.main()