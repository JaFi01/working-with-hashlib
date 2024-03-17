#This is task, to check if linux .iso file which I'be downloaded has correct hash
#Path implied here is specific to me, as I run this on my own mahine via WSL

import hashlib

CORRECT_HASH = 'b284afcc298cc6f5da6ab4d483318c453b2074485974b71b16fdfc7256527cb1' # *linuxmint-21.3-xfce-64bit.iso from https://ftp.heanet.ie/mirrors/linuxmint.com/stable/21.3/sha256sum.txt


def calculate_file_hash(file_path):
    """Funkction calculating hash SHA-256 for choosen file.

    Args:
        file_path (str): Path to file.

    Returns:
        str: Hash SHA-256 for file.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def main():
    path_to_file = "/mnt/c/Users/jaros/Downloads/linuxmint-21.3-xfce-64bit.iso"
    file_hash = calculate_file_hash(path_to_file)

    if file_hash == CORRECT_HASH:
        print("Hash is correct!")
    else:
        print("Hash is incorrect.")

if __name__ == "__main__":
    main()