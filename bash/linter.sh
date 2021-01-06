#!/bin/bash -e

{
	black --version | grep -E "20.8b1" > /dev/null
} || {
	echo "Linter requires 'black==20.8b1' !"
	exit 1
}

ISORT_VERSION=$(isort --version-number)

set -v

echo "Running isort ..."
isort -y -sp . --atomic

echo "Running black ..."
black -l 100 .

echo "Running flake8 ..."
if [ -x "$(command -v flake8-3)" ]; then
	flake8-3 .
else
	python3 -m flake8 .
fi
