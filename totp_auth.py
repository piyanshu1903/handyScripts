#server-end
import hashlib
import pyotp
import qrcode
    

secret=pyotp.random_base32()
provisioning_uri = pyotp.totp.TOTP(secret).provisioning_uri(name='Piyanshu TOTP', issuer_name='PM.co')
img = qrcode.make(provisioning_uri)
img.save("./totp_qr.png") # It contains uri for authenticator apps


totp = pyotp.TOTP(secret)
print("Current OTP:", totp.now()) #Server end otp generation for a client
totp.now() #stores current otp
totp.verify(803283)   # verifies clients otp


#TOTP structure
'''
class TOTP(
    s: str,
    digits: int = 6,
    digest: Any = None,
    name: str | None = None,
    issuer: str | None = None,
    interval: int = 30
)
'''



