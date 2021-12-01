import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spectramap",
    version="0.3.1.2",
    author="Juan-David Munoz-Bolanos",
    author_email="jmunozbolanos@gmail.com",
    description="Hyperspectral package for spectroscopists",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/darksiders123/spectramap",
    project_urls={
        "Bug Tracker": "https://github.com/darksiders123/spectramap",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
	"Intended Audience :: Science/Research",
	"Development Status :: 3 - Alpha",
	"Topic :: Software Development :: Bug Tracking"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=["scikit-learn", "pyspectra", "hdbscan", "scipy"],
)