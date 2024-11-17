from PIL import Image


def insert_lsb_text(filename: str, message: str) -> None:
    
    image = Image.open(filename)
    pixels = image.load()

    watermarked_image = Image.new('RGB', (image.width, image.height), 'black')
    watermarked_pixels = watermarked_image.load()

    bits = ''.join(format(ord(i), '08b') for i in message)

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b = pixels[x, y]

            index = (x * image.height + y) % len(bits)

            r = int(f'{r:08b}'[:7] + f'{bits}'[index: index + 1], 2)
            # g = int(f'{g:08b}'[:7] + f'{bits}'[index: index + 1], 2)
            # b = int(f'{b:08b}'[:7] + f'{bits}'[index: index + 1], 2)

            watermarked_pixels[x, y] = (r, g, b)

    watermarked_image.save(f"{filename}-watermark.png")


def extract_lsb_text(filename: str) -> None:
    
    image = Image.open(filename)
    pixels = image.load()

    message = ""
    bits = ""

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b = pixels[x, y]

            bits += f'{r:08b}'[7:8]
            # bits += f'{g:08b}'[7:8]
            # bits += f'{b:08b}'[7:8]

    for i in range(0, len(bits), 8):
        message += chr(int(bits[i:i + 8], 2))

    print(message)


def insert_lsb_image(filename: str, watermark: str) -> None:

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

    watermarked_image.save(f"{filename}-watermark.png")


def extract_lsb_image(filename: str) -> None:

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


def insert_alpha_watermark(filename: str, watermark: str) -> None:

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
                alpha = 127

            watermarked_pixels[x, y] = (r, g, b, alpha)

    watermarked_image.save(f"{filename}-watermark.png")


def remove_alpha_watermark(filename: str) -> None:

    image = Image.open(filename)
    pixels = image.load()

    for x in range(0, image.width):
        for y in range(0, image.height):
            r, g, b, _ = pixels[x, y]

            pixels[x, y] = (r, g, b, 255)

    image.save(f"{filename}-no-watermark.png")