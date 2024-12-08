#!/usr/bin/env python3

import argparse
from typing import Sequence

import alpha
import dct
import lsb
import tests


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='', dest="command")

    choices = alpha.METHODS + lsb.METHODS + dct.METHODS
    
    encode_parser = subparsers.add_parser('encode', help='encode watermark')
    encode_parser.add_argument('mode', choices=choices, help='choose mode')
    encode_parser.add_argument('filename', help='path to file that should be watermarked')
    encode_parser.add_argument('message', help='watermark that should be embedded')
    
    decode_parser = subparsers.add_parser('decode', help='decode watermark')
    decode_parser.add_argument('mode', choices=choices, help='choose mode')
    decode_parser.add_argument('filename', help='path to file that contains watermark')

    subparsers.add_parser('test', help='execute the tests')
    
    args = parser.parse_args(argv)

    if args.command == None:
        parser.print_help()
    else:
        # decide which command should be executed
        if args.command == "encode":
            print("Encoding watermark...")
            match args.mode:
                case "lsb-text":
                    lsb.encode_text(args.filename, args.message)
                case "lsb-image":
                    lsb.encode_image(args.filename, args.message)
                case "alpha":
                    alpha.encode(args.filename, args.message)
                case _:
                    if args.mode in choices:
                        dct.encode(args.filename, args.message, args.mode)
        elif args.command == "decode":
            print("Decoding watermark...")
            match args.mode:
                case "lsb-text":
                    lsb.decode_text(args.filename)
                case "lsb-image":
                    lsb.decode_image(args.filename)
                case "alpha":
                    alpha.decode(args.filename)
                case _:
                    if args.mode in choices:
                        dct.decode(args.filename, args.mode)
        elif args.command == "test":
            print("Running tests...")
            tests.test()
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
