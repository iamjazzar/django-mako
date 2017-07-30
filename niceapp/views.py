from django.shortcuts import render, render_to_response


def function_based_view(request, engine):
    context = {
        'items': [
            'Wow',
            'This is awesome',
            'Don\'t forget to bring some bread honey ;)',
            'The requested template is: {}'.format(engine),
        ],
        'value': 1+1,
        'engine': engine,
    }

    if engine == 'mako':
        template_name = 'mako.html'
    else:
        template_name = 'django.html'

    return render_to_response(
        template_name=template_name,
        context=context,
        using=engine,
    )
