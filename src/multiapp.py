import streamlit as st

class MultiApp:
    """
    A class to manage multiple Streamlit applications in a single interface.
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """
        Add a new application.

        Parameters:
        - title: str, title of the application.
        - func: callable, the function that renders the application.
        """
        self.apps.append({"title": title, "function": func})

    def run(self):
        """
        Render the app menu and execute the selected application.
        """
        st.sidebar.title("Navigasi")
        app = st.sidebar.radio(
            "Pilih Halaman:", self.apps, format_func=lambda app: app["title"]
        )
        app["function"]()
