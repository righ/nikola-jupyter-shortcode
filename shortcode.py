# -*- coding: utf-8 -*-
import pathlib
import lxml.html

try:
    from traitlets.config import Config
except ImportError:
    from IPython.config import Config

try:
    from nbconvert.exporters import HTMLExporter
except ImportError:
    from IPython.nbconvert.exporters import HTMLExporter

from nikola.plugin_categories import ShortcodePlugin


class JupyterShortcodePlugin(ShortcodePlugin):
    """ Jupyter notebook shortcode. """
    name = "jupyter_shortcode"

    def set_site(self, site):
        super(JupyterShortcodePlugin, self).set_site(site)
        self.site.register_shortcode('jupyter', self.handler)

    def handler(self, filename, site=None, data=None, lang=None, post=None):
        c = Config(self.site.config['IPYNB_CONFIG'])
        export_html = HTMLExporter(config=c)
        path = str(pathlib.Path(post.source_path).parent / filename)
        (notebook_raw, _) = export_html.from_filename(path)

        # The raw HTML contains garbage (scripts and styles). Extract only div id=notebook-container and children
        notebook_html = lxml.html.fromstring(notebook_raw)
        notebook_code = lxml.html.tostring(notebook_html.xpath('//*[@id="notebook-container"]')[0], encoding='unicode')

        return notebook_code, [path]
