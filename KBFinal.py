#Kaden Becker Final Project 2FA System

""" READ ME:    it is important to use the terminal and use the code (pip install pyotp) for this code to work"""
import pyotp
import time

secret_key = pyotp.random_base32()
print(f"Secret Key: {secret_key}")

totp = pyotp.TOTP(secret_key, interval=20)

while True:
    otp = totp.now()
    print(f"Current One time password: {otp}")

    #Verify if the One Time Password is correct or incorrect
    user_input = input("Enter OTP for verification (or 'exit'): ")
    if user_input.lower() == 'exit':
        break
    if totp.verify(user_input):
        print("One time password verification successful.")
    else:
        print("One time password verification failed.")
    time.sleep(10)
