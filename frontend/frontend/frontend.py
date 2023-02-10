"""Welcome to Pynecone! This file outlines the steps to create a basic app."""

import pynecone as pc

from pcconfig import config
from .build import build


docs_url = "http://localhost:3000/build/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""

    pass


def index():
    return pc.center(
        pc.vstack(

            pc.heading("Welcome to Tour Constructor!", font_size="2em"),
            pc.link(
                "Try to build!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="10%",
    )

def buildpage():
     return build() 

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.add_page(build, route="/build")
app.compile()
