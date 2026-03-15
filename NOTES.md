# Project Notes

## Mistakes & Resolutions

### [2026-03-15] Wrong index for IP address extraction
**Mistake:** Used `parts[10]` to extract the IP address from a log line.
**How we caught it:** Rohan questioned it, we ran an enumerate() check to print each word with its index.
**Resolution:** Correct index is `parts[12]`.
**Lesson:** Never hardcode a list index without verifying it first. Always use enumerate() to confirm position before assuming.
