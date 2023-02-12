# INET 4031 - Lab 4 - Part 2
## Linux User Management Part 2

The `create-users.py` script reads in a list of user accounts and creates corresponding system accounts on the system.

## Input Format
The input to the script is a list of user accounts in the following format:
`<username>:<password>:<lastname>:<firstname>:<group1,group2,group3,...>`

Each line in the input file represents a single user account and the fields are separated by a colon (:). The group field is a list of group names that the user should belong to, separated by commas. Lines that start with a # are considered comments and are ignored by the script.

## Usage
The script can be executed as follows:
`sudo python3 create-users.py < create-users.input`

where create-users.input is the file containing the list of user accounts.

## Output
The script outputs the status messages for each user account created, including the creation of the user account, setting the password, and adding the user to the specified groups.