# datascience-python-template

This repository is a [cookiecutter](https://github.com/cookiecutter/cookiecutter) templates for
quick python project scaffolding.

## Requirements

Install `cookiecutter` with either of the following

* pip: `pip install cookiecutter`
* [homebrew](https://brew.sh):  `brew install cookiecutter`

## Features

This package template is set up to allow scientists/developers to be immediately productive writing python.
Here are some of the features the package format setups up automatically.

* ✅ **Automatically sets the python package version** from the git tag. If a git tag is not preset then the latest git commit hash is used.
* ✅ **Linting/formatting** are automatically setup using [`tox`](https://tox.wiki/en/latest/).
* ✅ Isolated builds with [`tox`](https://tox.wiki/en/latest/).
* ✅ **Debugging** with vscode.
* ✅ Example **unit tests**.
* ✅ Example **command line entry point**.
* ✅ Example **parameter config file** (which is loaded via a `--run-config` argument).
* ✅ [pre-commit](https://pre-commit.com) **git hooks**.

## Usage

You can read the templates directly from git without downloading them you do need to provide the `--directory`
argument to select the template. An example below,

```sh
cookiecutter git+ssh://git@github.com/andela-technology/ds-code-template --directory basic-template
```

## Example

Here we show the steps need to create an example package called `algo-cat-tracker`.

```sh

# generate your package from the template
cookiecutter git+ssh://git@github.com/andela-technology/ds-code-template --directory basic-template

# Answer questions:
    package_name: cat-tracker
    module_name: cat_tracker

# new directory will have generated code
cd cat_tracker

# Initialize the git repo, add files and commit
#❗ NOTE: You must do this step or the generated package won't build.
git init . && git add -A && git commit -am "Initial Commit"

# after you make a virtualenv install and build the package
pip install ".[dev]"

# run linting/formatting/tests
tox

# If everything succeed then you are good to go! Push your code to github.
```
