# Biscuit

**Biscuit** is an offline password hash auditing and recovery CLI tool written in Python.

![Biscuit Demo](assets/demo.gif)

## Status

Biscuit is currently **WIP**.

| Feature             | Status      |
| ------------------- | ----------- |
| Hash generation     | Implemented |
| Dictionary attack   | Implemented |
| Brute-force attack  | Implemented |
| Mask attack         | Planned     |
| Hybrid attack       | Planned     |
|                     |             |
| Parallelism         | WIP         |
| Mutations           | Planned     |
| Salt support        | Planned     |
|                     |             |
| Linux support       | Implemented |
| Windows support     | Planned     |
| macOS support       | Planned     |

*Currently supports only Linux.*

## Supported Algorithms

Currently supported:
- MD5
- SHA-1
- SHA-256
- SHA-384
- SHA-512

## Character sets

The tool uses ASCII character sets by default.

Currently supported:
- lowercase
- uppercase
- digits
- letters
- alphanumeric
- special
- all

## Installation

Clone the repository and install Biscuit with pip:

```
git clone https://github.com/vel4tus/biscuit-password-auditing.git
cd biscuit-password-auditing
pip install -e .
```

After installation:

```
biscuit --help
```

## Usage

Get general help:

```
biscuit --help
```

Get help for a specific mode:

```
biscuit dictionary --help
biscuit brute-force --help
biscuit hash-gen --help
```

## Authorized use only

Biscuit is intended for **authorized security auditing, password recovery, and educational purposes only**.

Do not use it against systems, accounts, or password hashes without explicit authorization.
