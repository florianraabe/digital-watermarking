from PIL import Image

METHODS = ['lsb', 'lsb-image']


def encode_text(filename: str, message: str) -> Image:
    
    image = Image.open(filename)
    pixels = image.load()

    watermarked_image = Image.new('RGB', (image.width, image.height), 'black')
    watermarked_pixels = watermarked_image.load()

    bits = ''.join(format(ord(i), '08b') for i in message)

    outfile = filename.split(".")

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b = pixels[x, y]

            index = (x * image.height + y) % len(bits)

            r = int(f'{r:08b}'[:7] + f'{bits}'[index: index + 1], 2)
            # g = int(f'{g:08b}'[:7] + f'{bits}'[index: index + 1], 2)
            # b = int(f'{b:08b}'[:7] + f'{bits}'[index: index + 1], 2)

            watermarked_pixels[x, y] = (r, g, b)

    outfile = "".join(outfile[:-1]) + "-watermarked." + outfile[-1]
    watermarked_image.save(outfile)
    print(f"Watermarked file: {outfile}")

    return watermarked_image


def decode_text(filename: str) -> str:
    
    image = Image.open(filename)
    pixels = image.load()

    message = ""
    bits = ""

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b, *_ = pixels[x, y]

            bits += f'{r:08b}'[7:8]
            # bits += f'{g:08b}'[7:8]
            # bits += f'{b:08b}'[7:8]

    for i in range(0, len(bits), 8):
        message += chr(int(bits[i:i + 8], 2))

    return message


def encode_image(filename: str, watermark: str) -> None:

    image = Image.open(filename)
    pixels = image.load()

    watermark_image = Image.open(watermark)
    watermark_pixels = watermark_image.load()

    watermarked_image = Image.new('RGB', (image.width, image.height), 'black')
    watermarked_pixels = watermarked_image.load()

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b = pixels[x, y]
            r2, g2, b2 = watermark_pixels[x, y]

            r = int(f'{r:08b}'[:4] + f'{r2:08b}'[:4], 2)
            g = int(f'{g:08b}'[:4] + f'{g2:08b}'[:4], 2)
            b = int(f'{b:08b}'[:4] + f'{b2:08b}'[:4], 2)

            watermarked_pixels[x, y] = (r, g, b)

    outfile = filename.split(".")
    outfile = "".join(outfile[:-1]) + "-watermarked." + outfile[-1]
    watermarked_image.save(outfile)
    print(f"Watermarked file: {outfile}")


def decode_image(filename: str) -> None:

    image = Image.open(filename)
    pixels = image.load()

    watermark = Image.new('RGB', (image.width, image.height), 'black')
    watermark_pixels = watermark.load()

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b = pixels[x, y]

            r = int(f'{r:08b}'[4:8] + f'0000', 2)
            g = int(f'{g:08b}'[4:8] + f'0000', 2)
            b = int(f'{b:08b}'[4:8] + f'0000', 2)

            watermark_pixels[x, y] = (r, g, b)

    watermark.save(f"watermark.png")
