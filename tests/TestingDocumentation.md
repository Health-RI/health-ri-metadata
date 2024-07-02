# Documentation for the testing harness

## Introduction

This folder contains files related to a testing harness for the SHACL shapes. The main purpose of
these is to catch errors at an early stage in development, for example data that should validate
but fails to validate, or minor syntax errors that hadn't come up before. We do this by testing
the shapes against test data of which we know the expected test result.

## Running the tests

The tests are automatically run by Github actions on every pull request. However, you can also run
these locally. You will need to have [Hatch](https://www.python.org/) installed on your computer.
To install Hatch, follow the instructions at this link for your operating system: <https://hatch.pypa.io/latest/install/>

To run the tests, go to your commandline of choice and running `hatch run test`. You will get a test report then.

If any of the tests fail, the testing tool will show you which test failed and what the associated
error message was.

## Developing your own tests

> **Note:** This section is to be expanded

The testing is performed using [pySHACL](https://github.com/RDFLib/pySHACL) and [pytest](https://docs.pytest.org/).
Full documentation on these tools is currently outside of the scope of this document.
