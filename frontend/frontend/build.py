import pynecone as pc

home_page = "http://localhost:3000/"

def build():
    return pc.vstack(
            pc.heading("Tour builder page", font_size="2em"),
            pc.link(
                "Home",
                href=home_page,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            )
    )