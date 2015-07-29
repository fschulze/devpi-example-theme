from devpi_web.views import ContextWrapper
from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import FileResponse
from pyramid.view import view_config
import hashlib


@view_config(
    route_name="inheritance_diagram",
    request_method="GET")
def inheritance_diagram(context, request):
    """ Serves the raw documentation files. """
    context = ContextWrapper(context)
    stage_key = ','.join(x.name for x in context.stage._sro())
    stage_key = hashlib.md5(stage_key.encode('utf-8')).hexdigest()
    filename = '%s-%s.svg' % (context.stage.name, stage_key)
    path = request.registry['inheritance_diagram_path'].join(filename)
    if not path.exists():
        # generate the file here and return not found only on error
        error = True
        if error:
            raise HTTPNotFound("Path %s not found" % path)
    return FileResponse(path)


@view_config(
    route_name="orgchart",
    request_method="GET",
    renderer="templates/orgchart.pt")
def orgchart(context, request):
    """ Serves the raw documentation files. """
    context = ContextWrapper(context)
    return dict()
