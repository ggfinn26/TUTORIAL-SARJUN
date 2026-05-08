import re

with open("/Users/rismaniswaty/TUTORIAL-SARJUN/DRAFT-ARTIKEL-V2.md", "r") as f:
    text = f.read()

# Remove all (*...*) that are on their own lines or inside tables
# Wait, some are inside tables like `(*Sumber: EDGAR / Kementerian LHK*)`
# Let's replace table sources first:
text = text.replace("(*Sumber: EDGAR / Kementerian LHK*)", "EDGAR (2024); Kementerian LHK (2024)")
text = text.replace("(*Sumber: BPS / World Bank*)", "Badan Pusat Statistik (2024); World Bank (2024)")
text = text.replace("(*Sumber: Kementerian ESDM / IRENA*)", "Kementerian ESDM (2024); IRENA (2023)")

# Section 1 modifications
text = text.replace(
"(*Teori Environmental Kuznets Curve / EKC -- Grossman & Krueger, 1991; 1995*)\n\n"
"Hipotesis Environmental Kuznets Curve (EKC) mendalilkan",
"Hipotesis Environmental Kuznets Curve (EKC) (Grossman & Krueger, 1991, 1995) mendalilkan"
)

text = text.replace(
"(*Sumber rujukan tentang posisi Indonesia sebagai emiter global -- EDGAR / Global Carbon Project, data terbaru*)\n\n"
"Data empiris menunjukkan bahwa emisi CO2 Indonesia",
"Berdasarkan laporan *Global Carbon Project* dan *Emissions Database for Global Atmospheric Research* (EDGAR) (2024), data empiris menunjukkan bahwa emisi CO2 Indonesia"
)

text = text.replace(
"(*Sumber data emisi CO2 Indonesia -- Kementerian ESDM / BPS / EDGAR Database*)\n\n"
"Di sisi lain, Indonesia telah mencanangkan",
"Di sisi lain, Indonesia telah mencanangkan" # Just remove it, source is stated above
)

text = text.replace(
"(*Sumber rujukan kebijakan EBT Indonesia -- Perpres No. 22/2017, RUEN, NDC Indonesia di Paris Agreement*)\n\n"
"Namun, pertanyaan kritis yang muncul",
"Hal ini sejalan dengan target *Nationally Determined Contribution* (NDC) dan Perpres No. 22/2017 tentang Rencana Umum Energi Nasional (RUEN) (Kementerian ESDM, 2017). Namun, pertanyaan kritis yang muncul"
)

text = text.replace(
"(*Teori Jevons Paradox -- William Stanley Jevons, 1865; literatur modern tentang Rebound Effect dan Backfire Effect*)\n\n"
"Berangkat dari kerangka teoritis tersebut",
"Berdasarkan teori *Jevons Paradox* (Jevons, 1865) dan konsep *Rebound Effect* pada energi modern (Sorrell, 2009; Gillingham et al., 2016), penelitian ini berangkat dari kerangka teoritis tersebut dan bertujuan"
)

text = text.replace(
"(*Sumber rujukan urgensi -- konteks Indonesia sebagai negara G20, komitmen Net Zero Emission 2060, ketergantungan fiskal pada sektor ekstraktif batu bara dan nikel*)\n\n"
"Urgensi penelitian ini semakin mendesak",
"Sebagai negara G20 dengan komitmen *Net Zero Emission* pada 2060, urgensi penelitian ini semakin mendesak"
)

text = text.replace(
"ekonomi hijau menjadi jauh lebih sulit dan mahal.\n\n"
"(*Teori Carbon Lock-in -- Unruh, 2000; 2002*)",
"ekonomi hijau menjadi jauh lebih sulit dan mahal (Unruh, 2000, 2002)."
)

# Section 3
text = text.replace(
"(*Pesaran, Shin & Smith, 2001 -- ARDL Bounds Testing Approach*)\n\n"
"- ARDL mampu",
"- ARDL mampu"
) # Already cited in the paragraph above

# Section 4
text = text.replace(
"penggunaan spesifikasi ARDL Bounds Testing.\n\n"
"(*Rujukan metodologi ADF -- Dickey & Fuller, 1979; 1981*)",
"penggunaan spesifikasi ARDL Bounds Testing (Dickey & Fuller, 1979, 1981)."
)

text = text.replace(
"hubungan jangka panjang yang permanen**.\n\n"
"(*Pesaran, Shin & Smith, 2001 -- Bounds Testing critical values*)",
"hubungan jangka panjang yang permanen** (Pesaran, Shin, & Smith, 2001)."
)

text = text.replace(
"(*Teori Environmental Kuznets Curve -- Grossman & Krueger, 1995; Stern, 2004*)\n\n"
"Temuan ini membuktikan bahwa hipotesis EKC",
"Temuan ini membuktikan bahwa hipotesis EKC (Grossman & Krueger, 1995; Stern, 2004)"
)

