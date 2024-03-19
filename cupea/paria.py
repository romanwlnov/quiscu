from selenium.webdriver.common.keys import Keys

def change_on_last_tab(driver):
    """Switches to the last tab in the current window.

    Args:
        driver: The WebDriver instance used to interact with the browser.
    """

    # Get the current window handle.
    current_window = driver.current_window_handle

    # Get all the window handles.
    window_handles = driver.window_handles

    # Switch to the last window handle.
    driver.switch_to.window(window_handles[-1])

    # Check if the current window handle is the same as the last window handle.
    if current_window != driver.current_window_handle:
        # The current window handle is not the same as the last window handle.
        # This means that the driver has successfully switched to the last tab.
        return True
    else:
        # The current window handle is the same as the last window handle.
        # This means that the driver has failed to switch to the last tab.
        return False
