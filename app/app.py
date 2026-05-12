"""Minimal Streamlit app for the outfit matching assistant."""

try:
    import streamlit as st
except ImportError:
    st = None


def main() -> None:
    if st is None:
        print("Streamlit is not installed. Run `pip install -r requirements.txt` first.")
        return

    st.set_page_config(page_title="Outfit Matching Assistant", page_icon="👕")
    st.title("Outfit Matching Assistant")
    st.write("Upload an outfit image and get matching color recommendations.")


if __name__ == "__main__":
    main()
