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

def gen_data_files(*dirs):
    results = []

    for src_dir in dirs:
        for root,dirs,files in os.walk(src_dir):
            results.append((root, map(lambda f:root + "/" + f, files)))
    return results


setuptools.setup(
    name="skillner",
    version="0.0.1",
    author="Anas Ait AOMAR & Badr MOUFAD (Adapted by Shachaf Poran)",
    author_email="Badr.MOUFAD@emines.um6p.ma",
    description="An NLP module to automatically Extract skills and certifications from unstructured job postings, "
                "texts, and applicant's resumes",
    url="https://github.com/shachaf-perfect/skill_ner.git",
    keywords=["skillner", 'python', 'NLP', "NER", "skills-extraction", "job-description"],
    # download_url='https://github.com/AnasAito/SkillNER/archive/refs/tags/v1.0.3.tar.gz',
    packages=setuptools.find_packages(),
    include_package_data=True,
    data_files=gen_data_files('.'),
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
