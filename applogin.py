# Data dictionary berisi username dan password mahasiswa
data_mahasiswa = {
    'nabilassgf': 'nblssgf10',
    'naiyla': 'nyl123',
    'riskawati': 'ika04',
    'wahdania': 'nia456',
    'nurmahda': 'nur05',
    'safril': 'ucup789',
    'ilham': 'bayisehat',
    'nabiltamim': 'nabil102',
    'manda': 'mnd03',
    'ella': 'elaila02'
}

# Fungsi untuk melakukan login
def login():
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")

    # Memeriksa keberadaan username dan password dalam data dictionary
    if username in data_mahasiswa and data_mahasiswa[username] == password:
        print("Selamat datang,", username)
    else:
        print("Data yang dimasukkan salah.")

# Memanggil fungsi login
login()