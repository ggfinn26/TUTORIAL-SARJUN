# Paradoks Transisi Energi dan Kegagalan Decoupling Emisi Karbon di Indonesia: Bukti Empiris dari Model ARDL (2010-2024)

---

## 1. LATAR BELAKANG

Perubahan iklim merupakan tantangan eksistensial abad ke-21 yang menuntut setiap negara untuk merekonsiliasi ambisi pertumbuhan ekonomi dengan komitmen reduksi emisi gas rumah kaca. Indonesia, sebagai ekonomi terbesar di Asia Tenggara dan salah satu emiter karbon dioksida (CO2) terbesar di dunia, menghadapi dilema fundamental: dapatkah negara ini terus bertumbuh tanpa mengorbankan lingkungan?

(*Teori Environmental Kuznets Curve / EKC -- Grossman & Krueger, 1991; 1995*)

Hipotesis Environmental Kuznets Curve (EKC) mendalilkan bahwa hubungan antara pertumbuhan ekonomi dan degradasi lingkungan membentuk kurva U-terbalik. Pada fase awal industrialisasi, peningkatan pendapatan per kapita disertai eskalasi polusi. Namun, setelah melampaui titik balik (turning point) tertentu, pertumbuhan ekonomi justru diikuti oleh penurunan polusi -- seiring transisi struktural ekonomi dari sektor padat karbon menuju sektor jasa dan teknologi bersih.

(*Sumber rujukan tentang posisi Indonesia sebagai emiter global -- EDGAR / Global Carbon Project, data terbaru*)

Data empiris menunjukkan bahwa emisi CO2 Indonesia mengalami eskalasi persisten selama periode 2010-2024. Total emisi meningkat dari 543,9 juta ton CO2 pada tahun 2010 menjadi 920,9 juta ton CO2 pada tahun 2024 -- suatu lonjakan sebesar 69,3% dalam kurun waktu lima belas tahun. Tren ini berlangsung nyaris tanpa interupsi, bahkan ketika ekonomi mengalami kontraksi akibat pandemi COVID-19 pada tahun 2020 (emisi hanya turun sementara ke 694,3 juta ton sebelum kembali melonjak).

(*Sumber data emisi CO2 Indonesia -- Kementerian ESDM / BPS / EDGAR Database*)

Di sisi lain, Indonesia telah mencanangkan target ambisius dalam bauran energi baru dan terbarukan (EBT). Penetrasi EBT dalam bauran energi nasional meningkat dari 5,4% pada tahun 2010 menjadi 14,68% pada tahun 2024.

(*Sumber rujukan kebijakan EBT Indonesia -- Perpres No. 22/2017, RUEN, NDC Indonesia di Paris Agreement*)

Namun, pertanyaan kritis yang muncul adalah: apakah peningkatan penetrasi EBT ini benar-benar efektif dalam mereduksi emisi karbon? Ataukah justru terjadi paradoks di mana penambahan kapasitas energi terbarukan tidak serta-merta menurunkan ketergantungan pada energi fosil?

(*Teori Jevons Paradox -- William Stanley Jevons, 1865; literatur modern tentang Rebound Effect dan Backfire Effect*)

Berangkat dari kerangka teoritis tersebut, penelitian ini bertujuan untuk menguji dua hipotesis utama:

1. **Bagaimana korelasi pertumbuhan ekonomi (PDB) dengan emisi CO2 di Indonesia?** -- Apakah hipotesis EKC berlaku, atau justru Indonesia masih terjebak dalam fase ascending curve?
2. **Bagaimana korelasi penetrasi energi baru terbarukan (EBT) dengan emisi CO2?** -- Apakah transisi energi hijau berhasil menjadi instrumen dekarbonisasi, atau justru memicu efek rebound?

(*Sumber rujukan urgensi -- konteks Indonesia sebagai negara G20, komitmen Net Zero Emission 2060, ketergantungan fiskal pada sektor ekstraktif batu bara dan nikel*)

