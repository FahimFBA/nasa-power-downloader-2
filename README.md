# 🌍 NASA POWER Hourly Data Downloader Ver.2

This project automates the downloading and merging of hourly climate data from [NASA POWER API](https://power.larc.nasa.gov/).  

## 🚀 Features  
👉 Downloads hourly weather data (2014–2024)  
👉 Splits requests into smaller chunks (1 year per request)  
👉 Cleans and removes unnecessary headers from downloaded CSV files  
👉 Automatically merges data into a single CSV file  
👉 Saves cleaned and merged data in organized directories  
👉 Handles API errors with a retry mechanism  

---

## 📂 Project Structure  
```
📺 nasa-power-downloader  
👤📂 data/                 # Stores all data files  
👤   📂 cleaned/          # Stores cleaned CSV files (without headers)  
👤   📂 merged/           # Stores the final merged CSV file  
👤📂 scripts/              # Python scripts for downloading & merging  
👤📝 README.md             # Project documentation  
👤📝 LICENSE               # Open-source license  
👤📝 config.py             # API settings  
```

---

## 📊 Available Parameters  

The following meteorological parameters are included in the downloaded dataset:  

| Parameter                | Description                                                   | Unit    |
| ------------------------ | ------------------------------------------------------------- | ------- |
| **ALLSKY_SFC_SW_DWN**    | All Sky Surface Shortwave Downward Irradiance (CERES SYN1deg) | Wh/m²   |
| **T2M**                  | Temperature at 2 Meters (MERRA-2)                             | °C      |
| **QV2M**                 | Specific Humidity at 2 Meters (MERRA-2)                       | g/kg    |
| **RH2M**                 | Relative Humidity at 2 Meters (MERRA-2)                       | %       |
| **PRECTOTCORR**          | Precipitation Corrected (MERRA-2)                             | mm/hr   |
| **WD10M**                | Wind Direction at 10 Meters (MERRA-2)                         | Degrees |
| **WS10M**                | Wind Speed at 10 Meters (MERRA-2)                             | m/s     |
| **PS**                   | Surface Pressure (MERRA-2)                                    | kPa     |
| **DEW**                  | Dew Point Temperature (calculated)                            | °C      |
| **WET BULB TEMPERATURE** | Wet Bulb Temperature (calculated)                             | °C      |

---

## 🛠 Setup Instructions  
### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/FahimFBA/nasa-power-downloader.git  
cd nasa-power-downloader  
```  

### 2️⃣ Install Dependencies  
```bash
pip install -r scripts/requirements.txt  
```  

### 3️⃣ Configure Settings (Optional)  
Edit [**config.py**](./config.py) to change location and parameters.  

### 4️⃣ Run the Data Downloader  
```bash
python scripts/download_nasa_power.py  
```  

### 5️⃣ Clean & Merge Downloaded Files  
```bash
python scripts/merge_csv.py  
```  

The cleaned files will be saved in:  
📂 **data/cleaned/**  

The final merged dataset will be saved as:  
📝 **data/merged/merged_data.csv**  

---

## 🐜 License  
This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.  

---

## 👨‍💻 Author  
Md. Fahim Bin Amin – [fahimbinamin@gmail.com](mailto:fahimbinamin@gmail.com)  
GitHub: [@FahimFBA](https://github.com/FahimFBA)
