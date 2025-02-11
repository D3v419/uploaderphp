import requests
import os

def upload_file(website, filename, filepath):
    """Mengunggah file ke situs web.

    Args:
        website: Alamat situs web (contoh: "http://example.com").
        filename: Nama file yang akan diunggah (contoh: "shell.php").
        filepath: Path lengkap ke file yang akan diunggah.
    """

    try:
        with open(filepath, "rb") as f:
            files = {"file": (filename, f)}
            response = requests.post(f"{website}/path/to/upload/script.php", files=files)

            if response.status_code == 200:
                print(f"Berhasil mengunggah {filename} ke {website}")
                print(f"Link: {website}/path/to/uploaded/{filename}")
            else:
                print(f"Gagal mengunggah {filename} ke {website}")
                print(response.text)

    except FileNotFoundError:
        print(f"File {filepath} tidak ditemukan.")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan saat menghubungi {website}: {e}")

if __name__ == "__main__":
    website = input("Masukkan alamat situs web: ")
    filename = input("Masukkan nama file PHP: ")
    filepath = input("Masukkan path lengkap ke file PHP: ")

    if not os.path.exists(filepath):
        print(f"File {filepath} tidak ditemukan.")
    else:
        upload_file(website, filename, filepath)
