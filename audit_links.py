import os
import re
from urllib.parse import urljoin, urlparse

def check_links(directory):
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    print(f"Found {len(html_files)} HTML files.")

    # Regex patterns for different tags and attributes
    patterns = [
        (re.compile(r'<a\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE), 'link'),
        (re.compile(r'<img\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE), 'image'),
        (re.compile(r'<link\s+[^>]*href=["\']([^"\']+)["\']', re.IGNORECASE), 'stylesheet'),
        (re.compile(r'<script\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE), 'script'),
        (re.compile(r'<audio\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE), 'audio'),
        (re.compile(r'<source\s+[^>]*src=["\']([^"\']+)["\']', re.IGNORECASE), 'source'),
    ]

    broken_links = []
    missing_images = []
    missing_scripts = []
    missing_stylesheets = []
    missing_audio = []

    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            base_dir = os.path.dirname(html_file)

            for pattern, tag_type in patterns:
                matches = pattern.findall(content)
                for match in matches:
                    # Handle absolute URLs (http://, https://, //)
                    if match.startswith(('http://', 'https://', '//')):
                        continue
                    
                    # Handle root-relative paths (starting with /)
                    # For this project, we assume the root is the workspace directory
                    if match.startswith('/'):
                        # Remove leading slash and join with workspace root
                        # But wait, if it's /Info for Shareholders.html, it might be relative to the project root
                        # Let's try to see if it exists relative to the workspace root
                        target_path = os.path.join(directory, match.lstrip('/'))
                    else:
                        # Relative path
                        target_path = os.path.normpath(os.path.join(base_dir, match))

                    # Clean up target path (remove fragments like #unaudited)
                    target_path = target_path.split('#')[0].split('?')[0]

                    if not os.path.exists(target_path):
                        error_msg = f"{html_file} -> {match}"
                        if tag_type == 'link':
                            broken_links.append(error_msg)
                        elif tag_type == 'image':
                            missing_images.append(error_msg)
                        elif tag_type == 'stylesheet':
                            missing_stylesheets.append(error_msg)
                        elif tag_type == 'script':
                            missing_scripts.append(error_msg)
                        elif tag_type == 'audio' or tag_type == 'source':
                            missing_audio.append(error_msg)

    return broken_links, missing_images, missing_scripts, missing_stylesheets, missing_audio

if __name__ == "__main__":
    workspace_dir = "."
    broken, images, scripts, styles, audio = check_links(workspace_dir)

    print("\n--- Audit Results ---")
    print(f"Broken Links: {len(broken)}")
    for link in broken[:20]: print(link)
    if len(broken) > 20: print("...")

    print(f"\nMissing Images: {len(images)}")
    for img in images[:20]: print(img)
    if len(images) > 20: print("...")

    print(f"\nMissing Scripts: {len(scripts)}")
    for script in scripts[:20]: print(script)
    if len(scripts) > 20: print("...")

    print(f"\nMissing Stylesheets: {len(styles)}")
    for style in styles[:20]: print(style)
    if len(styles) > 20: print("...")

    print(f"\nMissing Audio/Source: {len(audio)}")
    for aud in audio[:20]: print(aud)
    if len(audio) > 20: print("...")
