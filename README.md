While upgrading a kernel from one version to another, one must go through the
manual task of figuring out whether each config option should be enabled, set
to default (olddefconfig), or disabled.

The idea is to make this process less daunting and reduce the risk of oversight
that comes with manual evaluation.

The better approach is to make incremental changes to these configs as the
upstream kernel keeps moving forward, even as a distro is not adopting that
kernel. So once the distro decides to upgrade the kernel, it has a config file
ready.

TODO:
[ ] First step is to create a config record/ database file to keep track config
options across different flavors and architectures.
 
**Stale**
The approach is to start slowly with scripting and later integrate AI to reduce
the manual workload on kernel maintainers. The first step is to build
command-line tools that can later be used by AI agents.

