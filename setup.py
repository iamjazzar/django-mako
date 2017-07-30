from distutils.core import setup

setup(
    name='django-mako',
    version='1.0.0',
    packages=['djangomako'],
    install_requires=['Django==1.11.3', 'Mako==1.0.7'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Django Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    url='https://github.com/ahmedaljazzar/django-mako',
    license='MIT License',
    author='Ahmed Jazzar',
    author_email='me@ahmedjazzar.com',
    description='The simple, elegant Django Mako library',
)
