from setuptools import setup, find_packages
setup(
    name="formify",
    version="1.0.4",
    packages=find_packages(),
	package_data={
        "": ["*.css"],
    },
	install_requires=["pyside2", "matplotlib"]
)