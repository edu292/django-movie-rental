from django.conf import settings

def htmx_base_template(request):
    """
    Sets the base_template path from settings based on the request type.
    """
    if request.htmx:
        # Get the HTMX base template path from settings
        path = getattr(settings, "HTMX_BASE_TEMPLATE", "_partial.html")
    else:
        # Get the standard base template path from settings
        path = getattr(settings, "BASE_TEMPLATE", "_base.html")

    return {'base_template': path}