# Messages Automation
Messages Automation in Python using selenium which is capable of sending messages and images to any desired recipient given by user on WhatsApp Web.

# Requirements
Python 2 or Python 3 (preferred)

# Run on local machine
1. Clone the repository
```
git clone https://github.com/Lavanyask03/whatsapp-automation.git
```

2. Install required packages via pip. (Type in anaconda prompt or python prompt)
```
pip install -r requirements.txt
```

3. Open and run the notebook using Jupyter notebook.
```
jupyter-notebook WhatsApp_Automation.ipynb
```

## Note
Do change the path for chromedriver.exe file.

# Usage
Enter in the recipient's name and message to send it, image can also be sent.
The QR Code scanning cannot be automated and should be done manually when the Whatsapp Web page opens.

# Running the Automation Script via GitHub Actions
You can also run the automation script using GitHub Actions.

1. Go to your GitHub repository.
2. Click on the "Actions" tab.
3. Select the "FA Message Automation" workflow from the list on the left.
4. Click the "Run workflow" button on the right.
5. Fill in the input fields for `message`, `filepath`, and `contacts`.
6. Click the "Run workflow" button to start the workflow with the provided inputs.

This will execute the workflow immediately, running your script and generating the log file. You can download the log file from the GitHub Actions run page to see the detailed report of the execution.