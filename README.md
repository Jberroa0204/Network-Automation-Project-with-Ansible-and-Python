Network Automation Project with Ansible and Python
Introduction
This report details a network automation project focused on managing Cisco devices using Ansible and Python. The project's main objectives were to automate sending configuration commands, retrieving outputs from show commands, and ensuring connectivity with network devices.

Environment Setup
Python and Ansible Installation
Python and Ansible were installed on a macOS system.
Ansible collections for Cisco were installed using ansible-galaxy collection install cisco.ios.
Inventory File Configuration
An inventory file was created to define the Cisco device (sandbox-iosxe-latest-1.cisco.com) with necessary credentials and connection settings.
Ansible Playbooks
Configuration Playbook (configure_cisco.yml)
Purpose: To send configuration commands to the Cisco device.
Key Commands:
Set hostname: hostname MyCiscoRouter.
Other configuration commands can be added similarly.
Show Commands Playbook (show_commands.yml)
Purpose: To execute and display outputs from show commands.
Key Commands:
Execute show version and display the output.
Python Script for Automation (network_automation.py)
A Python script was written to run these Ansible playbooks.
The script used the subprocess module to execute ansible-playbook commands.
Testing and Validation
The playbooks were tested against the Cisco sandbox environment.
Successful execution was confirmed for both configuration changes and retrieval of show command outputs.
Troubleshooting and Resolutions
Encountered Issues:
Ansible PATH Issue:

Initial error due to Ansible not being in the PATH.
Resolved by adding Ansible's installation path to the system's PATH variable.
SSH Key Verification:

Encountered SSH key verification issue.
Resolved by manually SSH-ing into the device and accepting the key.
Syntax and Quotation Errors:

Faced syntax errors in the playbooks.
Resolved by correcting string quotations and formatting.
Conclusion and Learning Outcomes
This project provided hands-on experience with network automation using Ansible and Python. Key learnings include:

Ansible playbook creation and execution.
Integrating Python with Ansible for network automation.
Troubleshooting common issues in network automation tasks.
Appendix
Resources Used
Ansible Documentation
Python.org

