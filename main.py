#!/usr/bin/env python3

import argparse
from typing import Sequence

import lsb


def main(argv: Sequence[str] | None = None) -> int:

    parser = argparse.ArgumentParser()

    subparsers = parser.add_subparsers(help='', dest="command")
    
    encode_parser = subparsers.add_parser('encode', help='encode watermark')
    encode_parser.add_argument('mode', choices=['lsb-text', 'lsb-image', 'alpha'], help='choose mode')
    encode_parser.add_argument('filename', help='path to file that should be watermarked')
    encode_parser.add_argument('message', help='watermark that should be embedded')
    
    decode_parser = subparsers.add_parser('decode', help='decode watermark')
    decode_parser.add_argument('mode', choices=['lsb-text', 'lsb-image', 'alpha'], help='choose mode')
    decode_parser.add_argument('filename', help='path to file that contains watermark')
    
    args = parser.parse_args(argv)

    if args.command == None:
        parser.print_help()
    else:
        # decide which command should be executed
        if args.command == "encode":
            print("Encoding watermark...")
            match args.mode:
                case "lsb-text":
                    lsb.insert_lsb_text(args.filename, args.message)
                case "lsb-image":
                    lsb.insert_lsb_image(args.filename, args.message)
                case "alpha":
                    lsb.insert_alpha_watermark(args.filename, args.message)
        elif args.command == "decode":
            print("Decoding watermark...")
            match args.mode:
                case "lsb-text":
                    lsb.extract_lsb_text(args.filename)
                case "lsb-image":
                    lsb.extract_lsb_image(args.filename)
                case "alpha":
                    lsb.remove_alpha_watermark(args.filename)
    
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
