def find_duplicates(filename):
    names = []

    # read file
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith("- "):  # API lines start with '- '
                api_name = line[2:].strip()
                names.append(api_name)

    duplicates = set([name for name in names if names.count(name) > 1])

    if duplicates:
        print("🔁 Duplicate API names found:\n")
        for item in duplicates:
            print(f" - {item}")
    else:
        print("✅ No duplicates found!")

find_duplicates("README.md")