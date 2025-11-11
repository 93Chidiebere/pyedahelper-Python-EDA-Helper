# from setuptools import setup, find_packages

# setup(
#     name='pyedahelper',
#     version='0.1.0',
#     packages=find_packages(),
#     install_requires=[
#         'pandas',
#         'numpy',
#         'matplotlib',
#         'seaborn'
#     ],
# )

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pyedahelper",
    version="1.0.3",
    author="Chidiebere V. Christopher",
    author_email="vchidiebere.vc@gmail.com",
    description="An interactive cheat sheet, AI-powered guide for exploratory data analysis (EDA), and tools for data visualization, cleaning and feature engineering.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
    python_requires=">=3.7",
)