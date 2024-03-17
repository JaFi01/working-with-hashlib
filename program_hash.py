import hashlib
#This is task, to check if linux .iso file which I'be downloaded has correct hash
#Path implied in this script is specific to me, as I run this on my own mahine via WSL

CORRECT_HASH = 'b284afcc298cc6f5da6ab4d483318c453b2074485974b71b16fdfc7256527cb1' # *linuxmint-21.3-xfce-64bit.iso from https://ftp.heanet.ie/mirrors/linuxmint.com/stable/21.3/sha256sum.txt


def calculate_file_hash(file_path):
    """Calculate the SHA-256 hash for a given binary file.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: SHA-256 hash for the File.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


def main():
    path_to_file = "/mnt/c/Users/jaros/Downloads/linuxmint-21.3-xfce-64bit.iso"
    choice = input("Enter 'h' to check if hash is correct or 'r' to read the hash of the file: ").strip().lower()
    if choice == 'h':
        file_hash = calculate_file_hash(path_to_file)
        if file_hash == CORRECT_HASH:
            print("Hash is correct!")
        else:
            print("Hash is incorrect.")
        #print("File hash:", file_hash)
    elif choice == 'r':
        file_hash = calculate_file_hash(path_to_file)
        print("Hash of the file:", file_hash)
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()