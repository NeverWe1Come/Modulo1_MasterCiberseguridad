import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
from cryptography.hazmat.backends import default_backend

backend = default_backend()
key = os.urandom(24)

