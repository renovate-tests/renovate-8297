# Experimenting with Renovate

A small Bazel monorepo that reproduces the issue raised by [discussions #8297](https://github.com/renovatebot/renovate/discussions/8297). The project contains two very, very simple "Hello World" programs.

Expectations: Renovate detects that the Axios 0.20.0 dependency has a vulnerability (CVE-2020-28168) and opens a PR "right away".

Current behavior: the update of Axios is listed in the Dependency Dashboard but it is not flagged as a vulnerability.

## Build, Test and Run

```sh
# Build and test everything
./bazelisk build //packages/...
./bazelisk test //packages/...

# Run the Python and TypeScript examples
./bazelisk run //packages/python/hello/cli:cli
./bazelisk run //packages/typescript/hello/cli:bin

# Clean
./bazelisk clean
./bazelisk clean --expunge
```
