"""
Exercise 1: Loading Programs
Data analysis tool demonstrating pip and Poetry dependency management.
"""

import sys
import importlib
from typing import Optional


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation",
    "numpy": "Numerical computation",
    "matplotlib": "Visualization",
}

OPTIONAL_PACKAGES = {
    "requests": "Network access",
}


def check_package(name: str) -> Optional[str]:
    """Try to import a package and return its version, or None if missing."""
    try:
        mod = importlib.import_module(name)
        version: str = getattr(mod, "__version__", "unknown")
        return version
    except ImportError:
        return None


def check_dependencies() -> dict[str, Optional[str]]:
    """Check all required and optional packages."""
    results: dict[str, Optional[str]] = {}
    all_packages = {**REQUIRED_PACKAGES, **OPTIONAL_PACKAGES}
    for pkg in all_packages:
        results[pkg] = check_package(pkg)
    return results


def show_dependency_status(
    results: dict[str, Optional[str]]
) -> bool:
    """Print dependency status. Returns True if all required are present."""
    print("Checking dependencies:")
    all_ok = True

    for pkg, label in REQUIRED_PACKAGES.items():
        version = results.get(pkg)
        if version:
            print(f"  [OK] {pkg} ({version}) - {label} ready")
        else:
            print(f"  [MISSING] {pkg} - {label} NOT available")
            all_ok = False

    for pkg, label in OPTIONAL_PACKAGES.items():
        version = results.get(pkg)
        if version:
            print(f"  [OK] {pkg} ({version}) - {label} ready")

    return all_ok


def show_install_instructions() -> None:
    """Show how to install missing packages with pip and Poetry."""
    print()
    print("Missing dependencies detected!")
    print()
    print("Install with pip:")
    print("  pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("  poetry install")
    print("  poetry run python loading.py")
    print()
    print("--- pip vs Poetry comparison ---")
    print(
        "  pip         : simple, no lock file by default, "
        "manual version pinning"
    )
    print(
        "  Poetry      : lock file (poetry.lock), "
        "dependency resolver, virtual env built-in"
    )


def run_analysis() -> None:
    """Run the Matrix data analysis and generate a visualization."""
    import numpy as np  # type: ignore
    import pandas as pd  # type: ignore
    import matplotlib  # type: ignore
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # type: ignore

    print()
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    rng = np.random.default_rng(42)
    time_steps = np.arange(1000)
    signal = (
        rng.normal(0, 1, 1000).cumsum()
        + rng.uniform(-0.5, 0.5, 1000)
    )
    noise = rng.normal(0, 0.3, 1000)

    df = pd.DataFrame(
        {
            "time": time_steps,
            "signal": signal,
            "noise": noise,
            "combined": signal + noise,
        }
    )

    rolling_mean: pd.Series = (
        df["combined"].rolling(window=50).mean()
    )

    print("Generating visualization...")

    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    fig.suptitle("Matrix Data Analysis", fontsize=16, color="green")
    fig.patch.set_facecolor("black")

    for ax in axes:
        ax.set_facecolor("#0a0a0a")
        ax.tick_params(colors="green")
        ax.spines[:].set_color("green")

    axes[0].plot(
        df["time"], df["combined"],
        color="#00ff41", linewidth=0.7, alpha=0.8, label="Raw signal"
    )
    axes[0].plot(
        df["time"], rolling_mean,
        color="#ff4400", linewidth=2, label="Rolling mean (50)"
    )
    axes[0].set_title(
        "Matrix Signal Stream", color="green"
    )
    axes[0].set_xlabel("Time", color="green")
    axes[0].set_ylabel("Amplitude", color="green")
    axes[0].legend(
        facecolor="black", labelcolor="green", edgecolor="green"
    )

    axes[1].hist(
        df["combined"], bins=50,
        color="#00ff41", edgecolor="black", alpha=0.85
    )
    axes[1].set_title(
        "Signal Distribution", color="green"
    )
    axes[1].set_xlabel("Value", color="green")
    axes[1].set_ylabel("Frequency", color="green")

    stats_text = (
        f"Mean: {df['combined'].mean():.2f}  "
        f"Std: {df['combined'].std():.2f}  "
        f"Min: {df['combined'].min():.2f}  "
        f"Max: {df['combined'].max():.2f}"
    )
    fig.text(
        0.5, 0.01, stats_text,
        ha="center", color="#00ff41", fontsize=9
    )

    plt.tight_layout(rect=(0, 0.03, 1, 0.96))
    output_path = "matrix_analysis.png"
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close()

    print()
    print("Analysis complete!")
    print(f"Results saved to: {output_path}")


def show_package_versions(
    results: dict[str, Optional[str]]
) -> None:
    """Show a comparison table of installed package versions."""
    print()
    print("--- Installed package versions ---")
    all_pkgs = {**REQUIRED_PACKAGES, **OPTIONAL_PACKAGES}
    for pkg, label in all_pkgs.items():
        ver = results.get(pkg)
        status = ver if ver else "NOT INSTALLED"
        print(f"  {pkg:<12} {status:<15}  ({label})")


def main() -> None:
    """Main entry point."""
    print("LOADING STATUS: Loading programs...")
    print()

    results = check_dependencies()
    all_ok = show_dependency_status(results)
    show_package_versions(results)

    if not all_ok:
        show_install_instructions()
        sys.exit(1)

    run_analysis()


if __name__ == "__main__":
    main()
