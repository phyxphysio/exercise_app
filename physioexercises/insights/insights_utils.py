import matplotlib.pyplot as plt
import pandas as pd
import os

def process_data(file):
    case_acceptance_df = pd.read_csv(file)
    case_acceptance_df["Case Acceptance Rate"] = pd.to_numeric(
        case_acceptance_df["Case Acceptance Rate"], errors="coerce"
    )
    clinician_rates = (
        case_acceptance_df.groupby("Clinician name")["Case Acceptance Rate"]
        .mean()
        .reset_index()
    )
    clinician_rates = clinician_rates.sort_values(
        "Case Acceptance Rate", ascending=False
    )

    # Path to save the image
    img_path = os.path.join('static', 'images', 'plot.png')

    # Create the bar chart
    plt.figure(figsize=(8, 6))
    plt.bar(
        clinician_rates["Clinician name"],
        clinician_rates["Case Acceptance Rate"],
        color="skyblue",
    )
    plt.title("Case Acceptance Rate per Clinician")
    plt.xlabel("Clinician Name")
    plt.ylabel("Average Case Acceptance Rate")
    plt.ylim(0, 1)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot as a static file
    plt.savefig(img_path)
    plt.close()
    
    return img_path
