import re

with open("/Users/rismaniswaty/TUTORIAL-SARJUN/ringkasan-v1.md", "r") as f:
    text = f.read()

text = text.replace("# Ringkasan Sesi Penyusunan Artikel — V1", "# Ringkasan Sesi Penyusunan Artikel — V2")

text = text.replace("Menyusun **draft pertama artikel ilmiah**", "Menyusun dan merevisi **draft artikel ilmiah (V2)**")
text = text.replace("Pada tahap ini, **teori dan rujukan belum dimasukkan secara penuh** -- hanya ditandai dengan format `(*NAMA TEORI / SUMBER RUJUKAN*)` agar mudah dilengkapi di revisi berikutnya.", "Pada tahap ini, bagian tinjauan pustaka telah disusun komprehensif, seluruh placeholder teori telah diintegrasikan menjadi kutipan standar akademis (APA Style), dan Daftar Pustaka lengkap telah ditambahkan.")

text = text.replace("- [X] Output tersimpan di: **`DRAFT-ARTIKEL-V1.md`**", "- [X] Output tersimpan di: **`DRAFT-ARTIKEL-V1.md`**\n- [X] Melengkapi Tinjauan Pustaka (Literature Review) dengan lebih dari 20 referensi\n- [X] Mengganti seluruh placeholder teori pendukung menjadi in-text citation yang benar\n- [X] Menyusun Daftar Pustaka (Bibliography)\n- [X] Output versi terbaru tersimpan di: **`DRAFT-ARTIKEL-V2.md`**")

text = text.replace("| 1  | **Literature Review**                  | Belum         | Perlu diisi dengan tinjauan pustaka lengkap (minimal 15--20 rujukan) |", "| 1  | **Literature Review**                  | Selesai       | Telah diisi dengan tinjauan pustaka lengkap (>20 rujukan) |")
text = text.replace("| 2  | **Teori-teori pendukung**              | Ditandai saja | Masih dalam format placeholder `(*...*)`                           |", "| 2  | **Teori-teori pendukung**              | Selesai       | Telah diintegrasikan ke dalam teks beserta sitasi |")
text = text.replace("| 5  | **Daftar Pustaka**                     | Belum         | Menunggu teori dan rujukan final                                     |", "| 5  | **Daftar Pustaka**                     | Selesai       | Telah ditambahkan di bagian akhir artikel |")

text = text.replace("`DRAFT-ARTIKEL-V1.md`", "`DRAFT-ARTIKEL-V2.md`")

with open("/Users/rismaniswaty/TUTORIAL-SARJUN/ringkasan-v2.md", "w") as f:
    f.write(text)

print("Ringkasan updated successfully")
