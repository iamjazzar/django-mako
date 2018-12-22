from django.shortcuts import render_to_response, render
from django.views.generic import TemplateView


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

    return render(
        template_name=template_name,
        context=context,
        request=request,
        using=engine,
    )


class ClassBasedView(TemplateView):
    def get_template_names(self):
        engine = self.kwargs['engine']
        if engine == 'mako':
            self.template_engine = 'mako'
            return 'mako.html'

        return 'django.html'

    def get_context_data(self, **kwargs):
        context = super(ClassBasedView, self).get_context_data(**kwargs)
        engine = kwargs['engine']
        context.update({
            'items': [
                'Wow',
                'This is awesome',
                'Don\'t forget to bring some bread honey ;)',
                'The requested template is: {}'.format(engine),
            ],
            'value': 1+1,
            'engine': engine,
        })

        return context
