from frontend.utils import make_hashes


class Config:
    app_name = "RAGnBeyond"
    sidebar_image_uri = "resources/sidebar.png"

    users = {
        "admin": make_hashes("123")
    }


config = Config()
