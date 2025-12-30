# HTML Deprecated Tag Checker

A validation tool that scans your HTML files for obsolete tags like `<center>`, `<font>`, `<marquee>` (wait, marquee isn't consistently deprecated but often discouraged, this tool focuses on strictly deprecated ones like `applet`, `font`, `center` etc). Helps prepare your project for modern standards.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **HTML5 Compliance**: Detects tags removed from the HTML5 specification.
*   **Unsupported Detection**: Finds `<applet>`, `<frameset>`, `<center>` and more.
*   **Zero Dependencies**: Pure Python.

## Usage

```bash
python run_checker.py [path]
```

### Examples

**1. Scan Project**
```bash
python run_checker.py frontend/
```

**2. Updates**
```html
<center>Text</center> <!-- Flagged -->
<div style="text-align:center">Text</div> <!-- Safe -->
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