Urgensi penelitian ini semakin mendesak mengingat Indonesia masih sangat bergantung pada ekspor komoditas ekstraktif padat karbon, khususnya batu bara dan nikel. Struktur ekonomi yang berbasis pada ekstraksi sumber daya alam menciptakan apa yang dikenal sebagai *carbon lock-in* -- suatu kondisi di mana infrastruktur dan kepentingan ekonomi-politik yang ada mengunci perekonomian pada trajektori tinggi karbon, sehingga transisi menuju ekonomi hijau menjadi jauh lebih sulit dan mahal.

(*Teori Carbon Lock-in -- Unruh, 2000; 2002*)

---

## 2. LITERATURE REVIEW

(*BAGIAN INI AKAN DIISI DENGAN TINJAUAN PUSTAKA. Teori dan rujukan yang perlu dibahas meliputi:*)

1. (*Teori Environmental Kuznets Curve -- evolusi dari Grossman & Krueger hingga studi kontemporer di negara berkembang*)
2. (*Studi empiris EKC di Indonesia dan negara ASEAN -- hasil yang mendukung dan menolak hipotesis EKC*)
3. (*Teori Jevons Paradox dan Rebound Effect dalam konteks energi terbarukan -- Sorrell, 2009; Gillingham et al., 2016*)
4. (*Konsep Carbon Lock-in dan Path Dependency -- Unruh, 2000; Seto et al., 2016*)
5. (*Studi terdahulu tentang hubungan EBT dan emisi CO2 -- apakah ada bukti backfire effect di negara lain?*)
6. (*Aplikasi metode ARDL dalam studi lingkungan-ekonomi -- Pesaran et al., 2001*)
7. (*Kebijakan energi Indonesia -- RUEN, RUPTL, dan target NDC*)

---

## 3. METHOD, DATA, DAN ANALISIS

### 3.1 Metode Penelitian

Penelitian ini mengadopsi pendekatan kuantitatif dengan menggunakan model **Autoregressive Distributed Lag (ARDL)** yang diperkenalkan oleh Pesaran, Shin, dan Smith (2001). Pemilihan metode ARDL dilandasi oleh beberapa keunggulan teknis:

(*Pesaran, Shin & Smith, 2001 -- ARDL Bounds Testing Approach*)

- ARDL mampu mengakomodasi variabel dengan derajat integrasi campuran, yakni I(0) dan I(1), selama tidak ada variabel yang terintegrasi pada derajat I(2).
- Pendekatan ini secara simultan dapat mengestimasi hubungan jangka pendek (short-run dynamics) dan jangka panjang (long-run equilibrium) dalam satu kerangka model.
- ARDL tetap menghasilkan estimator yang konsisten dan efisien meskipun diaplikasikan pada sampel berukuran kecil (*small sample size*).

### 3.2 Data

Penelitian ini menggunakan data runtun waktu (*time series*) tahunan selama periode 2010-2024 (T = 15 observasi). Variabel yang digunakan meliputi:

| **Variabel** | **Proksi** | **Satuan** | **Sumber** |
|---|---|---|---|
| Emisi Karbon (LN_CO2) | Total emisi CO2 Indonesia | Juta Ton CO2 | (*Sumber: EDGAR / Kementerian LHK*) |
| Pertumbuhan Ekonomi (PDB) | Pertumbuhan PDB Riil | Persen (%) | (*Sumber: BPS / World Bank*) |
| Energi Baru Terbarukan (EBT) | Bauran EBT dalam energi nasional | Persen (%) | (*Sumber: Kementerian ESDM / IRENA*) |

Berikut adalah data penelitian:

