from passlib.context import CryptContext

# hashing algorithm setup
pwd_context = CryptContext(
    schemes=["bcrypt"], # Hashing algorithm specify karta hai.Bcrypt industry standard hai.
    deprecated="auto" # Agar future me algorithm change ho, to passlib automatically old hashes handle kar sakta hai.
)

#Hash Password
def hash_password(password: str):
    return pwd_context.hash(password)

#Verify Password
def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password, hashed_password
    )