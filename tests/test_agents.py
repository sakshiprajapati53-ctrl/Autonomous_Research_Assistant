from auth.password_utils import hash_password
from auth.password_utils import verify_password

hashed = hash_password("abc123")
print(hashed)

verify_password(
    "abc123",
    hashed
)

verify_password(
    "wrong",
    hashed
)