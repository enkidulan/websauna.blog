"""This contains app entry point for running a demo site for this addon or running functional tests for this addon."""

import websauna.system


class Initializer(websauna.system.DemoInitializer):
    """A demo / test app initializer for testing addon websauna.blog."""

    def include_addons(self):
        """Include this addon in the configuration."""
        self.config.include("websauna.blog")


def main(global_config, **settings):
    init = Initializer(global_config)
    init.run()
    return init.make_wsgi_app()
