# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
import kagglehub
from kagglehub import KaggleDatasetAdapter

# Set the path to the file you'd like to load
file_path = "/Users/felix/Desktop/Code/ML/Heart_Thing/data/data.csv"

# Load the latest version
df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "redwankarimsony/heart-disease-data",
    "data.csv",
)

print("First 5 records:", df.head())
