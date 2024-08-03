import streamlit as st
import random
import string

def generate_key(length=16):
    """Generate a random activation key."""
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def generate_keys(number_of_keys, key_length=16):
    """Generate a list of unique activation keys."""
    keys = set()
    while len(keys) < number_of_keys:
        keys.add(generate_key(key_length))
    return list(keys)

def main():
    st.title("Activation Key Generator")
    
    st.sidebar.header("Settings")
    num_keys = st.sidebar.number_input("How many activation keys would you like to generate?", min_value=1, max_value=1000, value=5)
    key_length = st.sidebar.slider("Length of each activation key:", min_value=8, max_value=32, value=16)
    
    if st.button("Generate Keys"):
        with st.spinner('Generating keys...'):
            keys = generate_keys(num_keys, key_length)
            st.success(f"Generated {num_keys} keys:")
            st.text("\n".join(keys))
    
if __name__ == "__main__":
    main()
