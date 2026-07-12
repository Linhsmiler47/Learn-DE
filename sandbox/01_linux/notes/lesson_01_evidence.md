## Lesson 01: Linux & Ubuntu/WSL Mental Model

## Permission Investigation: Linux filesystem vs `/mnt/c`

### Commands used

```bash
mkdir -p sandbox/01_linux/workspace/permission-test
mkdir -p /mnt/c/Temp/wsl-permission-test

echo "This is the Linux file" \
  > sandbox/01_linux/workspace/permission-test/linux.txt

echo "This is the Windows file" \
  > /mnt/c/Temp/wsl-permission-test/windows.txt

echo "=== BEFORE ==="

ls -l sandbox/01_linux/workspace/permission-test/linux.txt
ls -l /mnt/c/Temp/wsl-permission-test/windows.txt

chmod 000 sandbox/01_linux/workspace/permission-test/linux.txt
chmod 000 /mnt/c/Temp/wsl-permission-test/windows.txt

echo "=== AFTER ==="

ls -l sandbox/01_linux/workspace/permission-test/linux.txt
ls -l /mnt/c/Temp/wsl-permission-test/windows.txt

echo "=== READ LINUX FILE ==="

cat sandbox/01_linux/workspace/permission-test/linux.txt \
  || echo "Linux file read was blocked"

echo "=== READ WINDOWS FILE ==="

cat /mnt/c/Temp/wsl-permission-test/windows.txt \
  || echo "Windows file read was blocked"
```

### Relevant terminal output

```text
=== BEFORE ===
-rw-r--r-- 1 linhtran linhtran 23 Jul 12 16:43 sandbox/01_linux/workspace/permission-test/linux.txt
-rwxrwxrwx 1 linhtran linhtran 25 Jul 12 16:43 /mnt/c/Temp/wsl-permission-test/windows.txt

=== AFTER ===
---------- 1 linhtran linhtran 23 Jul 12 16:43 sandbox/01_linux/workspace/permission-test/linux.txt
-r-xr-xr-x 1 linhtran linhtran 25 Jul 12 16:43 /mnt/c/Temp/wsl-permission-test/windows.txt

=== READ LINUX FILE ===
cat: sandbox/01_linux/workspace/permission-test/linux.txt: Permission denied
Linux file read was blocked

=== READ WINDOWS FILE ===
This is the Windows file
```

### Validation performed

I used `ls -l` before and after applying `chmod 000` to both files. On the Linux filesystem, the permission bits changed to `----------`, and attempting to read the file produced `Permission denied`. On `/mnt/c`, the displayed permissions changed to `-r-xr-xr-x`, but the file could still be read successfully.

### Short explanation

I created one file in the Linux filesystem and another in a temporary folder on the Windows C: drive mounted at `/mnt/c`. I applied the same `chmod 000` command to both files and then attempted to read them. The Linux file became inaccessible, while the `/mnt/c` file remained readable, proving that Linux permission changes are not enforced the same way on the two filesystems.

### Troubleshooting notes

No problems occurred during the investigation.
