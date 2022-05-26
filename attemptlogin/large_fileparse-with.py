#!/usr/bin/python3
loginfail = 0
with open("/home/student/mycode/attemptlogin/keystone.common.wsgi", "r") as kfile:
        for line in kfile:
            if "- - - - -] Authorization failed" in line:
                loginfail += 1
kfile.close()
print("The number of failed log in attempts is", loginfail)

