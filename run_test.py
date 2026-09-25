"""
Runner script for Capstone Assignment 1: Web Application Automation with Selenium WebDriver.
Executes the PyTest test suite, generates HTML execution reports, and logs captured screenshots.
"""

import os
import sys
import pytest


def main():
    # Ensure current directory is in sys.path
    project_root = os.path.dirname(os.path.abspath(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Ensure output directories exist
    reports_dir = os.path.join(project_root, "reports")
    screenshots_dir = os.path.join(project_root, "screenshots")
    os.makedirs(reports_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    report_file = os.path.join(reports_dir, "execution_report.html")

    print("=" * 70)
    print("  CAPSTONE ASSIGNMENT 1: SELENIUM WEBDRIVER AUTOMATION")
    print("  Application: AutomationExercise (https://automationexercise.com)")
    print("=" * 70)
    print(f"Running test suite with PyTest...")
    print(f"Target Report: {report_file}")
    print("=" * 70)

    # Configure pytest arguments
    args = [
        "-v",
        "-s",
        f"--html={report_file}",
        "--self-contained-html",
        os.path.join(project_root, "tests", "test_ecommerce.py"),
    ]

    exit_code = pytest.main(args)

    print("\n" + "=" * 70)
    print("  EXECUTION SUMMARY")
    print("=" * 70)
    if exit_code == 0:
        print("  Status: PASSED")
    else:
        print(f"  Status: FAILED (Exit Code: {exit_code})")

    print(f"  HTML Report: file:///{report_file.replace(os.sep, '/')}")

    # List screenshots
    if os.path.exists(screenshots_dir):
        shots = [f for f in os.listdir(screenshots_dir) if f.endswith(".png")]
        print(f"  Captured Screenshots ({len(shots)} files):")
        for shot in sorted(shots):
            full_p = os.path.join(screenshots_dir, shot)
            print(f"    - {shot}: file:///{full_p.replace(os.sep, '/')}")
    print("=" * 70)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
