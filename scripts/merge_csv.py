import sys
import os

# Add root dir to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import config
import sys
import os
import numpy as np
import pandas as pd
import shutil


def print_progress(message, emoji="✅"):
    print(f"{emoji} {message}")


def create_cleaned_dir(data_dir, cleaned_dir):
    if not os.path.exists(cleaned_dir):
        os.makedirs(cleaned_dir)
        print_progress(f"Created cleaned directory: {cleaned_dir}")
    else:
        print(f"⚠️ {cleaned_dir} already exists!")


def clean_and_copy_csv_files(data_dir, cleaned_dir):
    for file_name in os.listdir(data_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(data_dir, file_name)
            cleaned_file_path = os.path.join(cleaned_dir, file_name)
            shutil.copy(file_path, cleaned_file_path)

            print_progress(f"Cleaning file: {file_name}")
            with open(cleaned_file_path, 'r') as file:
                lines = file.readlines()

            in_header = False
            cleaned_lines = []
            for line in lines:
                if "-BEGIN HEADER-" in line:
                    in_header = True
                if in_header:
                    if "-END HEADER-" in line:
                        in_header = False
                    continue
                cleaned_lines.append(line)

            with open(cleaned_file_path, 'w') as file:
                file.writelines(cleaned_lines)

            print_progress(f"Finished cleaning: {file_name}", "✔️")


def calculate_dew_point(temp, humidity):
    a = 17.27
    b = 237.7
    gamma = (a * temp) / (b + temp) + np.log(humidity / 100.0)
    return (b * gamma) / (a - gamma)


def calculate_wet_bulb(temp, humidity):
    return temp * np.arctan(0.151977 * np.sqrt(humidity + 8.313659)) + np.arctan(temp + humidity) - np.arctan(humidity - 1.676331) + 0.00391838 * np.power(humidity, 1.5) * np.arctan(0.023101 * humidity) - 4.686035


def merge_csv_files(cleaned_dir, merged_dir, output_file):
    df_list = []
    print_progress("Merging CSV files...")
    for file_name in os.listdir(cleaned_dir):
        if file_name.endswith('.csv'):
            file_path = os.path.join(cleaned_dir, file_name)
            try:
                df = pd.read_csv(file_path, on_bad_lines='skip', header=0)
                df_list.append(df)
                print_progress(f"Added file: {file_name}", "📄")
            except pd.errors.ParserError as e:
                print(
                    f"⚠️ Skipping file {file_name} due to parsing error: {e}")

    if df_list:
        merged_df = pd.concat(df_list, ignore_index=True)
        print("Before renaming columns:", merged_df.columns.tolist())

        merged_df.rename(columns={
            "YEAR": "YEAR",
            "MO": "MONTH",
            "DY": "DAY",
            "HR": "HOUR",
            "ALLSKY_SFC_SW_DWN": "IRRADIANCE",
            "T2M": "TEMPERATURE",
            "QV2M": "DEW",
            "RH2M": "HUMIDITY",
            "PRECTOTCORR": "PRECIPITATION",
            "WD10M": "WIND DIRECTION",
            "WS10M": "WIND SPEED",
            "PS": "PRESSURE"
        }, inplace=True)

        print("After renaming columns:", merged_df.columns.tolist())

        merged_df["DEW"] = calculate_dew_point(
            merged_df["TEMPERATURE"], merged_df["HUMIDITY"])
        merged_df["WET BULB TEMPERATURE"] = calculate_wet_bulb(
            merged_df["TEMPERATURE"], merged_df["HUMIDITY"])
        print("Final columns in dataframe:", merged_df.columns.tolist())

        if not os.path.exists(merged_dir):
            os.makedirs(merged_dir)
            print_progress(f"Created merged directory: {merged_dir}")

        output_path = os.path.join(merged_dir, output_file)
        merged_df.to_csv(output_path, index=False, sep=';')
        print_progress(f"Merged file saved as {output_path}", "🎉")
    else:
        print("⚠️ No valid CSV files to merge.")


def main():
    data_dir = 'data'
    cleaned_dir = os.path.join(data_dir, 'cleaned')
    merged_dir = os.path.join(data_dir, 'merged')
    output_file = 'merged_data.csv'
    create_cleaned_dir(data_dir, cleaned_dir)
    clean_and_copy_csv_files(data_dir, cleaned_dir)
    merge_csv_files(cleaned_dir, merged_dir, output_file)


if __name__ == '__main__':
    main()
