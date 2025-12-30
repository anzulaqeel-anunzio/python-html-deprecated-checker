# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import re
import os

class DeprecatedChecker:
    # List of deprecated tags in HTML5
    DEPRECATED_TAGS = [
        'acronym', 'applet', 'basefont', 'big', 'center', 'dir', 'font', 
        'frame', 'frameset', 'isindex', 'noframes', 'strike', 'tt', 'xmp'
    ]
    
    # Regex to find these tags: <tagname ...
    # We create one regex for efficiency? Or one per tag.
    # Regex: <(tag1|tag2|tag3)\b
    
    PATTERN = re.compile(r'<(' + '|'.join(DEPRECATED_TAGS) + r')\b', re.IGNORECASE)

    @staticmethod
    def scan_file(filepath):
        issues = []
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            for match in DeprecatedChecker.PATTERN.finditer(content):
                tag = match.group(1).lower()
                # find line number
                line_nm = content[:match.start()].count('\n') + 1
                
                issues.append({
                    'line': line_nm,
                    'file': filepath,
                    'tag': tag,
                    'msg': f"Deprecated HTML tag found: <{tag}>"
                })
        except Exception:
            pass
        return issues

    @staticmethod
    def scan_directory(directory):
        all_issues = []
        for root, dirs, files in os.walk(directory):
            if 'node_modules' in dirs: dirs.remove('node_modules')
            if '.git' in dirs: dirs.remove('.git')
            
            for file in files:
                if file.endswith(('.html', '.htm', '.php', '.jsp', '.asp')):
                    path = os.path.join(root, file)
                    issues = DeprecatedChecker.scan_file(path)
                    all_issues.extend(issues)
        return all_issues

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
