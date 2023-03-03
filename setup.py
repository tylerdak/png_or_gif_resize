from setuptools import setup, find_packages

setup(
    name="resize_image",
    version="0.1",
    # Author details
    author="Tyler Dakin",
    author_email="tyler@dakin.one",
    packages=find_packages("."),
    package_dir={"": "."},
    setup_requires=["Pillow==9.4.0"]
)