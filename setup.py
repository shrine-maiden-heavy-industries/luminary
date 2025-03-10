#!/usr/bin/env python3
# SPDX-License-Identifier: BSD-3-Clause

from setuptools import setup, find_packages
from pathlib    import Path

REPO_ROOT   = Path(__file__).parent
README_FILE = (REPO_ROOT / 'README.md')

def scm_version():
	def local_scheme(version):
		if version.tag and not version.distance:
			return version.format_with('')
		else:
			return version.format_choice('+{node}', '+{node}.dirty')
	return {
		'relative_to'   : __file__,
		'version_scheme': 'guess-next-dev',
		'local_scheme'  : local_scheme
	}

def doc_version():
	try:
		from setuptools_scm.git import parse as parse_git
	except ImportError:
		return ''

	git = parse_git('.')
	if not git:
		return ''
	elif git.exact:
		return git.format_with('v{tag}')
	else:
		return 'latest'

setup(
	name             = 'luminary-fpga',
	use_scm_version  = scm_version(),
	author           = ', '.join([
		'Aki Van Ness',
		'Rachel Mant',
	]),
	author_email     = ', '.join([
		'aki@lethalbit.net',
		'git@dragonmux.network',
	]),
	description      = 'Host tools for Luminary FPGA debug controllers',
	license          = 'BSD-3-Clause',
	python_requires  = '~=3.10',
	zip_safe         = True,
	url              = 'https://github.com/shrine-maiden-heavy-industries/luminary',

	long_description = README_FILE.read_text(),
	long_description_content_type = 'text/markdown',

	setup_requires   = [
		'wheel',
		'setuptools',
		'setuptools_scm'
	],

	install_requires = [
		'setuptools',
		'pyusb~=1.2.0',
		'pyvcd>=0.4.0,<0.5',
	],

	extras_require   = {
		'dev': [
			'nox'
		],
	},

	packages         = find_packages(
		where   = '.',
		exclude = (
			'tests',
			'tests.*',
			'contrib',
			'contrib.*',
			'firmware',
			'firmware.*',
		)
	),


	classifiers       = [
		'Development Status :: 4 - Beta',

		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: Science/Research',

		'License :: OSI Approved :: BSD License',

		'Operating System :: MacOS :: MacOS X',
		'Operating System :: Microsoft :: Windows',
		'Operating System :: POSIX :: Linux',

		'Programming Language :: Python :: 3.10',
		'Programming Language :: Python :: 3.11',
		'Programming Language :: Python :: 3.12',
		'Programming Language :: Python :: 3.13',

		'Topic :: Scientific/Engineering',
		'Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)',
		'Topic :: Software Development',
		'Topic :: Software Development :: Embedded Systems',
		'Topic :: Software Development :: Libraries',

	],

	project_urls     = {
		'Documentation': 'https://github.com/shrine-maiden-heavy-industries/luminary',
		'Source Code'  : 'https://github.com/shrine-maiden-heavy-industries/luminary',
		'Bug Tracker'  : 'https://github.com/shrine-maiden-heavy-industries/luminary/issues',
	},
)
