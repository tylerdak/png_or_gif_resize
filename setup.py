from setuptools import setup, find_packages

setup(
    name="resizeImage",
    version="0.1",
    # Author details
    author="Tyler Dakin",
    author_email="tyler@dakin.one",
    packages=find_packages("src"),
    package_dir={"": "src"},
    setup_requires=["Pillow==9.4.0"]
)