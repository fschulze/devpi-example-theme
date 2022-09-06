from pluggy import HookimplMarker
from pyramid.events import subscriber
from pyramid.events import BeforeRender
import importlib.resources


devpiserver_hookimpl = HookimplMarker("devpiserver")


@devpiserver_hookimpl
def devpiserver_cmdline_run(xom):
    # this is slightly hacky, because accessing the command line args like that
    # is not part of the official API, but this is just for convenience
    if xom.config.args.theme is None:
        xom.config.args.theme = importlib.resources.path(
            'devpi_example_theme', 'theme')
    else:
        xom.log.error("You are trying to set a theme, but devpi-example-theme is installed.")
        return 1


@devpiserver_hookimpl
def devpiserver_pyramid_configure(config, pyramid_config):
    # we use a subdirectory in the serverdir to store the diagrams
    pyramid_config.registry['inheritance_diagram_path'] = config.serverdir.join('.diagrams')
    # by using include, the package name doesn't need to be set explicitly
    # for registrations of static views etc
    # see ``includeme`` for actual configuration
    pyramid_config.include('devpi_example_theme')


# example for a request method
def generated_at(request):
    from devpi_web.views import format_timestamp
    import time
    return format_timestamp(time.time())


# example for a BeforeRender handler
@subscriber(BeforeRender)
def add_global(event):
    routename = event['request'].matched_route.name
    if routename == 'root':
        users = event.rendering_val['users']
        # here you can do anything to the user list, like reordering
        # as an example we change the title of the user
        for user in users:
            user['title'] = 'User: %s' % user['title']
    return


def includeme(config):
    config.add_route(
        "inheritance_diagram",
        "/{user}/{index}/+inheritance_diagram")
    config.add_route(
        "orgchart",
        "/+orgchart")
    config.add_request_method(generated_at, reify=True)
    config.scan()
