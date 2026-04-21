import importlib
import sys


REQUIRED_PACKAGES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def load_dependency(package_name):
    """Return (module, version) if import succeeds, else (None, None)."""
    try:
        module = importlib.import_module(package_name)
    except ImportError:
        return None, None

    version = getattr(module, "__version__", "unknown")
    return module, version


def print_dependency_status():
    """Print package availability and collect imported modules."""
    imported_modules = {}
    missing = []

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")

    for package_name, description in REQUIRED_PACKAGES.items():
        module, version = load_dependency(package_name)
        if module is None:
            print(f"[MISSING] {package_name} - required for this program")
            missing.append(package_name)
        else:
            print(f"[OK] {package_name} ({version}) - {description}")
            imported_modules[package_name] = module

    return imported_modules, missing


def print_environment_comparison():
    """Show quick pip vs Poetry installation hints and runtime context."""
    is_poetry_like = (
        "poetry" in sys.executable.lower() or "pypoetry"
        "" in sys.executable.lower()
    )

    print()
    print("Dependency management comparison:")
    print("- pip: install with `pip install -r requirements.txt`")
    print("- Poetry: install with `poetry install`")
    print("- Poetry run: `poetry run python loading.py`")
    if is_poetry_like:
        print("Runtime environment: Poetry-managed environment detected")
    else:
        print("Runtime environment: standard Python/pip environment detected")


def print_missing_instructions(missing):
    """Provide helpful setup guidance when dependencies are missing."""
    print()
    print("Cannot continue: missing dependencies detected.")
    print("Missing packages: " + ", ".join(missing))
    print()
    print("Install with pip:")
    print("pip install -r requirements.txt")
    print()
    print("Install with Poetry:")
    print("poetry install")


def run_analysis(pandas_module, numpy_module, matplotlib_module):
    """Build Matrix-like data with numpy,"
    " analyze with pandas, and visualize."""
    print()
    print("Analyzing Matrix data...")

    points = 1000
    rng = numpy_module.random.default_rng(42)
    ticks = numpy_module.arange(points)
    signal = numpy_module.sin(ticks / 28.0) + rng.normal(0, 0.35, size=points)

    data = pandas_module.DataFrame({"tick"
                                    "": ticks, "signal": signal})
    data["rolling_mean"] = data[
        "signal"
        ].rolling(window=25, min_periods=1).mean()

    print(f"Processing {len(data)} data points...")
    print("Generating visualization...")
    pyplot = matplotlib_module.pyplot
    pyplot.figure(figsize=(10, 5))
    pyplot.plot(
        data["tick"], data[
            "signal"
            ], linewidth=0.8, alpha=0.55, label="Raw signal"
    )
    pyplot.plot(
        data["tick"], data[
            "rolling_mean"
            ], linewidth=2.0, label="Rolling mean (25)"
    )
    pyplot.title("Matrix Signal Analysis")
    pyplot.xlabel("Tick")
    pyplot.ylabel("Signal")
    pyplot.legend()
    pyplot.tight_layout()
    pyplot.savefig("matrix_analysis.png")
    pyplot.close()

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main():
    modules, missing = print_dependency_status()
    print_environment_comparison()

    if missing:
        print_missing_instructions(missing)
        return 1

    # Import pyplot lazily only after matplotlib is confirmed present.
    matplotlib_pyplot = importlib.import_module("matplotlib.pyplot")
    modules["matplotlib"].pyplot = matplotlib_pyplot

    run_analysis(modules["pandas"], modules["numpy"], modules["matplotlib"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
