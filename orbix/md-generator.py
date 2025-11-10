import os
import ast

def extract_docstrings_from_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        file_content = f.read()
    tree = ast.parse(file_content)
    docs = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            name = node.name
            docstring = ast.get_docstring(node)
            type_name = "Function" if isinstance(node, ast.FunctionDef) else "Class"
            if docstring:
                docs.append((type_name, name, docstring))
    return docs

def generate_markdown(docs, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("# Documentation\n\n")
        for type_name, name, docstring in docs:
            f.write(f"## {type_name}: {name}\n\n")
            f.write(f"{docstring}\n\n")

def scan_directory_for_docs(directory, output_file="DOCS.md"):
    all_docs = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                docs = extract_docstrings_from_file(filepath)
                all_docs.extend(docs)
    generate_markdown(all_docs, output_file)
    print(f"Documentation generated and saved to {output_file}")

if __name__ == "__main__":
    directory = input("Enter directory to scan (default current directory): ").strip()
    if directory == "":
        directory = "."
    scan_directory_for_docs(directory)
