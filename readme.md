#### Welcome Ndung'u's  Sitecore Interview questions documentation

To see the questions, open ./assignment.pdf
The code was tested on **MacOs Big Sur v 11.2.2**

#### Pre-requisites
Please follow these steps to set up your environment:
1. [Install Python 3.8.0] (https://www.python.org/downloads/release/python-380/)
2. Navigate to the root of the project
3. Run command `pip install -r requirements.txt` and wait dependencies to be resolved
4. Activate virtual environment using command `source env/bin/activate`
5. Download and install Selenium Driver for chrome [for your operating system](https://chromedriver.storage.googleapis.com/index.html?path=89.0.4389.23/)

6. Extract the downloaded chome driver and move it to a directory of your choice. Remember this path, it will be used while instantiating the chrome driver

7. [Optional] Open the moved driver with terminal by right *click -> openwith -> terminal.app*. This helps bypass **MacOs Big Sur v 11.2.2** security checks that marks chromedriver as malware.

8. Finally, (not related to the above) install postman v2.1



## Running the project
1. For question 1, run `python3 question1_script.py`
2. For question 2 run `behave`
3. For question 3:
    - Open postman
    - Import postman/weatherNY.json as a copy to ensure no conflicts with your existing collections
    - expand the imported collection
    - Select the only request in the collection
    - Send the request (By clicking send button)
    - Once request is finished, switch to **Test Results** tab to see that the test fails.



