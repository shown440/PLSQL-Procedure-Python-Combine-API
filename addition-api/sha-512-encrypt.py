import hashlib
# def encrypt_string(hash_string):
#     sha_signature = \
#         hashlib.sha256(hash_string.encode()).hexdigest()
#     return sha_signature 

# a = "c7c4740b79e1478e3d426c0dd4f9fdbd4e3f08d43f7a3efe79274e7eb35f838dfe082610420db97811bbe9b91ffb9fbc7cd7bb67d0ec3d39abaebb05bcd82b47"
hash_string = "xbhfjsdhfklsdfhsdlfhsdlfhsdlifhslifhlifglifgelighelgerligherligerligerlgergierg"
sha_signature = hashlib.sha512(hash_string.encode()).hexdigest()
print(len(sha_signature))
print(sha_signature)