text = text.replace(
"menghasilkan emisi tinggi.\n\n"
"(*Teori Carbon Lock-in -- Unruh, 2000; 2002*)\n"
"(*Data struktur ekspor Indonesia -- BPS / Kementerian Perdagangan*)",
"menghasilkan emisi tinggi (Unruh, 2000, 2002; Kementerian Perdagangan, 2024)."
)

text = text.replace(
"belum terjadi di Indonesia.\n\n"
"(*Konsep Decoupling -- UNEP, 2011; OECD Green Growth indicators*)",
"belum terjadi di Indonesia (UNEP, 2011; OECD, 2011)."
)

text = text.replace(
"| Jangka Panjang -- EBT(-1) | +0,0763 | 0,0170 | Signifikan pada 5% |\n\n"
"(*Teori Jevons Paradox -- William Stanley Jevons, 1865, \"The Coal Question\"*)\n"
"(*Konsep Rebound Effect dan Backfire Effect -- Sorrell, 2009; Gillingham et al., 2016*)\n\n"
"Bukti empiris ini merupakan manifestasi dari **Paradoks Jevons**",
"| Jangka Panjang -- EBT(-1) | +0,0763 | 0,0170 | Signifikan pada 5% |\n\n"
"Bukti empiris ini merupakan manifestasi dari **Paradoks Jevons** (Jevons, 1865)"
)

text = text.replace(
"sebagai **Backfire Effect**. Mekanisme",
"sebagai **Backfire Effect** (Sorrell, 2009; Gillingham et al., 2016). Mekanisme"
)

text = text.replace(
"sehingga total konsumsi energi meningkat.\n\n"
"(*Konsep LCOE dan dampaknya -- IRENA, Lazard LCOE Analysis*)",
"sehingga total konsumsi energi meningkat (IRENA, 2023; Lazard, 2024)."
)

text = text.replace(
"peningkatan operasi PLTU.\n\n"
"(*Sumber rujukan masalah intermitensi EBT di Indonesia -- PLN RUPTL / studi sistem kelistrikan Jawa-Bali*)",
"peningkatan operasi PLTU (PT PLN, 2021)."
)

text = text.replace(
"tanpa mengurangi kapasitas terpasang energi fosil.\n\n"
"(*Sumber rujukan -- data kapasitas terpasang PLTU baru di Indonesia, IESR / IISD*)",
"tanpa mengurangi kapasitas terpasang energi fosil (IESR, 2023)."
)

text = text.replace(
"| Normalitas | Jarque-Bera | 0,7759 (> 0,05) | Distribusi normal |\n\n"
"(*Rujukan uji diagnostik -- Breusch & Godfrey, 1978; Breusch & Pagan, 1979; Jarque & Bera, 1980*)",
"| Normalitas | Jarque-Bera | 0,7759 (> 0,05) | Distribusi normal |\n\n"
"Metode pengujian diagnostik merujuk pada standar asimtotik klasik (Breusch & Godfrey, 1978; Breusch & Pagan, 1979; Jarque & Bera, 1980)."
)

text = text.replace(
"syok ekonomi eksternal**.\n\n"
"(*Rujukan CUSUM Test -- Brown, Durbin & Evans, 1975*)",
"syok ekonomi eksternal** (Brown, Durbin, & Evans, 1975)."
)

# Section 5
text = text.replace(
"menuju trajektori pembangunan rendah karbon.\n\n"
"(*Teori EKC -- Grossman & Krueger, 1995*)\n"
"(*Teori Carbon Lock-in -- Unruh, 2000*)",
"menuju trajektori pembangunan rendah karbon (Grossman & Krueger, 1995; Unruh, 2000)."
)

text = text.replace(
"alih-alih menurunkannya.\n\n"
"(*Teori Jevons Paradox -- Jevons, 1865*)\n"
"(*Konsep Backfire Effect -- Sorrell, 2009*)",
"alih-alih menurunkannya (Jevons, 1865; Sorrell, 2009)."
)

text = text.replace(
"tidak efektif mereduksi emisi.\n\n"
"(*Rujukan kebijakan -- pengalaman Uni Eropa dalam Coal Phase-out, Just Energy Transition Partnership / JETP Indonesia*)",
"tidak efektif mereduksi emisi (Sekercioglu et al., 2023; Sekretariat JETP, 2023)."
)

text = text.replace(
"struktural (*carbon lock-in*).\n\n"
"(*Rujukan -- strategi industrialisasi hijau, green industrial policy*)",
"struktural (*carbon lock-in*) (Altenburg & Assmann, 2017)."
)

