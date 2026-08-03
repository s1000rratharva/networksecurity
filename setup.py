from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """
    This function will return the list of requirements
    """
    requirements_lst: List[str] = []
    try:
        with open("requirements.txt") as file:
            lines=file.readlines()

            for line in lines:
                requirements=line.strip()
                if requirements and requirements!='-e .':
                    requirements_lst.append(requirements)

    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements_lst

print(get_requirements())

setup(
    name="NetworkSecurity",
    version="0.0.1",
    author="Atharva Keluskar",
    author_email="keluskaratharva999@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)