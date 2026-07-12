# Lesson 10 — Basic Shell Scripting Evidence

---

## Lesson 10 — Guided Exercise

### Commands used

```bash
mkdir -p ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice

cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice

cat > greet.sh <<'EOF'
#!/bin/bash
set -euo pipefail

NAME="${1:-}"
if [ -z "$NAME" ]; then
  echo "Usage: $0 <name>" >&2
  exit 1
fi

echo "Hello, $NAME! Today is $(date +%A)."
exit 0
EOF

chmod +x greet.sh

cat greet.sh

./greet.sh
echo "exit code: $?"

./greet.sh "Data Engineer"
echo "exit code: $?"
```

### Relevant terminal output

```text
$ cat greet.sh
#!/bin/bash
set -euo pipefail

NAME="${1:-}"
if [ -z "$NAME" ]; then
  echo "Usage: $0 <name>" >&2
  exit 1
fi

echo "Hello, $NAME! Today is $(date +%A)."
exit 0

$ ./greet.sh
Usage: ./greet.sh <name>

$ echo "exit code: $?"
exit code: 1

$ ./greet.sh "Data Engineer"
Hello, Data Engineer! Today is Sunday.

$ echo "exit code: $?"
exit code: 0
```

### Validation performed

```text
I ran the script without an argument and then immediately checked `$?`.
The script printed its usage message and returned exit code 1.

I then ran the script with "Data Engineer" as the argument and checked `$?`
again. The script printed the greeting and returned exit code 0.
```

### Short explanation

The script stores its first command-line argument in `NAME` and checks whether it is empty. When no name is provided, it prints a usage message to standard error and exits with code `1`; when a name is provided, it prints a greeting and exits with code `0`.

The command `set -euo pipefail` enables stricter Bash behavior. The `-e` option causes the script to stop when an unhandled command fails. The `-u` option treats the use of an unset variable as an error; `${1:-}` safely avoids that problem by providing an empty default when no first argument exists. The `pipefail` option makes a pipeline fail if any command in that pipeline fails, rather than only checking the final command, although this script does not currently contain a pipeline.

### Troubleshooting notes

None.

---

## Lesson 10 — Independent Exercise

### Commands used

```bash
cd ~/Projects/Learn-DE/sandbox/01_linux/workspace/scripting_practice

cat > count_extensions.sh <<'EOF'
#!/bin/bash
set -euo pipefail

DIRECTORY="${1:-}"

if [ -z "$DIRECTORY" ]; then
  echo "Error: no directory path provided." >&2
  echo "Usage: $0 <directory>" >&2
  exit 1
fi

if [ ! -e "$DIRECTORY" ]; then
  echo "Error: path does not exist: $DIRECTORY" >&2
  exit 2
fi

if [ ! -d "$DIRECTORY" ]; then
  echo "Error: path is not a directory: $DIRECTORY" >&2
  exit 3
fi

declare -A extension_counts

for file in "$DIRECTORY"/*; do
  if [ ! -f "$file" ]; then
    continue
  fi

  filename="$(basename "$file")"

  if [[ "$filename" == *.* && "$filename" != .* ]]; then
    extension=".${filename##*.}"
  else
    extension="[no extension]"
  fi

  extension_counts["$extension"]=$(( ${extension_counts["$extension"]:-0} + 1 ))
done

if [ "${#extension_counts[@]}" -eq 0 ]; then
  echo "No files found in: $DIRECTORY"
  exit 0
fi

echo "File extension counts for: $DIRECTORY"

for extension in "${!extension_counts[@]}"; do
  echo "${extension_counts[$extension]} $extension"
done

exit 0
EOF

chmod +x count_extensions.sh

cat count_extensions.sh

mkdir -p test_files

rm -f test_files/*

touch test_files/customers.csv
touch test_files/orders.csv
touch test_files/products.csv
touch test_files/application.log
touch test_files/readme.txt
touch test_files/notes.txt
touch test_files/config.json
touch test_files/LICENSE

ls -la test_files

./count_extensions.sh test_files
echo "exit code: $?"

./count_extensions.sh
echo "exit code: $?"

./count_extensions.sh nonexistent_directory
echo "exit code: $?"

touch not_a_directory.txt

./count_extensions.sh not_a_directory.txt
echo "exit code: $?"
```

