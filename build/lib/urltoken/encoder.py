import os
import hashlib
import string


class UrlTokenEncoder:

    URL_TOKEN_SECRET = os.getenv('URL_TOKEN_SECRET')
    BASE62 = string.ascii_uppercase + string.ascii_lowercase + string.digits

    def __init__(self, secret: str = URL_TOKEN_SECRET):
        self.secret = secret

    @staticmethod
    def base62_encode(num, alphabet=BASE62):
        """Encode a number in Base X

        `num`: The number to encode
        `alphabet`: The alphabet to use for encoding
        """
        if num == 0:
            return alphabet[0]
        arr = []
        base = len(alphabet)
        while num:
            num, rem = divmod(num, base)
            arr.append(alphabet[rem])
        arr.reverse()
        return ''.join(arr)

    @staticmethod
    def base62_decode(token, alphabet=BASE62):
        """Decode a Base X encoded string into the number

        `string`: The encoded string
        `alphabet`: The alphabet to use for encoding
        """
        base = len(alphabet)
        strlen = len(token)
        num = 0

        idx = 0
        for char in token:
            power = (strlen - (idx + 1))
            num += alphabet.index(char) * (base ** power)
            idx += 1

        return num

    @staticmethod
    def token_to_num(token):
        return int.from_bytes(token.encode(), 'little')

    @staticmethod
    def num_to_token(num):
        return num.to_bytes((num.bit_length() + 7) // 8, 'little').decode()

    def encode(self, data: str) -> str:
        """
        Encodes a dictionary into a URL-safe token.

        :param data: The dictionary to encode.

        """
        token = self.base62_encode(self.token_to_num(data))
        if self.secret:
            token += '.' + hashlib.sha256(f'{data}{self.secret}'.encode()).hexdigest()

        return token

    def decode(self, token: str) -> str:
        """
        Decodes a URL-safe token into a dictionary.

        :param token: The token to decode.
        """
        data = self.num_to_token(self.base62_decode(token.split('.')[0]))
        if self.secret:
            if len(token.split('.')) != 2:
                raise ValueError('Invalid token, this token is not encoded with a secret.')

            token_hash = token.split('.')[1]
            if token_hash != hashlib.sha256(f'{data}{self.secret}'.encode()).hexdigest():
                raise ValueError('Invalid token, the token hash does not match the secret.')

        return data
