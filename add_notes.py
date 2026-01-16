#!/usr/bin/env python3
"""Add empty notes to all config options in annotations file."""

import re
import sys

def add_empty_notes(input_file, output_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()
    
    result = []
    in_header = True
    
    for line in lines:
        # Keep header and comments as-is
        if line.startswith('#') or line.strip() == '':
            result.append(line)
            if '# ---- Annotations without notes ----' in line:
                in_header = False
            continue
        
        # Match config lines with policy
        match = re.match(r'^(CONFIG_\w+)\s+policy<(.+)>$', line.rstrip())
        if match:
            config_name = match.group(1)
            policy = match.group(2)
            # Add line with policy and empty note on same line
            result.append(f"{config_name: <47} policy<{policy}> note<>\n")
        else:
            result.append(line)
    
    with open(output_file, 'w') as f:
        f.writelines(result)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
        sys.exit(1)
    
    add_empty_notes(sys.argv[1], sys.argv[2])
    print(f"Added empty notes to all configs. Output written to {sys.argv[2]}")
