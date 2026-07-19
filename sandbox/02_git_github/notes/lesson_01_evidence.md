
## Lesson 01: Git's Mental Model - Guided 

**Commands used** (paste the actual commands you ran, in order):

```bash
cd ~/Projects/Learn-DE
   git log --oneline
   git log --graph --oneline --all
   git show --stat HEAD
   cat .git/HEAD
   git symbolic-ref HEAD
    git rev-parse main
   git rev-parse HEAD
```

**Relevant terminal output** (paste the actual output — not a paraphrase):
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ cd ~/Projects/Learn-DE
git log --oneline
git log --graph --oneline --all
e881578 (HEAD -> main, origin/main) Add learning path on 07-13
c87bebc Add Data Engineering learning instructions
9678afe Remove Zone.Identifier files and update gitignore
f3f1329 Initial commit
* e881578 (HEAD -> main, origin/main) Add learning path on 07-13
* c87bebc Add Data Engineering learning instructions
* 9678afe Remove Zone.Identifier files and update gitignore
* f3f1329 Initial commit
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git symbolic-ref HEAD
refs/heads/main
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git symbolic-ref HEAD
refs/heads/main
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git rev-parse HEAD
e881578a44b8401bd7fff28331c6514010df8d69
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git rev-parse main
e881578a44b8401bd7fff28331c6514010df8d69



```



```

**For GitHub web actions (PR / Issue / Release), if applicable**:
- URL:
- Real text you wrote (description, comment, notes):

**Validation performed** (which validation command(s) you ran, and what they showed):

```

```

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):



**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):

---

## Lesson 01: Git's Mental Model - Independent 

linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ gait branch practice/prediction-check
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git branch 
* main
  practice/prediction-check
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git switch practice/prediction-check
Switched to branch 'practice/prediction-check'
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git branch 
  main
* practice/prediction-check
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ echo "Git prediction check" > sandbox/02_git_github/prediction-check.txt
git add sandbox/02_git_github/prediction-check.txt
git commit -m "Add prediction check scratch file"
[practice/prediction-check b4b91e2] Add prediction check scratch file
 1 file changed, 1 insertion(+)
 create mode 100644 sandbox/02_git_github/prediction-check.txt
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git switch main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
linhtran@DESKTOP-FSMTJKA:~/Projects/Learn-DE$ git log --graph --oneline --all --decorate
git rev-parse main
* b4b91e2 (practice/prediction-check) Add prediction check scratch file
* e881578 (HEAD -> main, origin/main) Add learning path on 07-13
* c87bebc Add Data Engineering learning instructions
* 9678afe Remove Zone.Identifier files and update gitignore
* f3f1329 Initial commit
e881578a44b8401bd7fff28331c6514010df8d69

**Short explanation** (2–4 sentences, in your own words: what did you do and why did it work?):
branch practice/prediction-check đi trước main đúng 1 commit.


**Troubleshooting notes** (only if something went wrong — what broke, how you diagnosed it, how you fixed it; leave blank if nothing went wrong):
