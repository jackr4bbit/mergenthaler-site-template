from mergenthaler import Site, Feed
from colour import Color
from jinja2 import Environment, ChoiceLoader, PackageLoader

class TravisSite(Site):
    name = "Travis Site"
    colors = Site.colors | {"accent": Color("#007543")}

    def __init__(self, feed: Feed):
        super().__init__(feed)
        loader = ChoiceLoader([
            PackageLoader("mg_travis_site", "site"),
            self.jinjaEnv.loader
        ])
        self.jinjaEnv = Environment(loader=loader)