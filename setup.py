from pip.req import parse_requirements
import setuptools


# Filters out relative/local requirements (i.e. ../lib/utils)
remote_requirements = '\n'.join(str(r.req) for r in parse_requirements("requirements.txt", session='dummy') if r.req)

setuptools.setup(
    name='jenkins-test',
    version='0.0.1',

    author='Max Zheng',
    author_email='maxzheng.os @t gmail.com',

    description='Test project for Jenkins',
    long_description=open('README.md').read(),

    url='https://github.com/maxzheng/jenkins-test',

    install_requires=remote_requirements,

    license='MIT',

    packages=setuptools.find_packages(),
    include_package_data=True,

    setup_requires=['setuptools-git'],

    # entry_points={
    #    'console_scripts': [
    #        'script_name = package.module:entry_callable',
    #    ],
    # },

    classifiers=[
      'Development Status :: 5 - Production/Stable',

      'Intended Audience :: Developers',
      'Topic :: Software Development :: Testing',

      'License :: OSI Approved :: MIT License',

      'Programming Language :: Python :: 3',
      'Programming Language :: Python :: 3.6',
    ],

    keywords='<KEYWORDS>',
)