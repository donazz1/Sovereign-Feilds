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
            print('  [SKIP] Operation ' + str(i))
            continue
        parts = op.split('---REPLACE---', 1)
        find_text = parts[0].strip('\n')
        replace_text = parts[1].strip('\n')
        if find_text in html:
            html = html.replace(find_text, replace_text, 1)
            applied += 1
            print('  [OK] Operation ' + str(i))
        else:
            missed += 1
            print('  [MISS] Operation ' + str(i))
    with open(target_file, 'w', encoding='utf-8') as f:
        f.write(html)
    if missed > 0:
        sys.exit(1)

if __name__ == '__main__':
    patch_file = sys.argv[1]
    target_file = sys.argv[2]
    apply_patch(patch_file, target_file)
