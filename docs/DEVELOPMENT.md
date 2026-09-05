# Biscuit Development Plan

- [x] Completed
- [~] In progress
- [ ] Planned

## Core Functionality

### Hashing
- [ ] Salt support
- [ ] Additional hash algorithms
- [ ] Hash format detection
- [ ] Hash input validation

Supported algorithms:
- md5
- sha1
- sha256
- sha384
- sha512

### Hash generation
- CLI
  - [x] Argument parser
  - [x] Argument validation
  - [x] Custom help message
- Generation
  - [x] Hash generation
  - [ ] Salt generation
  - [ ] Salted hash generation

### Dictionary attack
- CLI
  - [x] Argument parser
  - [x] Argument validation
  - [x] Custom help message
- Wordlist
  - [x] Built-in wordlists
  - [x] Custom wordlists
  - [x] Wordlist path handling
  - [ ] Wordlist management
  - [ ] Multiple wordlist support
  - [ ] Wordlist validation
  - [ ] Transformations and mutations
- Attack execution
  - [x] Parameters and progress display
  - [x] Hash generation
  - [ ] Salted hash support
  - [x] Hash comparison
  - [x] Result handling
  - [ ] Parallelism
  - [ ] Benchmarking

### Brute-force attack
- CLI
  - [x] Argument parser
  - [x] Argument validation
  - [x] Custom help message
- Candidate generation
  - [x] Custom keyspaces (character set and length)
- Attack execution
  - [x] Parameters and progress display
  - [x] Candidate and hash generation
  - [ ] Salted hash support
  - [x] Hash comparison
  - [x] Result handling
  - [~] Parallelism
  - [~] Benchmarking

### Mask attack
- [ ]

### Hybrid attack
- [ ]

## Performance

- [~] Optimize multiprocessing and task scheduling
- [ ] Benchmark and tune chunking
- [~] Reduce memory and IPC overhead
- [ ] GPU acceleration

## Attack Management

- [ ] Graceful interruption and cancellation
- [ ] Resume interrupted attacks
- [ ] Checkpointing
- [ ] Save/load attack configurations

## Configuration

- [x] Configuration file
- [ ] Configurable defaults
- [ ] Attack profiles
- [ ] Configuration validation

## CLI & Output

- [ ] Improve progress display
- [ ] Improve help and error messages
- [ ] Quiet/verbose modes
- [ ] Structured output
- [ ] Attack summaries and performance statistics

## Reliability

- [ ] Unit and integration tests
- [ ] Edge-case handling
- [ ] Error handling
- [ ] Regression testing

## Platform Support

- [ ] Windows support
- [ ] macOS support

## Packaging & Documentation

- [ ] Packaging and distribution
- [x] Installable CLI
- [ ] Complete README and documentation
- [ ] Release workflow

## Future / Experimental

- [ ] Advanced mutation/rule-based attacks
- [ ] Distributed execution
- [ ] Plugin/extensibility system
- [ ] Advanced profiling and attack analytics
- [ ] Interactive CLI mode