from setuptools import setup, find_packages

setup(
    name='problemas_opt',  # Nombre del paquete (puedes elegir uno único)
    version='0.0.1',      # Versión inicial
    packages=find_packages(), # Busca subdirectorios con __init__.py
    py_modules=['problemas'], # ¡Importante! Especifica que 'problemas.py' es un módulo
    install_requires=[
        'numpy',
    ],
    author='Diana Sanjuan', # Tu nombre
    description='Clases de problemas de optimización para DE con restricciones',
    long_description=open('README.md').read() if 'README.md' else '', # Opcional: descripción larga desde README
    long_description_content_type='text/markdown',
    url='https://github.com/dianasanjuan0017/problemas', # Tu URL de GitHub
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)