| **Tahun** | **Emisi CO2 (Juta Ton)** | **PDB Riil (%)** | **Bauran EBT (%)** |
|---|---|---|---|
| 2010 | 543,9 | 6,01 | 5,40 |
| 2011 | 596,3 | 6,17 | 3,77 |
| 2012 | 623,0 | 6,03 | 3,92 |
| 2013 | 591,3 | 5,56 | 4,96 |
| 2014 | 598,8 | 5,01 | 5,32 |
| 2015 | 612,0 | 4,88 | 4,39 |
| 2016 | 616,6 | 5,03 | 6,48 |
| 2017 | 645,2 | 5,07 | 6,70 |
| 2018 | 703,4 | 5,17 | 8,60 |
| 2019 | 756,1 | 5,03 | 9,70 |
| 2020 | 694,3 | -2,07 | 10,90 |
| 2021 | 713,1 | 3,70 | 11,80 |
| 2022 | 839,6 | 5,31 | 12,28 |
| 2023 | 861,6 | 5,05 | 13,29 |
| 2024 | 920,9 | 5,03 | 14,68 |

Dari tabel di atas terlihat bahwa emisi CO2 menunjukkan tren naik yang persisten (dari 543,9 menjadi 920,9 juta ton), sementara penetrasi EBT juga meningkat signifikan (dari 5,4% menjadi 14,68%). Pertumbuhan PDB relatif stabil di kisaran 5%, kecuali pada tahun 2020 yang mengalami kontraksi -2,07% akibat pandemi.

### 3.3 Tahapan Analisis

Analisis data dilakukan melalui empat tahapan sistematis:

1. **Uji Stasioneritas** -- Augmented Dickey-Fuller (ADF) Test untuk memastikan tidak ada variabel I(2).
2. **Estimasi Model ARDL dan Uji Kointegrasi** -- ARDL Bounds Testing untuk mendeteksi hubungan ekuilibrium jangka panjang.
3. **Estimasi Koefisien Jangka Panjang dan Jangka Pendek** -- Ekstraksi elastisitas dan Error Correction Term (ECT).
4. **Uji Diagnostik** -- Breusch-Godfrey (autokorelasi), Breusch-Pagan-Godfrey (heteroskedastisitas), Jarque-Bera (normalitas), serta CUSUM dan CUSUM of Squares (stabilitas).

---

## 4. HASIL DAN DISKUSI

### 4.1 Uji Stasioneritas (Augmented Dickey-Fuller)

Syarat fundamental dalam pengujian ARDL adalah memastikan tidak ada variabel yang terintegrasi pada derajat I(2). Hasil uji ADF disajikan pada tabel berikut:

| **Variabel** | **t-Stat (Level)** | **Prob. (Level)** | **t-Stat (1st Diff)** | **Prob. (1st Diff)** | **Derajat** |
|---|---|---|---|---|---|
| Emisi Karbon (LN_CO2) | 1,9234 | 0,9992 | -3,5075 | 0,0258 | I(1) |
| PDB Riil | -2,9162 | 0,0685 | -3,3649 | 0,0398 | I(1) |
| Penetrasi EBT | 0,9998 | 0,9936 | -4,6174 | 0,0039 | I(1) |

Seluruh variabel tidak stasioner pada tingkat Level (p-value > 0,05), namun berhasil mencapai stasioneritas pada diferensiasi pertama atau I(1) dengan tingkat signifikansi yang kuat (p-value < 0,05). Kondisi ini mengesahkan kelayakan penggunaan spesifikasi ARDL Bounds Testing.

(*Rujukan metodologi ADF -- Dickey & Fuller, 1979; 1981*)

### 4.2 Uji Kointegrasi (ARDL Bounds Testing)

Pengujian kointegrasi dilakukan untuk mengonfirmasi keberadaan ekuilibrium jangka panjang antarvariabel. Berdasarkan estimasi model ARDL, nilai **F-Statistic tercatat sebesar 5,075**.

Nilai ini secara absolut melampaui ambang batas atas (*Upper Bound*) I(1) pada taraf signifikansi 5% yang bernilai 4,428. Penolakan hipotesis nol (H0: tidak ada kointegrasi) memberikan justifikasi ekonometrika bahwa lintasan pertumbuhan ekonomi, penetrasi EBT, dan eskalasi emisi karbon di Indonesia **tidak bergerak secara acak, melainkan terikat dalam hubungan jangka panjang yang permanen**.

