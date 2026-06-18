from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.interpolate import make_interp_spline


BASE_DIR = Path(__file__).resolve().parent
DEMAND_FILE = BASE_DIR / "data_demand_graphs.csv"
ROI_FILE = BASE_DIR / "data_roi_graphs.csv"
FIGURE_WIDTH_CM = 14.5
FIGURE_HEIGHT_CM = 8
ROI_FIGURE_HEIGHT_CM = 13


def load_graph_data() -> tuple[pd.DataFrame, pd.DataFrame]:
    """
    Load the CSV files used for the presentation graphs.
    """
    demand_df = pd.read_csv(DEMAND_FILE, sep=";", decimal=",")
    roi_df = pd.read_csv(ROI_FILE, sep=";", decimal=",")

    demand_df = demand_df.rename(columns={demand_df.columns[0]: "Scenario"})
    roi_df = roi_df.rename(columns={roi_df.columns[0]: "Scenario"})

    return demand_df, roi_df


def smooth_curve(x_values: np.ndarray, y_values: np.ndarray, points: int = 300) -> tuple[np.ndarray, np.ndarray]:
    x_smooth = np.linspace(x_values.min(), x_values.max(), points)
    spline = make_interp_spline(x_values, y_values, k=2)
    y_smooth = spline(x_smooth)
    return x_smooth, y_smooth


def set_presentation_style() -> None:
    plt.rcParams.update(
        {
            "font.size": 14,
            "axes.titlesize": 14,
            "axes.labelsize": 12,
            "xtick.labelsize": 10,
            "ytick.labelsize": 10,
            "legend.fontsize": 8,
        }
    )


def plot_demand_graph(demand_df: pd.DataFrame) -> None:
    months = np.array([0, 12, 36])

    set_presentation_style()

    fig, ax1 = plt.subplots(figsize=(FIGURE_WIDTH_CM / 2.54, FIGURE_HEIGHT_CM / 2.54))
    ax2 = ax1.twinx()

    colors = {
        "Conservative": "#1f77b4",
        "Realistic": "#2ca02c",
        "Optimistic": "#ff7f0e",
    }

    for scenario in ["Conservative", "Realistic", "Optimistic"]:
        row = demand_df[demand_df["Scenario"] == scenario].iloc[0]

        individual_values = np.array([0, row["Individual 12"], row["Individual 36"]])
        subscription_values = np.array([0, row["Subscription 12"], row["Subscription 36"]])

        x_smooth, y_smooth = smooth_curve(months, individual_values)
        ax1.plot(
            x_smooth,
            y_smooth,
            label=f"{scenario} - Individual",
            color=colors[scenario],
            linewidth=2,
        )
        ax1.scatter(
            months,
            individual_values,
            s=50,
            color=colors[scenario],
            zorder=3,
        )

        x_smooth, y_smooth = smooth_curve(months, subscription_values)
        ax2.plot(
            x_smooth,
            y_smooth,
            label=f"{scenario} - Subscription",
            color=colors[scenario],
            linestyle="--",
            linewidth=2,
        )
        ax2.scatter(
            months,
            subscription_values,
            s=50,
            color=colors[scenario],
            zorder=3,
        )

    ax1.set_xlabel("Month")
    ax1.set_ylabel("Individual demand")
    ax2.set_ylabel("Subscription demand")
    ax1.set_xticks([0, 12, 36])
    ax1.set_title("Demand evolution by scenario")
    ax1.grid(True, linestyle="--", alpha=0.3)

    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="best")

    plt.tight_layout()
    # Keep the full canvas so the exported image preserves the intended physical size.
    plt.savefig(BASE_DIR / "graph_demand.png", dpi=300)
    plt.show()


def plot_roi_graph(roi_df: pd.DataFrame) -> None:
    months = [0, 12, 36]
    x = np.arange(len(months))
    bar_width = 0.24
    value_scale = 1000.0

    set_presentation_style()

    fig, axes = plt.subplots(
        nrows=3,
        ncols=1,
        sharex=True,
        figsize=(FIGURE_WIDTH_CM / 2.54, ROI_FIGURE_HEIGHT_CM / 2.54),
    )

    colors = {
        "cost": "#f4cccc",
        "revenue": "#d9ead3",
        "profit_positive": "#2ca02c",
        "profit_negative": "#d62728",
    }

    for ax, scenario in zip(axes, ["Conservative", "Realistic", "Optimistic"]):
        row = roi_df[roi_df["Scenario"] == scenario].iloc[0]

        cost_values = np.array(
            [
                row["Cost 0"],
                row["Cost 0-12"],
                row["Cost 0-36"],
            ]
        ) / value_scale
        revenue_values = np.array(
            [
                row["Revenue 0"],
                row["Revenue 0-12"],
                row["Revenue 0-36"],
            ]
        ) / value_scale
        profit_values = revenue_values - cost_values
        profit_colors = [colors["profit_positive"] if value >= 0 else colors["profit_negative"] for value in profit_values]

        ax.bar(x - bar_width, cost_values, width=bar_width, color=colors["cost"], label="Cost")
        ax.bar(x, revenue_values, width=bar_width, color=colors["revenue"], label="Revenue")
        ax.bar(x + bar_width, profit_values, width=bar_width, color=profit_colors, label="Revenue - cost")

        roi_36_value = row["ROI 0-36"] * 100
        roi_36_y = profit_values[2]
        roi_36_va = "bottom" if roi_36_y >= 0 else "top"
        ax.annotate(
            f"{roi_36_value:.1f}%",
            xy=(x[2] + bar_width, roi_36_y),
            xytext=(0, 4 if roi_36_y >= 0 else -4),
            textcoords="offset points",
            ha="center",
            va=roi_36_va,
            fontsize=10,
            color=colors["profit_positive"] if roi_36_y >= 0 else colors["profit_negative"],
        )

        ax.axhline(0, color="black", linewidth=0.8)
        ax.set_title(f"{scenario} scenario")
        ax.grid(True, axis="y", linestyle="--", alpha=0.3)

    axes[-1].set_xticks(x)
    axes[-1].set_xticklabels([str(month) for month in months])
    axes[-1].set_xlabel("Month", labelpad=8)

    fig.text(0.04, 0.5, "Thousands of â‚¬", va="center", rotation="vertical")
    axes[0].legend(loc="upper left", ncol=3, frameon=False)
    fig.subplots_adjust(left=0.14, right=0.98, top=0.94, bottom=0.13, hspace=0.52)

    fig.savefig(BASE_DIR / "graph_roi.png", dpi=300)
    plt.show()


def main() -> None:
    demand_df, roi_df = load_graph_data()
    # plot_demand_graph(demand_df)
    plot_roi_graph(roi_df)


if __name__ == "__main__":
    main()
