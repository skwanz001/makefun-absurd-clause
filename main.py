"""The Absurd Clause Contest entry.

Writes one absurd terms-of-service clause (138 characters) to
/output/entry.txt. Python 3.13, standard library only.

Why this line: it opens in perfect buried-boilerplate register ("By
using this service, you agree that..."), then the absurdity lands in
two steps — your shadow becomes Company property, then it is rented
out to third parties, and only on overcast days, when a shadow does
not even exist. One concrete image, one reading, no explaining of
its own joke.
"""

import os

CLAUSE = (
    "By using this service, you agree that your shadow becomes the "
    "property of the Company and may be rented to third parties on "
    "overcast days."
)


def main() -> None:
    # Gate: the sealed scorer only accepts 1-200 characters, not only
    # whitespace. Fail loudly here instead of shipping an invalid entry.
    if not 1 <= len(CLAUSE) <= 200 or not CLAUSE.strip():
        raise ValueError(f"clause is {len(CLAUSE)} characters, must be 1-200")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(CLAUSE)


if __name__ == "__main__":
    main()
