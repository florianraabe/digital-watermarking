import cv2
from imwatermark import WatermarkDecoder, WatermarkEncoder

METHODS = ['dwtDct', 'dwtDctSvd', 'rivaGan']


def encode(filename: str, message: str, method: str) -> None:
    bgr = cv2.imread(filename)

    encoder = WatermarkEncoder()
    encoder.set_watermark('bytes', message.ljust(16).encode('utf-8'))
    bgr_encoded = encoder.encode(bgr, method)

    outfile = filename.split(".")
    outfile = "".join(outfile[:-1]) + "-watermarked." + outfile[-1]
    cv2.imwrite(outfile, bgr_encoded)
    print(f"Watermarked file: {outfile}")


def decode(filename: str, method: str) -> None:
    bgr = cv2.imread(filename)

    decoder = WatermarkDecoder('bytes', 16*8)
    watermark = decoder.decode(bgr, method)

    print(watermark.decode('utf-8'))
