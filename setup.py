from setuptools import setup, find_packages

setup(
    name="datapeek",
    version="0.2.0",  # bumped version since this is a feature upgrade
    author="DevinduDh",
    author_email="youremail@example.com",
    description="A quick glance at your DataFrame with beautiful terminal and notebook output.",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "tabulate",
        "rich"
    ],
    python_requires=">=3.7",
)
