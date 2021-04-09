# Scammer HTTP Flood
This module is intended to be used to combat scammers by flooding their server with POST requests. By successfully doing so, it fills their database with fake data and makes it difficult to decipher which data is real and which isn't. The script generates a fake username and a fake password, which is then sent to the scammer's server. 

For demonstration, a mock server is included in this project and the script is configured to send the data to the server.

To improve efficiency, this script uses threading to send requests concurrently.

This project was inspired by Engineer Man, who wrote a similar script to combat scammers as well.