(*Pesaran, Shin & Smith, 2001 -- Bounds Testing critical values*)

Implikasi dari temuan ini sangat substansial: kebijakan pertumbuhan ekonomi dan kebijakan energi terbarukan secara empiris terbukti memiliki dampak struktural terhadap trajektori emisi karbon Indonesia, bukan sekadar fluktuasi sementara.

### 4.3 Estimasi Koefisien Jangka Panjang dan Jangka Pendek

Model menghasilkan nilai koefisien penyesuaian (Error Correction Term / **CointEq**) sebesar **-1,740** dengan probabilitas **0,0006**. Nilai negatif dan sangat signifikan ini mengonfirmasi bahwa:
- Model bersifat stabil dan konvergen.
- Guncangan ketidakseimbangan sistem akan dikoreksi secara agresif menuju garis ekuilibrium pada periode berikutnya.
- Kecepatan penyesuaian yang sangat tinggi (lebih dari 100%) mengindikasikan adanya *over-correction*, yang lazim terjadi pada sistem ekonomi-lingkungan dengan dinamika yang kompleks.

#### A. Pertumbuhan Ekonomi dan Emisi: Kegagalan EKC

Pada dimensi ekuilibrium **jangka panjang**, koefisien PDB menunjukkan nilai **positif sebesar 0,0428** dengan **p-value 0,0283** (signifikan pada taraf 5%).

(*Teori Environmental Kuznets Curve -- Grossman & Krueger, 1995; Stern, 2004*)

Temuan ini membuktikan bahwa hipotesis EKC **tidak berlaku** di Indonesia selama periode observasi. Setiap persentase kenaikan pertumbuhan PDB secara konsisten menyumbang tambahan emisi karbon. Kurva EKC Indonesia masih berada pada **fase mendaki** (*ascending phase*) dan gagal mencapai titik balik pelandaian (*turning point*).

Fenomena ini dapat dijelaskan melalui konsep **Structural Lock-in Effect**. Arsitektur ekonomi Indonesia yang berbasis pada ekspor komoditas ekstraktif padat karbon -- terutama batu bara, minyak kelapa sawit, dan nikel -- menciptakan ketergantungan struktural di mana pertumbuhan ekonomi secara inheren terkunci pada aktivitas yang menghasilkan emisi tinggi.

(*Teori Carbon Lock-in -- Unruh, 2000; 2002*)
(*Data struktur ekspor Indonesia -- BPS / Kementerian Perdagangan*)

Selama kontribusi sektor ekstraktif terhadap PDB tetap dominan, pertumbuhan ekonomi akan selalu disertai eskalasi emisi. Proses *decoupling* -- pemisahan pertumbuhan ekonomi dari peningkatan emisi -- belum terjadi di Indonesia.

(*Konsep Decoupling -- UNEP, 2011; OECD Green Growth indicators*)

#### B. Energi Terbarukan dan Emisi: Paradoks Jevons

Anomali terbesar dan temuan paling kritis dari penelitian ini terdeteksi pada dinamika variabel EBT. **Baik dalam jangka pendek maupun jangka panjang, transisi energi hijau secara konsisten berkorelasi positif terhadap kenaikan emisi.**

| **Dimensi** | **Koefisien** | **p-value** | **Signifikansi** |
|---|---|---|---|
| Jangka Pendek -- D(EBT) | +0,0292 | 0,0021 | Signifikan pada 1% |
| Jangka Panjang -- EBT(-1) | +0,0763 | 0,0170 | Signifikan pada 5% |

(*Teori Jevons Paradox -- William Stanley Jevons, 1865, "The Coal Question"*)
(*Konsep Rebound Effect dan Backfire Effect -- Sorrell, 2009; Gillingham et al., 2016*)

Bukti empiris ini merupakan manifestasi dari **Paradoks Jevons** dalam skala ekstrem, yang dalam literatur ekonomi energi dikenal sebagai **Backfire Effect**. Mekanisme yang mendasari paradoks ini dapat diuraikan sebagai berikut:

