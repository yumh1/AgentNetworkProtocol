#!/usr/bin/env python3

import os
import re

def natural_sort_key(s):
    """Sort strings containing numbers in natural order."""
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

def rename_files():
    directory = "/Users/cs/work/AgentNetworkProtocol/blogs/images/anp-in-w3c-20250214"
    files = [f for f in os.listdir(directory) if f.endswith('.jpg')]
    
    # Sort files naturally
    files.sort(key=natural_sort_key)
    
    # Rename files
    for i, old_name in enumerate(files, 1):
        old_path = os.path.join(directory, old_name)
        new_name = f"page{i}.jpg"
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")

if __name__ == "__main__":
    rename_files()
