from road_profile_viewer.visualization import create_dash_app

# =============================================================================
# CAMERA AND RAY CALCULATIONS
# =============================================================================


def helper_function(val: float) -> float:
    """Unused helper function that previously violated naming convention"""
    result = val * 2  # Fixed: Proper spacing around operators
    return result


# =============================================================================
# MAIN ENTRY POINT
# =============================================================================


def main() -> None:
    """
    Main function to run the Dash application.
    """
    app = create_dash_app()
    print("Starting Road Profile Viewer...")
    print("Open your browser and navigate to: http://127.0.0.1:8050/")
    print("Press Ctrl+C to stop the server.")
    app.run(debug=True)


if __name__ == "__main__":
    main()
