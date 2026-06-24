#!/usr/bin/env python3
"""Create the standard Codex project scaffold.

Args:
    --project-root: Optional target project root. Defaults to the current
        working directory.
"""

from __future__ import annotations

import argparse
from pathlib import Path


DIRECTORIES = (
    Path(".codex/agents"),
    Path(".agents/skills"),
)
FILES = (
    Path("AGENTS.md"),
    Path(".codex/config.toml"),
)


def setup_codex_project(project_root: Path) -> list[Path]:
    """Create required Codex directories and files without overwriting content.

    Args:
        project_root: Directory that should receive the Codex scaffold.

    Returns:
        Paths that were ensured, relative to the project root.
    """
    ensured: list[Path] = []

    # Create parent directories before touching files that live under them.
    for directory in DIRECTORIES:
        (project_root / directory).mkdir(parents=True, exist_ok=True)
        ensured.append(directory)

    for file_path in FILES:
        absolute_path = project_root / file_path
        absolute_path.parent.mkdir(parents=True, exist_ok=True)
        absolute_path.touch(exist_ok=True)
        ensured.append(file_path)

    return ensured


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Args:
        None.

    Returns:
        Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description="Create standard Codex project configuration files.",
    )
    parser.add_argument(
        "--project-root",
        default=".",
        help="Target project root. Defaults to the current working directory.",
    )
    return parser.parse_args()


def main() -> None:
    """Run the setup command.

    Args:
        None.
    """
    args = parse_args()
    project_root = Path(args.project_root).expanduser().resolve()
    project_root.mkdir(parents=True, exist_ok=True)

    ensured = setup_codex_project(project_root)

    print(f"project_root={project_root}")
    for path in ensured:
        print(f"ensured={path}")


if __name__ == "__main__":
    main()
