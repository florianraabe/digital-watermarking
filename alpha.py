from PIL import Image

METHODS = ['alpha']


def encode(filename: str, watermark: str) -> None:

    image = Image.open(filename)
    pixels = image.load()

    watermark_image = Image.open(watermark)
    watermark_pixels = watermark_image.load()

    watermarked_image = Image.new('RGBA', (image.width, image.height), 'black')
    watermarked_pixels = watermarked_image.load()

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b = pixels[x, y]
            r2, g2, b2, alpha = watermark_pixels[(x % watermark_image.width), (y % watermark_image.height)]
            
            if r2 == g2 == b2 == 0:
                alpha = 200

            watermarked_pixels[x, y] = (r, g, b, alpha)

    outfile = filename.split(".")
    outfile = "".join(outfile[:-1]) + "-watermarked." + outfile[-1]
    watermarked_image.save(outfile)
    print(f"Watermarked file: {outfile}")


def decode(filename: str) -> None:

    image = Image.open(filename)
    pixels = image.load()

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b, _ = pixels[x, y]

            pixels[x, y] = (r, g, b, 255)

    outfile = filename.split(".")
    outfile = "".join(outfile[:-1]) + "-no-watermark." + outfile[-1]
    image.save(outfile)
