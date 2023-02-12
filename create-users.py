#!/usr/bin/python3
import os
import re
import sys


def main():
    for line in sys.stdin:
        # Add a line of code here. Use re.match and create a regular expression to
        # check for the presence of a  # at the start of a line.We want to skip any
        # lines in the file that starts with a hashtag:
        # Create your regex(I suggest re.match) and save the result in a variable
        # named “match”
        match = re.match(r'^#', line)
        # strip any whitespace and split into into an array
        fields = line.strip().split(':')
        if match or len(fields) != 5:  # explain what this is checking for and why
            continue  # the continue here is for the FOR loop. So if the line
            # starts with a # or does NOT have five fields, we skip it
        username = fields[0]
        password = fields[1]
        # it is used to create a string with the user's firstname and lastname (fields[3] and fields[2]) and the rest of the fields are empty (,,,)
        gecos = "%s %s,,," % (fields[3], fields[2])
        groups = fields[4].split(',')
        print("==> Creating account for %s..." % (username))
        cmd = "/usr/sbin/adduser --disabled-password --gecos '%s' %s" % (
            gecos, username)
        # print cmd
        os.system(cmd)  # what does this line do?
        print("==> Setting the password for %s..." % (username))
        cmd = "/bin/echo -ne '%s\n%s' | /usr/bin/sudo /usr/bin/passwd %s" % (
            password, password, username)
        # print cmd
        os.system(cmd)
        # this loop is for the groups that the user belongs to and it is used to add the user to the groups.
        for group in groups:
            if group != '-':
                print("==> Assigning %s to the %s group..." %
                      (username, group))
                cmd = "/usr/sbin/adduser %s %s" % (username, group)
                # print cmd
                os.system(cmd)


if __name__ == '__main__':
    main()
