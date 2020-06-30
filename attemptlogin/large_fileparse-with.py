#!/usr/bin/python3

def main():
    loginfail = 0
    loginSuccess = 0

    with open("/home/student/mycode/attemptlogin/keystone.common.wsgi") as kfile:

        for line in kfile:
            if "- - - - -] Authorization failed" in line:
                loginfail += 1
            elif "-] Authorization failed" in line:
                loginSuccess +=1

    print("The number of failed log in attempts is ", loginfail)
    print("The number of login successful", loginSuccess)

if __name__ == "__main__":
    main()
