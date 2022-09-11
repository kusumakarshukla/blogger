from . import main

@main.errorhandler(404)
def page_not_found(e):
    return "Page Not Found",404

