# gve_devnet_cisco_call_home_service_auto_config
prototype script that reads device details from an Excel file and initializes the Call Home feature for Cisco routers and switches


## Contacts
* Jorge Banegas

## Solution Components
* CSR
* Netmiko

## Instructions
(optional) This first step is optional if the user wants to leverage a virtual environment to install python packages

```shell
pip install virtualenv
virtualenv env
source env/bin/activate
```

Install python dependencies 

```shell
pip install -r requirements.txt
```

Make sure to properly include the required details inside file.xlsx. 
Required details include 
- Host IP
- SSH username
- SSH pasword

Enter the desired email address to change to main.py line 32

```python
   email = "x@domain.com"
```

## Usage

To script after entering the devices detail on the spreadsheet:


    $ python main.py

A logging file will be produced to show which devices has sucessfully made the changes


# Screenshots

![/IMAGES/output.png](/IMAGES/output.png)

![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.