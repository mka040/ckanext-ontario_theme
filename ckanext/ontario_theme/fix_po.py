import polib

def fix_unescaped_quotes(po_file_path):
    try:
        po = polib.pofile(po_file_path)
        modified = False

        for entry in po:
            if '"' in entry.msgid:
                # Replace unescaped double quotes in msgid with escaped ones
                entry.msgid = entry.msgid.replace('"', r'\"')
                modified = True
            if '"' in entry.msgstr:
                # Replace unescaped double quotes in msgstr with escaped ones
                entry.msgstr = entry.msgstr.replace('"', r'\"')
                modified = True

        if modified:
            po.save(po_file_path)
            print(f"Unescaped double quotes have been fixed in: {po_file_path}")
    except Exception as e:
        print(f"An error occurred while fixing {po_file_path}: {e}")

def fix_unescaped_quotes_in_multiple_files(file_paths):
    for po_file_path in file_paths:
        fix_unescaped_quotes(po_file_path)

if __name__ == "__main__":
    po_file_paths = [
        "/home/vivek/ckan-docker/src/ckanext-ontario_theme/ckanext/ontario_theme/i18n/ar/LC_MESSAGES/ckanext-ontario_theme.po"
        # Add more file paths to the list as needed
    ]

    fix_unescaped_quotes_in_multiple_files(po_file_paths)
