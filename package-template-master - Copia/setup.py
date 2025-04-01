from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_imagens_com_python",
    version="0.0.1",
    author="Osny",
    author_email="osnynt@gmail.com",
    description="Processamento de imagens com Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="my_github_repository_project_link",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)