from PIL import (Image, ImageDraw, ImageEnhance, ImageFile, ImageFilter,
                 ImageFont)


def rotate(image: ImageFile, angle: int) -> Image:
    return image.rotate(angle)


def jpeg_compress(image: Image) -> Image:
    return image.convert('RGB')


def noise(image: Image) -> Image:
    return image.filter(ImageFilter.GaussianBlur(5))


def brightness(image: Image) -> Image:
    enhancer = ImageEnhance.Brightness(image)
    return enhancer.enhance(0.5)


def overlay(image: Image) -> Image:
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("assets/Font/FreeMono.ttf", 64)
    draw.text((48, 256),"Sample Text",(255,255,255),font=font)
    return image


def mask(image: Image) -> Image:
    image.putalpha(128)
    return image


def crop(image: Image) -> Image:
    return image.crop((64, 64, 256, 256))


def resize(image: Image) -> Image:
    width, height = image.size
    new_size = (width//2, height//2)
    return image.resize(new_size)
