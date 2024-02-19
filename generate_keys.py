### Generate keys

import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

names = ["Alvin Abhinav", "Martin Mahtab ","Richard Rachit"]
usernames = ["abhi", "mmartin","rrachit"]
passwords = ["password", "martin","1234"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent /"secret.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)