import os

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


# setup(
#     name='talentfabric-core',
#     version='0.4.0',
#     license='MIT',
#     author="Ariel Zadok",
#     author_email='ariel.z@goperfectmatch.com',
#     packages=find_packages('src'),
#     package_dir={'': 'src'},
#     url='https://github.com/TalentFabric/talentfabric-python-commons/talentfabric_core',
#     keywords='talent id generator',
#     install_requires=[
#         'country-converter==0.7.4'
#     ],
#
# )
