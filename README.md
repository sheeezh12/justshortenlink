# justshortenlink


Sebuah aplikasi web sederhana untuk mempersingkat URL menggunakan Flask. Link yang dipendekkan memiliki masa berlaku (expire date), disimpan dalam format JSON, dan dapat diakses melalui routing dinamis.

## Fitur

- Input URL asli dan tanggal kedaluwarsa via form HTML
- Generate kode pendek acak (6 karakter) dari angka dan huruf
- Penyimpanan data di file JSON.
- Routing dinamis /abc123:
- Redirect ke origin jika link masih aktif
- Tampilkan halaman expired (HTTP 410) jika sudah lewat
- Tampilkan halaman 404 jika kode tidak ditemukan
- Section hasil pemendekan muncul otomatis di halaman utama
- Validasi input expire-date dengan format MM/DD/YYYY
- Status HTTP sesuai kondisi (200, 404, 410)

## Tech / tools

- Bootstrap 
- Flask
- HTML, CSS, JavaScript

