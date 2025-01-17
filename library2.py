import cv2
from imwatermark import WatermarkDecoder, WatermarkEncoder
from PIL import Image

###############################################################################
#            https://github.com/ShieldMnt/invisible-watermark                 #
###############################################################################

METHODS = ['dwtDct', 'dwtDctSvd']


def encode(filename: str, message: str, method: str) -> Image:
    bgr = cv2.imread(filename)

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', message[:4].encode('utf-8'))
    bgr_encoded = encoder.encode(bgr, method)

    outfile = filename.split(".")
    outfile = "".join(outfile[:-1]) + "-watermarked." + outfile[-1]
    cv2.imwrite(outfile, bgr_encoded)
    print(f"Watermarked file: {outfile}")

    return Image.fromarray(bgr_encoded)


def decode(filename: str, method: str) -> str:
    bgr = cv2.imread(filename)

    decoder = WatermarkDecoder('bytes', 32)
    watermark = decoder.decode(bgr, method)

    try:
        watermark = watermark.decode('utf-8')
    except UnicodeDecodeError as e:
        pass

    return watermark
