from blind_watermark import WaterMark, bw_notes
from PIL import Image

###############################################################################
#               https://github.com/guofei9987/blind_watermark                 #
###############################################################################

METHODS = ['lib3']


def encode(filename: str, message: str) -> None:
    bw_notes.close()
    bwm1 = WaterMark(password_img=1, password_wm=1)
    bwm1.read_img(filename)
    bwm1.read_wm(message[:16].ljust(16), mode='str')

    outfile = filename.split(".")
    outfile = "".join(outfile[:-1]) + "-watermarked." + outfile[-1]
    bwm1.embed(outfile)
    print(f"Watermarked file: {outfile}")

    return Image.open(outfile)


def decode(filename: str) -> None:
    bw_notes.close()
    bwm1 = WaterMark(password_img=1, password_wm=1)
    wm_extract = bwm1.extract(filename, wm_shape=127, mode='str')

    return wm_extract