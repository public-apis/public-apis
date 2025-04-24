# remove_duplicates.py

def remove_duplicate_apis(readme_path):
    seen = set()
    output_lines = []
    duplicates = []

    with open(readme_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        line_strip = line.strip().lower()
        if line_strip.startswith('|') and line_strip.count('|') >= 2:
            if line_strip in seen:
                duplicates.append((i + 1, line.strip()))
                continue
            seen.add(line_strip)
        output_lines.append(line)

    with open(readme_path, 'w', encoding='utf-8') as file:
        file.writelines(output_lines)

    if duplicates:
        print("Removed the following duplicates:")
        for line_num, content in duplicates:
            print(f"Line {line_num}: {content}")
    else:
        print("No duplicates found.")

if __name__ == "__main__":
    remove_duplicate_apis("README.md")
