# demonstrate the logging api in Python

# TODO: use the built-in logging module
import logging

# TODO: Use basicConfig to configure logging
logging.basicConfig(level=logging.DEBUG, filename="output.log")

# TODO: Try out each of the log levels
logging.debug("This is a debug-level message")
logging.info("This is a info-level message")
logging.warning("This is a warning-level message")
logging.error("This is a error-level message")
logging.critical("This is a critical-level message")

# TODO: Output formatted strings to the log
var1 = "--here--"
var2 = 10
logging.info(f"Here's a str variable {var1}, and an int: {var2}")
