
## Lesson 02: Repository Setup, Configuration - Guided 

**Commands used** (paste the actual commands you ran, in order):

```bash
mkdir -p ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
cd ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
git init
ls -la .git
cd ~/Projects/Learn-DE
git config --list --show-origin
git switch main
git switch -c phase-02/gitattributes
cat > .gitattributes <<'EOF'
* text=auto

*.csv binary
*.parquet binary
*.xlsx binary
*.docx binary
*.pdf binary
EOF
git add .gitattributes
git commit -m "Add .gitattributes for line-ending normalization and binary data files"
git check-attr text -- README.md
git check-attr binary -- some_file.csv   # substitute a real path if one exists in the repo
```

**Relevant terminal output** (paste the actual output — not a paraphrase):
llinhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ mkdir -p ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ cd ~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo$ git init
Initialized empty Git repository in /home/linhtran/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo/.git/
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo$ ls -la .git
total 36
drwxr-xr-x 6 linhtran linhtran 4096 Jul 18 21:33 .
drwxr-xr-x 3 linhtran linhtran 4096 Jul 18 21:33 ..
-rw-r--r-- 1 linhtran linhtran   21 Jul 18 21:33 HEAD
-rw-r--r-- 1 linhtran linhtran   92 Jul 18 21:33 config
-rw-r--r-- 1 linhtran linhtran   73 Jul 18 21:33 description
drwxr-xr-x 2 linhtran linhtran 4096 Jul 18 21:33 hooks
drwxr-xr-x 2 linhtran linhtran 4096 Jul 18 21:33 info
drwxr-xr-x 4 linhtran linhtran 4096 Jul 18 21:33 objects
drwxr-xr-x 4 linhtran linhtran 4096 Jul 18 21:33 refs
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE/sandbox/02_git_github/workspace/init_demo$ cd ~/Projects/Learn-DE
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git config --list --show-origin
file:/home/linhtran/.gitconfig  user.name=Linh Tran
file:/home/linhtran/.gitconfig  user.email=linhsmiler47@gmail.com
file:/home/linhtran/.gitconfig  user.email=linhsmiler47@gmail.com
file:/home/linhtran/.gitconfig  init.defaultbranch=main
file:.git/config        core.repositoryformatversion=0
file:.git/config        core.filemode=true
file:.git/config        core.bare=false
file:.git/config        core.logallrefupdates=true
file:.git/config        remote.origin.url=https://github.com/Linhsmiler47/Learn-DE.git
file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
file:.git/config        branch.main.remote=origin
file:.git/config        branch.main.merge=refs/heads/main
(END)
file:/home/linhtran/.gitconfig  init.defaultbranch=main
file:.git/config        core.repositoryformatversion=0
file:.git/config        core.filemode=true
file:.git/config        core.bare=false
file:.git/config        core.logallrefupdates=true
file:.git/config        remote.origin.url=https://github.com/Linhsmiler47/Learn-DE.git
file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
file:.git/config        branch.main.remote=origin
file:.git/config        branch.main.merge=refs/heads/main
(END)
file:/home/linhtran/.gitconfig  init.defaultbranch=main
file:.git/config        core.repositoryformatversion=0
file:.git/config        core.filemode=true
file:.git/config        core.bare=false
file:.git/config        core.logallrefupdates=true
file:.git/config        remote.origin.url=https://github.com/Linhsmiler47/Learn-DE.git
file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
file:.git/config        branch.main.remote=origin
:
file:/home/linhtran/.gitconfig  init.defaultbranch=main
file:.git/config        core.repositoryformatversion=0
file:.git/config        core.filemode=true
file:.git/config        core.bare=false
file:.git/config        core.logallrefupdates=true
file:.git/config        remote.origin.url=https://github.com/Linhsmiler47/Learn-DE.git
file:.git/config        remote.origin.fetch=+refs/heads/*:refs/remotes/origin/*
file:.git/config        branch.main.remote=origin
file:.git/config        branch.main.merge=refs/heads/main
(END)

linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ 
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git switch main
git switch -c phase-02/gitattributes
cat > .gitattributes <<'EOF'
* text=auto

*.csv binary
*.parquet binary
*.xlsx binary
*.docx binary
*.pdf binary
EOF
git add .gitattributes
git commit -m "Add .gitattributes for line-ending normalization and binary data files"
Already on 'main'
Your branch is up to date with 'origin/main'.
Switched to a new branch 'phase-02/gitattributes'
[phase-02/gitattributes 7e029c2] Add .gitattributes for line-ending normalization and binary data files
 1 file changed, 7 insertions(+)
 create mode 100644 .gitattributes
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git check-attr text -- README.md
git check-attr binary -- some_file.csv   # substitute a real path if one exists in the repo
README.md: text: auto
some_file.csv: binary: set
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git log --oneline phase-02/gitattributes -1
7e029c2 (HEAD -> phase-02/gitattributes) Add .gitattributes for line-ending normalization and binary data files

---

## Lesson 02: Repository Setup, Configuration - Independent 

Initial status
?? sandbox/02_git_github/notes/lesson_01_evidence.md
?? sandbox/02_git_github/notes/lesson_02_evidence.md
?? "ymbolic-ref HEAD"
Test 1 — Python bytecode rule: *.pyc

Commands:

mkdir -p .lesson02-tests
touch .lesson02-tests/sample.pyc
git status --short --untracked-files=all
git check-ignore -v .lesson02-tests/sample.pyc
rm .lesson02-tests/sample.pyc
git status --short --untracked-files=all

Relevant output:

.gitignore:14:*.pyc     .lesson02-tests/sample.pyc

The test file did not appear in git status, proving that the *.pyc rule successfully ignores Python bytecode files. The file was removed after the test.

Test 2 — Environment file rule: .env

Commands:

touch .lesson02-tests/.env
git status --short --untracked-files=all
git check-ignore -v .lesson02-tests/.env
rm .lesson02-tests/.env
git status --short --untracked-files=all

Relevant output:

.gitignore:21:.env      .lesson02-tests/.env

The .env test file did not appear in git status, proving that the .env rule successfully protects environment and secret configuration files. The file was removed after the test.

Test 3 — Archive rule: *.zip

Commands:

touch .lesson02-tests/sample.zip
git status --short --untracked-files=all
git check-ignore -v .lesson02-tests/sample.zip
rm .lesson02-tests/sample.zip
git status --short --untracked-files=all

Relevant output:

.gitignore:4:*.zip      .lesson02-tests/sample.zip

The ZIP test file did not appear in git status, proving that the *.zip rule successfully ignores large archive files. The file was removed after the test.

Cleanup

Commands:

rmdir .lesson02-tests
git status --short --untracked-files=all

The test directory and all scratch files were removed. The same pre-existing untracked files remained before and after the tests, confirming that the tests did not leave additional artifacts.

Audit conclusion

The three tested .gitignore rules work correctly:

*.pyc
.env
*.zip

No genuine .gitignore gap was identified from these tests, so no new ignore rule was added.




