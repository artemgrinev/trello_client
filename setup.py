import setuptools
  
with open("README.md", "r") as fh:  
 long_description = fh.read()  
setuptools.setup(  
 name="trello_client-basics-api-artemgrinev", version="0.0.1", author="Artem Grinev", author_email="artemgrinev@gmail.com", description="client for trello", long_description=long_description, long_description_content_type="text/markdown", url="https://github.com/artemgrinev/trello_console_client", packages=setuptools.find_packages(), classifiers=[ "Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent", ], python_requires='>=3.6',)