1. **Efek Substitusi Harga**: Injeksi kapasitas EBT menurunkan *Levelized Cost of Electricity* (LCOE) secara agregat. Penurunan harga energi ini justru merangsang korporasi dan industri untuk mengekspansi skala produksi, sehingga total konsumsi energi meningkat.

(*Konsep LCOE dan dampaknya -- IRENA, Lazard LCOE Analysis*)

2. **Masalah Intermitensi dan Peaker PLTU**: Energi terbarukan seperti surya dan angin bersifat intermiten (fluktuatif). Untuk menjaga stabilitas jaringan listrik, utilitas merespons intermitensi ini dengan menyalakan pembangkit listrik tenaga uap (PLTU) batu bara sebagai *peaker plant* secara lebih agresif. Akibatnya, penambahan kapasitas EBT justru diikuti oleh peningkatan operasi PLTU.

(*Sumber rujukan masalah intermitensi EBT di Indonesia -- PLN RUPTL / studi sistem kelistrikan Jawa-Bali*)

3. **Tidak Ada Fase-Out Fosil**: Indonesia terus menambah kapasitas PLTU batu bara baru secara paralel dengan penambahan kapasitas EBT. Transisi energi yang terjadi bersifat aditif (*additive*), bukan substitutif. EBT ditambahkan ke dalam bauran energi tanpa mengurangi kapasitas terpasang energi fosil.

(*Sumber rujukan -- data kapasitas terpasang PLTU baru di Indonesia, IESR / IISD*)

Temuan ini memiliki implikasi kebijakan yang sangat serius: **penambahan kapasitas EBT tanpa disertai kebijakan penghentian (*phase-out*) energi fosil secara simultan tidak akan pernah efektif dalam mereduksi emisi karbon.**

### 4.4 Uji Diagnostik dan Stabilitas Model

Guna menjustifikasi ketangguhan (*robustness*) temuan empiris, serangkaian uji asumsi klasik diterapkan pada residu model:

| **Uji Diagnostik** | **Metode** | **Prob. Chi-Square** | **Keputusan** |
|---|---|---|---|
| Autokorelasi | Breusch-Godfrey LM Test | 0,0820 (> 0,05) | Tidak ada autokorelasi |
| Heteroskedastisitas | Breusch-Pagan-Godfrey | 0,4464 (> 0,05) | Homoskedastis |
| Normalitas | Jarque-Bera | 0,7759 (> 0,05) | Distribusi normal |

(*Rujukan uji diagnostik -- Breusch & Godfrey, 1978; Breusch & Pagan, 1979; Jarque & Bera, 1980*)

Model ARDL ini lolos secara sempurna dari seluruh ancaman bias ekonometrika. Lebih jauh, pengujian stabilitas struktural **CUSUM** dan **CUSUM of Squares** mendemonstrasikan bahwa garis fluktuasi residu secara konsisten bergerak di dalam koridor interval kepercayaan 5%. Hal ini membuktikan bahwa parameter model yang mengonfirmasi Paradoks Jevons ini **sangat stabil dan resisten terhadap guncangan syok ekonomi eksternal**.

(*Rujukan CUSUM Test -- Brown, Durbin & Evans, 1975*)

---

## 5. KESIMPULAN DAN SARAN

### 5.1 Kesimpulan

Berdasarkan hasil estimasi model ARDL dengan data runtun waktu Indonesia periode 2010-2024, penelitian ini menghasilkan dua temuan utama:

**Pertama**, pertumbuhan ekonomi (PDB) memiliki hubungan positif dan signifikan terhadap emisi CO2 dalam jangka panjang (koefisien = 0,0428; p-value = 0,0283). Temuan ini mengonfirmasi bahwa **hipotesis Environmental Kuznets Curve (EKC) tidak berlaku di Indonesia**. Kurva hubungan pendapatan-emisi masih berada pada fase mendaki, yang mengindikasikan kegagalan *decoupling* antara pertumbuhan ekonomi dan degradasi lingkungan. Struktur ekonomi Indonesia yang bertumpu pada sektor ekstraktif padat karbon menciptakan efek penguncian struktural (*carbon lock-in*) yang menghalangi transisi menuju trajektori pembangunan rendah karbon.

