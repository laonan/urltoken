import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urltoken",
    version="1.0.0",
    author="Laonan",
    author_email="hello@laonan.net",
    description="Simplifies encoding sensitive data like emails URL-safe tokens.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/laonan/urltoken",  # github url
    project_urls={
        "Bug Tracker": "https://github.com/laonan/urltoken/issues",
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    zip_safe=True,
    python_requires=">=3.6",
)
