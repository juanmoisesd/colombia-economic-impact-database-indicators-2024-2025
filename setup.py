from setuptools import setup, find_packages
setup(
    name="colombia-economic-impact-database-indicators-2024-2025",
    version="1.0.0",
    description="Base de Datos del Impacto Económico de Colombia 2024-2025: Indicadores Clave y Factores Influyentes.",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/colombia-economic-impact-database-indicators-2024-2025",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="zenodo, open-data",
)