(*Teori EKC -- Grossman & Krueger, 1995*)
(*Teori Carbon Lock-in -- Unruh, 2000*)

**Kedua**, penetrasi energi baru dan terbarukan (EBT) secara paradoksal menunjukkan korelasi positif dan signifikan terhadap emisi CO2, baik dalam jangka pendek (koefisien = 0,0292; p-value = 0,0021) maupun jangka panjang (koefisien = 0,0763; p-value = 0,0170). Temuan ini merupakan **bukti empiris kuat terjadinya Paradoks Jevons** dalam bentuk *Backfire Effect* -- di mana peningkatan efisiensi dan kapasitas energi terbarukan justru meningkatkan total konsumsi energi dan emisi karbon, alih-alih menurunkannya.

(*Teori Jevons Paradox -- Jevons, 1865*)
(*Konsep Backfire Effect -- Sorrell, 2009*)

Kedua temuan ini secara bersamaan menggambarkan **kegagalan struktural ganda** dalam arsitektur kebijakan iklim Indonesia: pertumbuhan ekonomi masih bersifat *carbon-intensive*, sementara transisi energi yang dilakukan bersifat *additive* -- menambah kapasitas terbarukan tanpa mengurangi kapasitas fosil.

### 5.2 Saran

Berdasarkan temuan empiris di atas, penelitian ini merekomendasikan beberapa implikasi kebijakan:

1. **Kebijakan Phase-Out Energi Fosil yang Terjadwal**: Penambahan kapasitas EBT harus disertai jadwal penghentian operasi PLTU batu bara secara bertahap. Tanpa fase-out simultan, transisi energi hanya bersifat aditif dan tidak efektif mereduksi emisi.

(*Rujukan kebijakan -- pengalaman Uni Eropa dalam Coal Phase-out, Just Energy Transition Partnership / JETP Indonesia*)

2. **Reformasi Struktur Ekonomi**: Indonesia perlu mengakselerasi diversifikasi ekonomi dari sektor ekstraktif padat karbon menuju sektor manufaktur bernilai tambah tinggi dan ekonomi hijau. Hal ini penting untuk memutus efek penguncian struktural (*carbon lock-in*).

(*Rujukan -- strategi industrialisasi hijau, green industrial policy*)

3. **Mekanisme Carbon Pricing**: Implementasi instrumen penetapan harga karbon -- baik melalui pajak karbon maupun sistem perdagangan emisi (*emissions trading system* / ETS) -- perlu dipercepat untuk menginternalisasi eksternalitas negatif dari emisi dan mencegah efek rebound.

(*Rujukan -- UU No. 7/2021 tentang HPP, skema pajak karbon Indonesia, pengalaman EU-ETS*)

4. **Penguatan Regulasi Intermitensi**: Diperlukan investasi masif dalam teknologi penyimpanan energi (*energy storage*) dan *smart grid* untuk mengurangi ketergantungan pada PLTU peaker sebagai solusi intermitensi EBT.

(*Rujukan -- teknologi battery energy storage system / BESS, roadmap PLN*)

5. **Penelitian Lanjutan**: Studi mendatang disarankan untuk memperluas cakupan variabel (misalnya, urbanisasi, Foreign Direct Investment, tata kelola pemerintahan) dan memperpanjang periode observasi guna memperoleh estimasi yang lebih robust. Penggunaan metode nonlinear seperti NARDL juga dapat memberikan wawasan tambahan mengenai asimetri hubungan antarvariabel.

(*Rujukan metodologi -- Shin, Yu & Greenwood-Nimmo, 2014, Nonlinear ARDL*)

---

> **Catatan**: Draft ini belum menyertakan tinjauan pustaka (Literature Review). Setiap penanda (*...*) menunjukkan teori atau sumber rujukan yang perlu dimasukkan pada revisi berikutnya.
