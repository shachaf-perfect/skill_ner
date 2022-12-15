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
    author_email="Badr.MOUFAD@emines.um6p.ma",
    description="An NLP module to automatically Extract skills and certifications from unstructured job postings, "
                "texts, and applicant's resumes",
    url="https://github.com/shachaf-perfect/skill_ner.git",
    keywords=["skillner", 'python', 'NLP', "NER", "skills-extraction", "job-description"],
    # download_url='https://github.com/AnasAito/SkillNER/archive/refs/tags/v1.0.3.tar.gz',
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: MIT License',
        "Operating System :: OS Independent",
    ],
)
