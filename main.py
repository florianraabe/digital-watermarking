#!/usr/bin/env python3

import argparse
from typing import Sequence

import library1
import library2
import library3


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='', dest="command")

    choices = library1.METHODS + library2.METHODS + library3.METHODS
    
    encode_parser = subparsers.add_parser('encode', help='encode watermark')
    encode_parser.add_argument('mode', choices=choices, help='choose mode')
    encode_parser.add_argument('filename', help='path to file that should be watermarked')
    encode_parser.add_argument('message', help='watermark that should be embedded')
    
    decode_parser = subparsers.add_parser('decode', help='decode watermark')
    decode_parser.add_argument('mode', choices=choices, help='choose mode')
    decode_parser.add_argument('filename', help='path to file that contains watermark')

    args = parser.parse_args(argv)

    if args.command == None:
        parser.print_help()
    else:
        # decide which command should be executed
        if args.command == "encode":
            print("Encoding watermark...")
            match args.mode:
                case "lsb":
                    library1.encode_text(args.filename, args.message)
                case "lsb-image":
                    library1.encode_image(args.filename, args.message)
                case "lib3":
                    library3.encode(args.filename, args.message)
                case _:
                    if args.mode in choices:
                        library2.encode(args.filename, args.message, args.mode)
        elif args.command == "decode":
            print("Decoding watermark...")
            match args.mode:
                case "lsb":
                    watermark = library1.decode_text(args.filename)
                    print(watermark)
                case "lsb-image":
                    watermark = library1.decode_image(args.filename)
                    print(watermark)
                case "lib3":
                    watermark = library3.decode(args.filename)
                    print(watermark)
                case _:
                    if args.mode in choices:
                        watermark = library2.decode(args.filename, args.mode)
                        print(watermark)
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
