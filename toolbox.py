import os

def get_special_folders_contents():
    special_folders = {
        'Documents': {
            'Windows': os.path.join(os.path.expanduser("~"), 'Documents'),
            'Linux': os.path.join(os.path.expanduser("~"), 'Documents'),
        },
        'Downloads': {
            'Windows': os.path.join(os.path.expanduser("~"), 'Downloads'),
            'Linux': os.path.join(os.path.expanduser("~"), 'Downloads'),
        },
        'Images': {
            'Windows': os.path.join(os.path.expanduser("~"), 'Pictures'),
            'Linux': os.path.join(os.path.expanduser("~"), 'Pictures'),
        },
        'Videos': {
            'Windows': os.path.join(os.path.expanduser("~"), 'Videos'),
            'Linux': os.path.join(os.path.expanduser("~"), 'Videos'),
        },
    }
    
    folder_contents = {}
    
    for folder_name, folder_paths in special_folders.items():
        folder_path = folder_paths.get(os.name, None)
        if folder_path and os.path.exists(folder_path):
            folder_contents[folder_name] = os.listdir(folder_path)
    
    return folder_contents
