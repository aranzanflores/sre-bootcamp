# These functions need to be implemented
import mysql.connector
import json
import jwt
import hashlib

hmac_secret = 'my2w7wjd7yXF64FIADfJxNs1oupTGAuW'
algorithm = 'HS256'

class DataBaseAccess():
    user = 'secret'
    password = 'noPow3r'
    host = 'bootcamp-tht.sre.wize.mx'
    name = 'bootcamp_tht'

class Token:

    database_access = DataBaseAccess()
    payload_data = {
                       "role": ""
                    }

    def generate_token(self, username, password):
        cxn = mysql.connector.connect(user=self.database_access.user,
                                      password=self.database_access.password,
                                      host=self.database_access.host,
                                      database=self.database_access.name)
        cursor = cxn.cursor()
        query = ("SELECT * FROM users WHERE username=%s")
        cursor.execute(query, (username,))
        result = cursor.fetchall() #TOO: assert that result contains only one tuple
        print(result)
        # Extract data from users table
        encrypted_password = result[0][1]
        salt = result[0][2]
        role = result[0][3]
        cursor.close()
        cxn.close()
        salted_password = password + salt
        hashed_password = hashlib.sha512(salted_password.encode()).hexdigest()
        self.payload_data["role"] = role
        if (hashed_password == encrypted_password):
            token = jwt.encode(payload = self.payload_data, key = hmac_secret, algorithm = algorithm)
            return token
        else:
            return "Authentication error"

class Restricted:

    expected_payload_data = {
                                'role' : 'admin'
                            }
    protected_data_string = "You are under protected data"

    def access_data(self, authorization):
        payload_data = jwt.decode(authorization, key = hmac_secret, algorithms = algorithm)
        if (self.expected_payload_data == payload_data):
            return self.protected_data_string
        else:
            return "Authorization error"
