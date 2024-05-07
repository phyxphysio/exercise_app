import plotly.express as px
import plotly.offline as po
import pandas as pd


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
    fig = px.bar(clinician_rates, x="Clinician name", y="Case Acceptance Rate")

    return po.plot(fig, auto_open=False, output_type="div")
