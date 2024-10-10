import pandas as pd

def parse_tle_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    satellite_data = []

    for i in range(0, len(lines), 3):
        line_1 = lines[i+1].strip()  
        line_2 = lines[i+2].strip()  
        
        satellite_info = {
            'satellite_catalog_number': line_1[2:7].strip(),
            'international_designator': line_1[9:17].strip(),
            'epoch_year': line_1[18:20].strip(),
            'epoch_day': line_1[20:32].strip(),
            'mean_motion_derivative': line_1[33:43].strip(),
            'mean_motion_derivative_2nd': line_1[44:52].strip(),
            'bstar_drag_term': line_1[53:61].strip(),
            'element_number': line_1[64:68].strip(),
            'inclination': line_2[8:16].strip(),
            'right_ascension': line_2[17:25].strip(),
            'eccentricity': line_2[26:33].strip(),
            'argument_of_perigee': line_2[34:42].strip(),
            'mean_anomaly': line_2[43:51].strip(),
            'mean_motion': line_2[52:63].strip(),
            'revolution_number_at_epoch': line_2[63:68].strip()
        }

        satellite_data.append(satellite_info)

    return satellite_data

def tle_to_dataframe(parsed_data):
    df = pd.DataFrame(parsed_data)
    return df

def main():
    tle_file_path = 'data/raw/tle_data.tle'

    parsed_tle_data = parse_tle_file(tle_file_path)

    tle_df = tle_to_dataframe(parsed_tle_data)

    tle_df.to_csv('data/output/parsed_tle_data.csv', index=False)
    print(tle_df.head())

if __name__ == "__main__":
    main()
