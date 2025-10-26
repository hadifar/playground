import streamlit as st

from config import config

footer = """<style>
a:link , a:visited{
color: blue;
text-decoration: none;
background-color: transparent;
}

a:hover,  a:active {
background-color: transparent;
}

.footer {
position: fixed;
bottom: 0;
color: black;
text-align: center;
font-size: smaller;
opacity: 0.9;
}
</style>
<div class="footer">
    <p>Developed with ❤️ by <a href="https://hadifar.github.io/" target="_blank">Amir</a></p>
</div>
"""
def sidebar_page():
    st.sidebar.image(config.sidebar_image_uri)
    st.sidebar.markdown(footer, unsafe_allow_html=True)
