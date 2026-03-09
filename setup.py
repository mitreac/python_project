from setuptools import setup

setup(
    name="python_prj",
    version="0.1.0",
    packages=["cm_pkg", "cm_pkg.ui"],
    entry_points={"console_scripts": ["greeting = cm_pkg.module1:say_hello"]},
)
