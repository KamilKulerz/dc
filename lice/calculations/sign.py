from base64 import b64encode
import rsa
from lice.calculations.helpers import read_from_file, write_to_file, private_key_from_file
import pyqrcode
import png
from pyqrcode import QRCode
import pathlib


def sign_data(data, private_key):
    signature = rsa.sign(data.encode('utf-8'), private_key, 'SHA-1')
    return data, signature


def sign_data_to_str(data):

    private_key = private_key_from_file(pathlib.Path(
        __file__).resolve().parent / 'private_key')
    signed_data, signature = sign_data(data, private_key)
    return f'{b64encode(signature).decode("ascii")}'


if __name__ == '__main__':
    data = 'test.test.123456789'
    data = input('Provide license data for signing: ')
    private_key = private_key_from_file('private_key')
    signed_data, signature = sign_data(data, private_key)

    license = f'{signed_data}...{b64encode(signature).decode("ascii")}'
    qrcode_data = pyqrcode.create(license)
    qrcode_data.png('signed_data.png', scale=6)

    write_to_file(license.encode(), 'license')
    write_to_file(signature, 'signature')
    write_to_file(signed_data.encode(), 'data')
