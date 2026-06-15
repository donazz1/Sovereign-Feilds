#!/usr/bin/env python3
import sys
import os

def apply_patch(patch_file, target_file):
    with open(patch_file, 'r', encoding='utf-8') as f:
        patch_content = f.read()

    with open(target_file, 'r', encoding='utf-8') as f:
        html = f.read()

    operations = patch_content.split('---PATCH---')
    operations = [op.strip() for op in operations if op.strip()]

    applied = 0
    missed = 0

    for i, op in enumerate(operations, 1):
        if '---REPLACE---' not in op:
            print(f"  [SKIP] Operation {i}: no ---REPLACE--- separator found")
            continue

        parts =
