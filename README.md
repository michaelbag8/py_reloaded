# py-reloaded

A Python command-line tool that reads text from an input file, applies a series of text transformations, and writes the result to an output file.

## Usage

```bash
python py_reloaded.py <input_file> <output_file>
```

- `input_file` — path to a text file containing raw text and inline transformation markers.
- `output_file` — path where the transformed text will be written.

## Constraints

- Only the Python standard library is allowed (no third-party packages).
- Test files should be included alongside the implementation.

## Transformations

Applied in the following order, since later rules depend on the results of earlier ones:

1. **`(hex)`** — replaces the word immediately before it with the decimal value of that hexadecimal number.
2. **`(bin)`** — replaces the word immediately before it with the decimal value of that binary number.
3. **`(up)`, `(low)`, `(cap)`** — uppercase, lowercase, or capitalize the word before the marker. Each accepts an optional count, e.g. `(up, 2)`, to apply the transformation to that many preceding words.
4. **Punctuation spacing** — `. , ! ? : ;` hug the preceding word and are followed by a single space before the next word, except for runs like `...` or `!?`, which stay glued together without inserted spacing.
5. **Single-quote pairs** — spaces inside `' ... '` are collapsed so the quotes hug the enclosed word(s), with no space between the quote marks and the text they wrap.
6. **`a` → `an`** — the article `a` is changed to `an` when the following word begins with a vowel or the letter "h".

## Development Approach

This project is being built through a mentorship-style, step-by-step process:

- No complete solutions or full functions are provided upfront — only small illustrative snippets (2–4 lines) to explain isolated concepts.
- Work proceeds in small, incremental milestones (e.g., argument parsing and file I/O before any transformation logic).
- Development starts from questions about approach (string vs. token-list representation, regex vs. manual parsing, edge cases) rather than a prescribed architecture.
- Code review happens through guiding questions rather than direct fixes.
- Test-driven habits are encouraged: usage examples from the spec are turned into test cases before writing the corresponding transformation logic.
- Progress is tracked and periodically summarized to clarify what's built and what remains.