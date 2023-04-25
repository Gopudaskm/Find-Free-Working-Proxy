Overview
"find_proxy.py" is a Python program that allows users to find working proxies for a specific website with customizable number of trials.
 The program collects proxies from two different sources, "https://free-proxy-list.net/" and "https://www.proxy-list.download/", and tests them by attempting to connect to the target website. 
The program output a JSON files that stores the desired trial number.

Required Libraries
*requests
*lxml
*beautifulsoup4
*json

Usage
To use the "find_proxy.py" program, simply run the Python script and specify the target website and the number of trials to run.
 By default, the program will use the target website "https://www.google.com" and 10 trials. However, users can customize these parameters by modifying the TARGET_URL and NUM_TRIALS variables at the beginning of the script.

Once the program is run, it will first collect a list of proxies from the two sources mentioned above.
It will then test each proxy by attempting to connect to the target website the specified number of times. 
Proxies that successfully connect to the website will be stored in a JSON file named "Working_proxy.json".

Disclaimer
Please note that this program is for educational purposes only, and the proxies collection may not work if the websites are altered.
Additionally, the program is not intended for any illegal or unauthorized use. Use of this program is at your own risk.