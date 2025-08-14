from setuptools import setup, find_packages

setup(
    name="datapeek",
    version="0.1.0",
    author="Your Name",
    author_email="youremail@example.com",
    description="A quick glance at your DataFrame.",
    packages=find_packages(),
    install_requires=["pandas", "tabulate"],
    python_requires=">=3.7",
)
