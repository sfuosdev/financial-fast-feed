# Introduction

Welcome onboard! Congradulations on become a developer for the Financial Fast Feed project! This document will contain documentation to help you get started with commiting new features.

<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="../client/public/staple-dark.jpg" width="50%">
        <source media="(prefers-color-scheme: light)" srcset="../client/public/staple.jpg" width="50%">
        <img src="../client/public/staple.jpg" alt="Financial Fast Feed">
    </picture>

[Website][Financial Fast Speed] | [Where Does Our Data Come From?] | [Helpful Git Commands] | [Getting Help]
</div>

Financial Fast Feed displays and summmarizes RSS Feeds with GPT-3.5 from 9 different financial news sources. Sources incude Crypto, Economic, and Stock Market news.

*Ethan Cratchley and SFU OS Dev*


## Where Does Our Data Come From?
### Sources: Total - 9
### Crypto
https://Blockchain.News/RSS/
https://bitcoinist.com/feed/
https://www.newsbtc.com/feed/
https://cointelegraph.com/rss

### Stock Market Movements
https://www.reutersagency.com/feed/?best-topics=business-finance&post_type=best
https://seekingalpha.com/feed.xml
https://fortune.com/feed/fortune-feeds/?id=3230629

### Economic Indicators
https://tradingeconomics.com/canada/rss
https://tradingeconomics.com/united-states/rss

## Helpful Git Commands

Below will be a list of useful Github commands and other related things to know before working on the project. Refer to the ["GitHub Cheat Sheet"]: https://education.github.com/git-cheat-sheet-education.pdf if there are any commands here missing!

Before working on project:

```git clone <repository-url>
cd <repo-name> # or open file in IDE
npm install
pip -install -r requirements.txt
git checkout development
git checkout <feature-branch> # We only work off of development and feature branches until further notice or specially asked
```
If you need to test code etc. DM ethan on discord for the .env info and put it in the server folder (MAKE SURE IT IS ALWYAS INCLUDED IN .gitignore, NEVER FETCH IT DIRECTLY)
Run Locally:
*Ensure previous steps complete.
```cd server
Run main.py
cd client
npm install (First Time)
npm start```

Access the App:
Frontend: http://localhost:3000/
Backend: http://localhost:5000/

Keeping Local Up to Date, Pull Latest Changes from Remote:
```git pull origin <branch-name>```

Create new Branch - build feature branches off of development 
```git checkout -b <new-branch-name>```

Switch to Existing Branch:
```git checkout <branch-name>```

Stage Changes and Check Status:
```git add <file-name> or git add .```
```git status```

Commit Changes:
```git commit -m "Your descriptive commit message"```

Push Changes:
```git push origin <branch-name>```

Merge Branches
```git checkout <target-branch>```
```git merge <source-branch>```

Note:*If you make a mistake or have a question feel free to ask in discord, when in doubt you are probably better off asking before pushing any code.* 

Pushing a Branch to Remote Repo:
```git push origin branch-name ```

Deleting a Branch:
```git branch -d branch-name  # Deletes only if the branch is merged
git branch -D branch-name  # Forces deletion
git push origin --delete branch-name # Delete a remote branch```

Merging a Feature Branch to Development:
```git checkout development
git merge feature-branch-name
git push origin development```

Pulling Updated Development Code to Feature Branch:
```git checkout feature-branch-name
git pull origin development```

Undoing Github Push:
```git reset --soft HEAD~1
git push origin -f```

Undoing Github Commit:
Undo the Last Commit (Keep Changes Staged):
```git reset --soft HEAD~1```

Undo the Last Commit (Unstage Changes):
```git reset --mixed HEAD~1```

Undo the Last Commit (Discard Changes):
```git reset --hard HEAD~1```


Undoing a Staged Change:
To unstage changes but keep them in the working directory:
```git reset HEAD file-name```

To unstage all changes:
```git reset```

Check Pushes and Commits:
```git log```


## Getting Help

Join our [discord]: https://discord.gg/cNKsqMQum9 to chat with other developers working on this project!