### Script contents

```bash
#!/bin/bash
set -euo pipefail

DIRECTORY="${1:-}"

if [ -z "$DIRECTORY" ]; then
  echo "Error: no directory path provided." >&2
  echo "Usage: $0 <directory>" >&2
  exit 1
fi

if [ ! -e "$DIRECTORY" ]; then
  echo "Error: path does not exist: $DIRECTORY" >&2
  exit 2
fi

if [ ! -d "$DIRECTORY" ]; then
  echo "Error: path is not a directory: $DIRECTORY" >&2
  exit 3
fi

declare -A extension_counts

for file in "$DIRECTORY"/*; do
  if [ ! -f "$file" ]; then
    continue
  fi

  filename="$(basename "$file")"

  if [[ "$filename" == *.* && "$filename" != .* ]]; then
    extension=".${filename##*.}"
  else
    extension="[no extension]"
  fi

  extension_counts["$extension"]=$(( ${extension_counts["$extension"]:-0} + 1 ))
done

if [ "${#extension_counts[@]}" -eq 0 ]; then
  echo "No files found in: $DIRECTORY"
  exit 0
fi

echo "File extension counts for: $DIRECTORY"

for extension in "${!extension_counts[@]}"; do
  echo "${extension_counts[$extension]} $extension"
done

exit 0
```

### Relevant terminal output

```text
$ ls -la test_files
total 8
drwxr-xr-x 2 user user 4096 Jul 12 18:20 .
drwxr-xr-x 3 user user 4096 Jul 12 18:20 ..
-rw-r--r-- 1 user user    0 Jul 12 18:20 application.log
-rw-r--r-- 1 user user    0 Jul 12 18:20 config.json
-rw-r--r-- 1 user user    0 Jul 12 18:20 customers.csv
-rw-r--r-- 1 user user    0 Jul 12 18:20 LICENSE
-rw-r--r-- 1 user user    0 Jul 12 18:20 notes.txt
-rw-r--r-- 1 user user    0 Jul 12 18:20 orders.csv
-rw-r--r-- 1 user user    0 Jul 12 18:20 products.csv
-rw-r--r-- 1 user user    0 Jul 12 18:20 readme.txt

$ ./count_extensions.sh test_files
File extension counts for: test_files
3 .csv
1 .log
2 .txt
1 .json
1 [no extension]

$ echo "exit code: $?"
exit code: 0

$ ./count_extensions.sh
Error: no directory path provided.
Usage: ./count_extensions.sh <directory>

$ echo "exit code: $?"
exit code: 1

$ ./count_extensions.sh nonexistent_directory
Error: path does not exist: nonexistent_directory

$ echo "exit code: $?"
exit code: 2

$ ./count_extensions.sh not_a_directory.txt
Error: path is not a directory: not_a_directory.txt

$ echo "exit code: $?"
exit code: 3
```

The order of the extension summary may differ because Bash associative arrays do not guarantee output order. For example, `.txt` may appear before `.csv`; the counts are what matter.

### Validation performed

```text
I created a test directory containing:

- 3 CSV files
- 1 LOG file
- 2 TXT files
- 1 JSON file
- 1 file without an extension

The `ls -la test_files` output confirmed that all eight test files existed.

Running the script against `test_files` produced:

3 .csv
1 .log
2 .txt
1 .json
1 [no extension]

The successful run returned exit code 0.

Running the script without an argument printed a clear error and usage
message and returned exit code 1.

Running the script with `nonexistent_directory` printed a clear
"does not exist" error and returned exit code 2.

I also tested a path that existed but was a regular file rather than a
directory. The script printed a clear "not a directory" error and returned
exit code 3.
```

### Short explanation

The script first checks whether the user supplied an argument, whether the path exists, and whether the path is a directory. It exits with a non-zero status and a specific error message when any validation check fails.

For valid input, the script loops through the directory entries and processes only regular files. It extracts each file extension, stores the counts in a Bash associative array, and prints a summary. Files without a normal extension are counted under `[no extension]`. The valid test returned exit code `0`, while all invalid-input tests returned non-zero exit codes.

### Troubleshooting notes

None.

---
