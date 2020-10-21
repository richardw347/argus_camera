"""
Convert Git tag versioning
to PEP 440
"""
import sys


def versioning_git_to_pep440(version: str) -> str:
    """
    Convert Git tag versioning
    to PEP 440

    EXAMPLES
    --------
    1.0.0 = 1.0.0
    1.0.0-dev = 1.0.0.dev0
    1.0.0-dev-1-ge913d81 = 1.0.0+dev1.ge913d81
    1.0.0-1-ge913d81 = 1.0.0+dev1.ge913d81

    1.0.0+dev1.ge913d81 less than 1.1.0.dev0

    """
    tk_ver = version.split("-")
    if len(tk_ver) <= 1:
        return version
    if tk_ver[1] != "dev":
        tk_ver.insert(1, "dev")
    if len(tk_ver) == 2:
        return ".".join(tk_ver) + "0"
    return "+".join(tk_ver[:2]) + ".".join(tk_ver[2:])


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(versioning_git_to_pep440(sys.argv[1]))
    else:
        print(versioning_git_to_pep440(sys.stdin.read().splitlines()[0]))
