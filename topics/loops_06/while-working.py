#!/usr/bin/env python3

secret = "swordfish"
pw = ''
auth = False
count = 0
max_attempt = 5

while pw != secret:
    count += 1
    if count > max_attempt:
        break
    elif count == 3:
        continue
    pw = input("{} What's the secret word?".format(count))
else:
    auth = True

print("Authorized" if auth else "calling police!")