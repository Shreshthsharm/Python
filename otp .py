import random

class OTPGenerator:
    def generate_otp(self):
        # Generate a random 6-digit OTP
        otp = random.randint(100000, 999999)
        return otp
otp_gen = OTPGenerator()
otp = otp_gen.generate_otp()
print("Your 6-digit OTP is:", otp)