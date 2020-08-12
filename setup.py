import setuptools

with open('./requirements.in') as f:
    install_requires = [l for l in f.readlines() if l and not l.startswith('#')]

if __name__ == '__main__':
    setuptools.setup(
        name='lepo',
        version='0.2.0',
        url='https://github.com/akx/lepo',
        author='Aarni Koskela',
        author_email='akx@iki.fi',
        maintainer='Aarni Koskela',
        maintainer_email='akx@iki.fi',
        license='MIT',
        install_requires=install_requires,
        packages=setuptools.find_packages('.', exclude=(
            'lepo_tests',
            'lepo_tests.*',
        )),
        include_package_data=True,
    )
