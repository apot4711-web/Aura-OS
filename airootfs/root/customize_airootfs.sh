#!/usr/bin/env bash
set -e

# Install the PyPI libraries aura-welcome.py needs that aren't
# available as official Arch packages.
pip install --break-system-packages --no-cache-dir \
    customtkinter \
    arabic_reshaper \
    python-bidi

chmod +x /usr/local/bin/aura-welcome.py
