"""
Program: Ohio Unemployment Plot (Lab 16, #1)
Author: (James) - Dyemydym Branco Vieira
Purpose: Read unemployment data from OHUR.csv and make a simple line graph.
Date: 2025-12-07
"""

import csv
from pathlib import Path

import matplotlib.pyplot as plt


def main():
    """Read data from OHUR.csv and plot unemployment rates."""

    # Make a Path to OHUR.csv.
    csv_path = Path(__file__).with_name("OHUR.csv")

    # store the x-values y-values (rate).
    record_numbers = []
    rates = []

    # Open and read the CSV file.
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.reader(f)

        # Read the header row.
        header_row = next(reader)

        # Print the header row with indexes
        print("Header indexes:")
        for index, column_name in enumerate(header_row):
            print(index, column_name)

        # read each remaining rows.
        for record_index, row in enumerate(reader, start=1):
            try:
                rate = float(row[1])
            except (ValueError, IndexError):
                print(f"Skipping bad or missing data on row {record_index}: {row}")
            else:
                record_numbers.append(record_index)
                rates.append(rate)

    # Make a simple line plot of the rates.
    plt.style.use("seaborn-v0_8")
    fig, ax = plt.subplots()

    ax.plot(record_numbers, rates, linewidth=2)

    # Add a title and axis labels.
    ax.set_title("Ohio Unemployment Rate Over Time", fontsize=16)
    ax.set_xlabel("Record number", fontsize=12)
    ax.set_ylabel("Unemployment rate (%)", fontsize=12)

    # Make tick labels a little smaller.
    ax.tick_params(axis="both", labelsize=10)

    # Adjust layout and show the graph.
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
