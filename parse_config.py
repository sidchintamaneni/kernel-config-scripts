#!/usr/bin/env python3
"""Parse kernel .config files into a structured record."""

import re
import sys
import yaml


def parse_config(filepath):
    """
    Parse a kernel .config file.
    Returns dict of {option_name: value}.
    Disabled options (# CONFIG_X is not set) get value "n".
    """
    config = {}
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            
            # Match: CONFIG_X=value
            match = re.match(r'^(CONFIG_\w+)=(.+)$', line)
            if match:
                config[match.group(1)] = match.group(2)
                continue
            
            # Match: # CONFIG_X is not set
            match = re.match(r'^# (CONFIG_\w+) is not set$', line)
            if match:
                config[match.group(1)] = 'n'
    
    return config


def build_record(config, version, arch, flavor):
    """
    Build record structure:
    CONFIG_X -> version -> arch -> flavor -> {value, comment}
    """
    record = {}
    for option, value in config.items():
        record[option] = {
            version: {
                arch: {
                    flavor: {
                        'value': value,
                        'comment': ''
                    }
                }
            }
        }
    return record


if __name__ == '__main__':
    if len(sys.argv) != 5:
        print(f"Usage: {sys.argv[0]} <config_file> <version> <arch> <flavor>")
        sys.exit(1)
    
    filepath, version, arch, flavor = sys.argv[1:5]
    
    config = parse_config(filepath)
    record = build_record(config, version, arch, flavor)
    
    print(yaml.dump(record, default_flow_style=False, sort_keys=False))
