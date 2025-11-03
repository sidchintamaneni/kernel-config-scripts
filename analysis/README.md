While upgrading a kernel from one version to another, one must go through the
manual task of figuring out whether each config option should be enabled, set
to default (olddefconfig), or disabled.

The idea is to make this process less daunting and reduce the risk of oversight
that comes with manual evaluation.

The approach is to start slowly with scripting and later integrate AI to reduce
the manual workload on kernel maintainers. The first step is to build
command-line tools that can later be used by AI agents.

TODO:
[] Evaluate the existing kernel kconfig scripts
[] Build a basic command line tool that diff's betweenn two config
[] Add more command line options that does diff's for specific usecases
