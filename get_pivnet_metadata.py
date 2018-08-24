#!/usr/bin/env python3
import httpio
import argparse

from zipfile import ZipFile
if __name__ == "__main__":
        parser = argparse.ArgumentParser(description='Get pivnet metadata.',
                                         epilog="example: ./get_pivnet_metadata.py --url 'https://network.pivotal.io/api/v2/products/elastic-runtime/releases/160817/product_files/193873/download' --token 'xxx'")
        parser.add_argument('--url',
                            help='download api link', required=True)
        parser.add_argument('--token',
                            help='Pivnet Legacy API Token', required=True)
        args = parser.parse_args()

        with httpio.open(args.url, allow_redirects=True, headers={ "Authorization" : "Token " + args.token}) as f:
            zf = ZipFile(f)
            contents = zf.read("metadata/metadata.yml")
            print(contents.decode('utf-8'))
