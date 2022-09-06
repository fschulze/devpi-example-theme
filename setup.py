from setuptools import setup


setup(
    name="devpi-example-theme",
    description="devpi-example-theme: an example theme with plugins for devpi-web",
    url="https://github.com/fschulze/devpi-example-theme",
    version='1.1',
    maintainer="Florian Schulze",
    maintainer_email="florian.schulze@gmx.net",
    license="MIT",
    entry_points={
        'devpi_server': [
            "devpi-example-theme = devpi_example_theme"]},
    install_requires=[
        'devpi-web'],
    include_package_data=True,
    python_requires='>=3.7',
    zip_safe=False,
    packages=['devpi_example_theme'])
