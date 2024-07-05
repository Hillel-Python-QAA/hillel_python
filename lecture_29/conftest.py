import base64
import logging
import os

import pytest
import pytest_html
from pytest_metadata.plugin import metadata_key


def pytest_html_report_title(report):
    report.title = "Pytest HTML Report Example"


def pytest_configure(config):
    config.stash[metadata_key]["Project"] = "Pytest With Hillel"


def pytest_html_results_table_row(report, cells):
    if report.failed:
        del cells[:]


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()
    extras = getattr(report, "extras", [])

    # Logger initializing
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if report.when == "call":
        # Assuming your screenshot is saved correctly at the specified path
        screenshot_path = os.getenv("SCREENSHOT_PATH", "./lecture_29/report/HW_1.png")
        logger.debug(screenshot_path)
        with open(screenshot_path, "rb") as image_file:
            encoded_string = base64.b64encode(
                image_file.read()
            ).decode()  # https://github.com/pytest-dev/pytest-html/issues/265
        extras.append(pytest_html.extras.png(encoded_string))
        report.extras = extras