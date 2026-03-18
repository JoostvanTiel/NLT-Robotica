import datetime


def _set_copyright(app, config):
    config.copyright = str(datetime.datetime.now().year)


def setup(app):
    app.connect("config-inited", _set_copyright)
    return {"version": "1.0", "parallel_read_safe": True}
