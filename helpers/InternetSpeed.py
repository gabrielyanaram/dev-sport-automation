from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options with desired network conditions
options = Options()
options.add_experimental_option("perfetto", {
    "domContentLoadedEventSent": True,
    "loadEventFired": True,
    "networkConditions": {
        "offline": False,  # Set to True for offline simulation
        "latency": 500,  # Latency in milliseconds
        "downloadThroughput": 500 * 1024,  # Download speed in bps (bits per second)
        "uploadThroughput": 500 * 1024  # Upload speed in bps (bits per second)
    }
})

# Create a ChromeDriver instance with the options
driver = webdriver.Chrome(options=options)


