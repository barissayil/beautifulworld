from setuptools import setup, find_packages

with open('README.md') as readme_file:
	README = readme_file.read()

setup_args = dict(
	name='beautifulworld',
	version='0.0.3',
	description='Package for visualizing data about cities',
	long_description_content_type="text/markdown",
	long_description=README,
	license='MIT',
	packages=find_packages(),
	author='Baris Sayil',
	author_email='barissayil@protonmail.com',
	keywords=['World', 'Cities'],
	url='https://github.com/barissayil/beautifulworld',
	download_url='https://pypi.org/project/beautifulworld/'
)

install_requires = [
	'pandas',
	'requests',
	'bs4',
	'seaborn',
	'numpy',
]

if __name__ == '__main__':
	setup(**setup_args, install_requires=install_requires)