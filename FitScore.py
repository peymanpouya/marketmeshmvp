import pandas as pd
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

# Specify the path to your CSV file in Google Drive
# Replace 'YourFolder/SubFolder/your_file.csv' with your actual file path
file_path = '/content/drive/My Drive/MarketMesh_Data/mena_markets.csv'
# Load the CSV
data = pd.read_csv(file_path)

# Example: Calculate Fit Score (from your prior code)
data['fit_score'] = (data['market_size'] / data['market_size'].max() * 50) - \
                    (data['competition'] * 30) - (data['risk'] * 20)
data['fit_score'] = data['fit_score'].clip(0, 100)
print(data[['country', 'fit_score']])