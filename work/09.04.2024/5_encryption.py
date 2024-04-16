from pathlib import Path
from pickle import load

import openssh_key.private_key_list  as pkl
import cryptography.hazmat.primitives.asymmetric.rsa as rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


#home = Path.home()

#pk_sk_pair = pkl.PrivateKeyList.from_string(open(home / '.ssh' / 'id_rsa').read())
#pk_sk_pair.priv

#sk_list = pkl.PrivateKeyList.from_list([pk_sk_pair], cipher='aes256-ctr', kdf='bcrypt')
#privat_key = sk_list.convert_to(rsa.RSAPrivateKey)
#public_key = sk_list.convert_to(rsa.RSAPublicKey)

with open('pair.pkl','rb') as f:
    pk_sk_pair = load(f)

private_key = pk_sk_pair.private.params.convert_to(rsa.RSAPrivateKey)
#print(pk_sk_pair.public.pack_public_string())

correspondent_pubkey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCc7uazELA5g4ee+jgkkpgIETKjoxLr6miedU0NXmfIOK2owgnPZwAG2Is8DRPodw9qZI6GkuynkNTlVE46f6MLie+WgwjEXiOWFKcKHoO0cQGmMLHi+YJNKKXZU2Y+NVZCIihoanwy5TKQBT7zynyRZvDz8V6xDguw8lXkQ/Q+XOiLC2x+aaOm5JhbDcQN4PIUTkgf0izInxqRfyG/kqM5VvAgMiKQA608B51mPrBOOZM/d51OMNnEkrgDqWym2GzODQbu1ucFVY8/ZZAODdqpgje3QWKwrhX0Pqw4Akx7aozLBaFJQRi57LkbQL2kuhw7UkOf4IEz+T+Ft5bHi4gnilQX3L4Bda5becdKaqiB0LWN0Sje/+JUexnq4AosX5530uWwvYKKiXij7RT0zL8z2+XFR3dLhwhp++mBePmFA+7mgYuAhexEDOTBHQyqbcFdp18d7X5w0I69OYjNfqBnYWK9INuaqU91g5nLBY1X5M7LWWqZ3sBUE9vOxtabOl9AURMxEJ+O8Rs/q/4ZzIjgFkM64gT049+sx6ZxQ0V89y/QQ8EaMbmeyisLlOzAf6PvruErcGQ30s35e2COwVyWQ42SthYO4oh0FnEQA4uzBmthzI/QO9prVpJFxMjeQ9ib2KmhfpSQgvK4WKw0JvDaYyZks9kzb+yX2ITGhpsSXw=="
public_key = pkl.PublicKey.from_string(correspondent_pubkey).params.convert_to(rsa.RSAPublicKey)

message = b"Hello, "

ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
#print(ciphertext)

messege_encrypted = b'\r\xaa\xca\xa5\xe2\x0f\x94\xff\xb40no^\x04q"\xdc-t\x82\xa0\x96t\xd4>\x16#\x94jET\xf3x\xac{X\x82\xc6\x98\xef\xe8-a\x1fW\xb5:\xd9\xe36\x9d#\x14ZSPV\xf0\xde\xe3m\x99\xd1\x8cyC]!Z\xa4HW[\xe5Er-\xdeP\x9e"w\xe3\xc7\xed\xe2>\xb6\x84\xaa\xeb\x89\xa6\x99-\nt\x1e\r\xd5K\x946kUY\xc2\x89\x84\x01\xd5N\xdc\x03\x8bg\x9b\xcb=GG*\x1ckR\xd4\x9f\xa72\x1f\xc3\xc4\x97\x1f\xc2\xab!R\x94\x84\x9f\x11\x84.\xf7\x9e\xcf<\x05pXw\xcbc\x8a\x0bt\xea&\xd0\x12\xdd\xf4\xa3\xab\x162\xb5\x18\xb7\xe3\xb4\xe77\xf8I%\r\xed/\xe0;\xc5\xe8e\xc0\xc8\xbc\xb7\x89k\x7f"\xfb\x05\x1b9>\xa3\xcf;\xa3\xbd\xf4\x85\x91\xf6\xe7\'\\\xe48=4z\x9fPN{\xae\xd5I\x8fv&!U+\xfe\xb6K\xa1<"\xcd\xf5\x9c\xdae\xac0\xf7\xfa\x91 \xd8(-\xef\xd6\x99\x1f\x98\xf6xn\xcaN\x8c\xbe=G%\xc8\x14\xb0k\xab\xec\x94WjN \x9c]\x80A\xc6\x16\n\xc7\x85w@\x10F\xa8\x8fr\xc8\xcfG2U\x99\xab\xb1\x18x9$\x88Q\xd3N+{\xaa\x9bf\x0cQ\xdex\xa7\xc8\xbb\xa8|\xa2#\x8a\xde\x92RHF\xa5L\x18\xf0\x1eQ+\xeb7\xa9\x97\x87\xb0p\xfbm\x9cR\x9ed\x9a\'ij\xb2\xfb\xae\x06x\xca\x7fBH\x89\xcf\x10\x17\x8c\x80\xe98\x07\x886.s\xd2[\xc7\xb0F?\xbd\xf0\xa0\x9cK\xf4Q0g\x05\xa2\x8e\x81\xe5\xc9?\xa1\x10\x98\xa8\xc0\x1fR\x93\x875\nZ<f\x87\x17f\xce\xd4"zp\xda-\x16\xf3\xb5N\xa4\x90Sy\x92^\x98Vul"^\xff/B\xa7\x16)\xa4\xe3\x91\x81\rV7M\x1c_\xbe\xac\x03\x91\x97m\x08{z\x9e\xe1G\xddJZ\xd0\x14SY\xb5\xd0b\xa2\xc2\xa4\x87~9H\xb0\xb8E\x88\xbf\xa8\x1d\xd4a\xef\xa2~H\xbc\xc1\x84\xe8\x1fCp\xa3\xb7Dj\xb6m\xe5\xaa\t\xa6\xc0'

print(private_key.decrypt(
    messege_encrypted,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
))
