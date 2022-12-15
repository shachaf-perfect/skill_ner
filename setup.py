import setuptools


dependencies = [
    "numpy",
    "pandas",
    "nltk",
    "spacy",
    "jellyfish",
    "ipython"
]

setuptools.setup(
    name="skillner",
    version="0.0.1",
    author="Anas Ait AOMAR & Badr MOUFAD (Adapted by Shachaf Poran)",
    author_email="shachaf.p@goperfectmatch.com",
    packages=setuptools.find_packages('.'),
    package_dir={'': '.'},
    url="https://github.com/shachaf-perfect/skill_ner.git",
    keywords=["skillner", 'python', 'NLP', "NER", "skills-extraction", "job-description"],
    install_requires=dependencies,
)
