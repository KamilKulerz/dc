import rsa


def private_key_from_file(filepath):
    with open(filepath, 'rb') as f:
        pk = rsa.PrivateKey.load_pkcs1(f.read(), format='PEM')
    return pk


def public_key_to_file(public_key, filepath):
    with open(filepath, 'wb+') as f:
        pk = rsa.PublicKey.save_pkcs1(public_key, format='PEM')
        f.write(pk)


def private_key_to_file(public_key, filepath):
    with open(filepath, 'wb+') as f:
        pk = rsa.PrivateKey.save_pkcs1(public_key, format='PEM')
        f.write(pk)


def public_key_from_file(filepath):
    with open(filepath, 'rb') as f:
        pk = rsa.PublicKey.load_pkcs1(f.read(), format='PEM')
    return pk


def write_to_file(data, filename):
    with open(filename, 'wb+') as f:
        f.write(data)


def read_from_file(filename):
    with open(filename, 'rb+') as f:
        data = f.read()
    return data
