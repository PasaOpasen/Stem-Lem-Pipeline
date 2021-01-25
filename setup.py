
import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()


setuptools.setup(
    name="StemLemPipe", 
    version="0.1.3",
    author="Demetry Pascal",
    author_email="qtckpuhdsa@gmail.com",
    maintainer = ['Demetry Pascal'],
    description="simple text transformer used several stemming and lemmatization backends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PasaOpasen/Stem-Lem-Pipeline",
    keywords=['text','nlp','nltk', 'ngrams','transformation', 'words', 'stemming', 'lemmatization'],
    packages = setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=['nltk','pymorphy2','pymystem3','stop_words']
    
    )