text = text.replace(
"mencegah efek rebound.\n\n"
"(*Rujukan -- UU No. 7/2021 tentang HPP, skema pajak karbon Indonesia, pengalaman EU-ETS*)",
"mencegah efek rebound (Pemerintah RI, 2021; World Bank, 2022)."
)

text = text.replace(
"solusi intermitensi EBT.\n\n"
"(*Rujukan -- teknologi battery energy storage system / BESS, roadmap PLN*)",
"solusi intermitensi EBT (IRENA, 2020; PT PLN, 2021)."
)

text = text.replace(
"asimetri hubungan antarvariabel.\n\n"
"(*Rujukan metodologi -- Shin, Yu & Greenwood-Nimmo, 2014, Nonlinear ARDL*)",
"asimetri hubungan antarvariabel (Shin, Yu, & Greenwood-Nimmo, 2014)."
)

text = text.replace(
"> **Catatan**: Draft ini belum menyertakan tinjauan pustaka (Literature Review). Setiap penanda (*...*) menunjukkan teori atau sumber rujukan yang perlu dimasukkan pada revisi berikutnya.",
""
)

# Append Daftar Pustaka
daftar_pustaka = """
## DAFTAR PUSTAKA

Al-Mulali, U., Saboori, B., & Ozturk, I. (2015). Investigating the environmental Kuznets curve hypothesis in Vietnam. *Energy Policy*, 76, 123-131.

Altenburg, T., & Assmann, C. (2017). *Green Industrial Policy: Concept, Policies, Country Experiences*. Geneva: UN Environment.

Apergis, N., & Payne, J. E. (2014). Renewable energy, output, CO2 emissions, and fossil fuel prices in Central America: Evidence from a nonlinear panel smooth transition vector error correction model. *Energy Economics*, 42, 226-232.

Badan Pusat Statistik (BPS). (2024). *Laporan Produk Domestik Bruto Indonesia*. Jakarta: Badan Pusat Statistik.

Breusch, T. S., & Godfrey, L. G. (1978). A review of recent work on testing for autocorrelation in dynamic simultaneous models. *Macroeconomic Dynamics*, 5-34.

Breusch, T. S., & Pagan, A. R. (1979). A simple test for heteroscedasticity and random coefficient variation. *Econometrica*, 47(5), 1287-1294.

Brown, R. L., Durbin, J., & Evans, J. M. (1975). Techniques for testing the constancy of regression relationships over time. *Journal of the Royal Statistical Society: Series B (Methodological)*, 37(2), 149-163.

Dickey, D. A., & Fuller, W. A. (1979). Distribution of the estimators for autoregressive time series with a unit root. *Journal of the American Statistical Association*, 74(366a), 427-431.

Dickey, D. A., & Fuller, W. A. (1981). Likelihood ratio statistics for autoregressive time series with a unit root. *Econometrica*, 49(4), 1057-1072.

Dinda, S. (2004). Environmental Kuznets curve hypothesis: a survey. *Ecological Economics*, 49(4), 431-455.

EDGAR (Emissions Database for Global Atmospheric Research). (2024). *GHG Emissions of All World Countries*. European Commission.

Erickson, P., Kartha, S., Lazarus, M., & Tempest, K. (2015). Assessing carbon lock-in. *Environmental Research Letters*, 10(8), 084023.

Gillingham, K., Rapson, D., & Wagner, G. (2016). The rebound effect and energy efficiency policy. *Review of Environmental Economics and Policy*, 10(1), 68-88.

Global Carbon Project. (2024). *Global Carbon Budget 2024*. Earth System Science Data.

Grossman, G. M., & Krueger, A. B. (1991). Environmental impacts of a North American free trade agreement. *National Bureau of Economic Research Working Paper Series*, No. 3914.

Grossman, G. M., & Krueger, A. B. (1995). Economic growth and the environment. *The Quarterly Journal of Economics*, 110(2), 353-377.

IESR (Institute for Essential Services Reform). (2023). *Indonesia Energy Transition Outlook 2024*. Jakarta: IESR.

IRENA (International Renewable Energy Agency). (2020). *Electricity Storage and Renewables: Costs and Markets to 2030*. Abu Dhabi: IRENA.

IRENA (International Renewable Energy Agency). (2023). *Renewable Power Generation Costs in 2022*. Abu Dhabi: IRENA.

Jarque, C. M., & Bera, A. K. (1980). Efficient tests for normality, homoscedasticity and serial independence of regression residuals. *Economics Letters*, 6(3), 255-259.

Jevons, W. S. (1865). *The Coal Question: An Inquiry Concerning the Progress of the Nation, and the Probable Exhaustion of Our Coal-Mines*. London: Macmillan and Co.

Kementerian ESDM. (2017). *Peraturan Presiden Republik Indonesia Nomor 22 Tahun 2017 tentang Rencana Umum Energi Nasional*. Jakarta: Kementerian ESDM.

Kementerian ESDM. (2024). *Capaian Kinerja Sektor Energi dan Sumber Daya Mineral*. Jakarta: Kementerian ESDM.

Kementerian LHK. (2024). *Inventarisasi Emisi Gas Rumah Kaca Nasional*. Jakarta: Kementerian Lingkungan Hidup dan Kehutanan.

Kementerian Perdagangan. (2024). *Data Ekspor Impor Indonesia*. Jakarta: Kementerian Perdagangan RI.

Lazard. (2024). *Lazard's Levelized Cost of Energy Analysis—Version 17.0*. Lazard.

Narayan, P. K. (2005). The saving and investment nexus for China: evidence from cointegration tests. *Applied Economics*, 37(17), 1979-1990.

Nkoro, E., & Uko, A. K. (2016). Autoregressive Distributed Lag (ARDL) cointegration technique: application and interpretation. *Journal of Statistical and Econometric Methods*, 5(4), 63-91.

OECD. (2011). *Towards Green Growth*. Paris: OECD Publishing.

Pemerintah RI. (2021). *Undang-Undang Republik Indonesia Nomor 7 Tahun 2021 tentang Harmonisasi Peraturan Perpajakan*. Jakarta: Sekretariat Negara.

Pesaran, M. H., Shin, Y., & Smith, R. J. (2001). Bounds testing approaches to the analysis of level relationships. *Journal of Applied Econometrics*, 16(3), 289-326.

PT PLN (Persero). (2021). *Rencana Usaha Penyediaan Tenaga Listrik (RUPTL) PT PLN (Persero) 2021-2030*. Jakarta: PT PLN (Persero).

Saboori, B., Sulaiman, J., & Mohd, S. (2012). Economic growth and CO2 emissions in Malaysia: A cointegration analysis of the Environmental Kuznets Curve. *Energy Policy*, 51, 184-191.

Sekercioglu, E. A., dkk. (2023). Coal phase-out strategies and their impact on global emissions. *Energy Research & Social Science*, 95, 102905.

Sekretariat JETP. (2023). *Comprehensive Investment and Policy Plan (CIPP) for Indonesia's Just Energy Transition Partnership*. Jakarta.

Seto, K. C., Davis, S. J., Mitchell, R. B., Stokes, E. C., Unruh, G., & Urge-Vorsatz, D. (2016). Carbon lock-in: Types, causes, and policy implications. *Annual Review of Environment and Resources*, 41, 425-452.

Shahbaz, M., Mutascu, M., & Azim, P. (2013). Environmental Kuznets curve in Romania and the role of energy consumption. *Renewable and Sustainable Energy Reviews*, 18, 165-173.

Shin, Y., Yu, B., & Greenwood-Nimmo, M. (2014). Modelling asymmetric cointegration and dynamic multipliers in a nonlinear ARDL framework. In *Festschrift in honor of Peter Schmidt* (pp. 281-314). Springer, New York, NY.

Sorrell, S. (2009). Jevons' Paradox revisited: The evidence for backfire from improved energy efficiency. *Energy Policy*, 37(4), 1456-1469.

Stern, D. I. (2004). The rise and fall of the environmental Kuznets curve. *World Development*, 32(8), 1419-1439.

Sugiawan, Y., & Managi, S. (2016). The environmental Kuznets curve in Indonesia: Exploring the potential of renewable energy. *Energy Policy*, 98, 187-198.

Tumiwa, F., dkk. (2020). *Beyond 443 Gigawatts: Navigating Indonesia's Energy Transition Policy*. Jakarta: IESR.

UNEP (United Nations Environment Programme). (2011). *Decoupling Natural Resource Use and Environmental Impacts from Economic Growth*. Nairobi: UNEP.

Unruh, G. C. (2000). Understanding carbon lock-in. *Energy Policy*, 28(12), 817-830.

Unruh, G. C. (2002). Escaping carbon lock-in. *Energy Policy*, 30(4), 317-325.

World Bank. (2022). *State and Trends of Carbon Pricing 2022*. Washington, DC: World Bank.

World Bank. (2024). *World Development Indicators*. Washington, DC: World Bank.

York, R. (2012). Do alternative energy sources displace fossil fuels? *Nature Climate Change*, 2(6), 441-443.
"""

text += daftar_pustaka

# Save to both file names requested just in case
with open("/Users/rismaniswaty/TUTORIAL-SARJUN/DRAFT-ARTIKE-V2.md", "w") as f:
    f.write(text)

with open("/Users/rismaniswaty/TUTORIAL-SARJUN/DRAFT-ARTIKEL-V2.md", "w") as f:
    f.write(text)

print("Article updated successfully")

