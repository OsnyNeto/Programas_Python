from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="osny_imagem_processing",
    version="0.0.2",
    author="Osny",
    author_email="osnynt@gmail.com",
    description="Processamento de imagens com Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/OsnyNeto/Programas_Python/tree/main/osny_imagem_processing",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)