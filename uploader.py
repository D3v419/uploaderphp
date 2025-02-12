import requests

def upload_file(website, file_name, file_content):
    # Buat URL untuk upload
    upload_url = f"http://{website}/upload.php"

    # Buat payload untuk upload
    files = {
        'file': (file_name, file_content, 'application/x-php')
    }

    # Kirim permintaan POST ke server
    response = requests.post(upload_url, files=files)

    # Cek status kode respons
    if response.status_code == 200:
        print(f"File {file_name} berhasil diupload ke {website}")
        print(f"Link untuk melihat file: http://{website}/{file_name}")
    else:
        print(f"Gagal mengupload file. Status kode: {response.status_code}")

# Contoh penggunaan
website = input("Masukkan nama website (contoh: example.com): ")
file_name = input("Masukkan nama file PHP (contoh: shell.php): ")
file_content = input("Masukkan konten file PHP (contoh: <?php echo 'Hello, World!'; ?>): ")

upload_file(website, file_name, file_content)
