def build_heading_hierarchy(headings):
    root = []
    stack = []

    for level, text in headings:
        node = {"level": level, "text": text, "children": []}

        if not stack:
            root.append(node)
            stack.append(node)
            continue

        if level > stack[-1]["level"]:
            stack[-1]["children"].append(node)
            stack.append(node)
            continue

        while stack and level <= stack[-1]["level"]:
            stack.pop()

        if stack:
            stack[-1]["children"].append(node)
        else:
            root.append(node)

        stack.append(node)

    return root


def print_hierarchy(tree, indent=0):
    for node in tree:
        print("  " * indent + f"H{node['level']}: {node['text']}")
        print_hierarchy(node["children"], indent + 1)