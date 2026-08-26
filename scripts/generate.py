#!/usr/bin/env python3
"""Single entry point for the entire profile generation pipeline."""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from generate_portrait import generate_crystal_portrait, load_config
from generate_skills_svg import generate_skills_svg
from generate_contributions_svg import generate_contributions_svg
from generate_bento_svg import generate_bento_svg
from render_readme import render_readme


def main():
    config = load_config("config.yml")
    print("\n[1/5] Generating portrait...")
    generate_crystal_portrait(config)
    print("\n[2/5] Generating skills HUD...")
    generate_skills_svg()
    print("\n[3/5] Generating contribution flow...")
    generate_contributions_svg()
    print("\n[4/5] Generating engineering showcase...")
    generate_bento_svg()
    print("\n[5/5] Rendering README...")
    render_readme()
    print("\nDone. README.md and all SVG assets are ready.")


if __name__ == "__main__":
    main()
