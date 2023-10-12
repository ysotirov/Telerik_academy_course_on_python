
# ПОСЛЕДНОТО
# https://www.youtube.com/watch?v=tRZGeaHPoaw&ab_channel=KevinStratvert



"""
В GITBASH

# Help git config
git config -h

# Подробно инфо за дадена команда
git help {command}

# Показва кой е логнат
git config --global user.name
git config --global user.email

# Логва друг човек
git config --global user.name Yasen Sotirov
git config --global user.email ia.sotirov@gmail.com

# Създаване на default branch
git config --global init.default branch main

# Чисти терминала - само за gitbash, не работи в pycharm terminal
clear

# Премахва фаил/папка от репото и не я траква повече
git rm -r --cached "folder_name"

# Прави ново Репозитори
git init

# Проверка статус
git status

# Траква отново всички файлове
git add --all

# качва в staging-а
git add .

# сваля от staging-a
git restore --staged file_name

# Commit - snapshot на всички файлове към момента
git commit -a -m "Message in quotes"

# Трие файл
git rm "file_name"

# Rename move from old to new file name
git rm "old_file_name" "new_file_name"

# Проверка на всички commit
git log

git fetch - показва новите неща от репото без да ги сваля

# Pull от репото
git pull

git log - показва всики камити до сега
commit 9a6a5a4503ad1f0b1d9727d6d122787c3413fdf4 (HEAD -> main, origin/main)
Author: Philip Sotirov <me@philipsotirov.com>
Date:   Fri Aug 11 18:54:42 2023 +0300

    Add .gitignore

# Компактна версия на горното
git log --oneline


# Добавя към стейджа конкретен фаил
git add file_name

# добавя всички променнени файлове към стейджа
гит адд .


сваля от сеейджа всички файл
git reset


git reset path/fail_name

след като съм ги аднал камитвам фаливете


# Показва адреса на репото на сървъра - има два адреса за fech  и за push
git remote -v


# Показва на къде "гледам" към кой бранч или commit
HEAD -> main


# създава нов branch
git checkout -b branch_name
или
git branch branch_name



отиване на мейн
git checkout main

# присъединяване на бранч към мейна
git merge branch_to_merge_kam_main

№ накрая изпращам към сървъра с push-вам за да кажа на orgin-a





"GIT"  # https://docs.github.com/en/get-started/using-git/about-git
# https://www.youtube.com/watch?v=SWYqp7iY_Tc&ab_channel=TraversyMedia
# оновен курс




# https://learngitbranching.js.org/
# branching



"ИНИЦИАЛИЗИРАНЕ НА ПРАЗНО РЕПО"
# git init


"ПРОВЕРКА СТАТУС working directory & staging area"
# git status


"ДОБАВЯНЕ ФАЙЛ КЪМ staging area"
# git add


"commit a file to our git repository"
# git commit


"ТРИТЕ СЪСТОЯНИЯ НА git"
# Working directory
# Staging area
# Repository


"КОМАДА ЗА ПРОВЕРКА ИСТОРИЯТА НА commits"
# git log


"КОМАНДА ЗА ДОБАВЯНЕ НА ВСИЧКИ ФАЙЛОВЕ И ПАПКИ КЪМ staging area"
# git add -A


"КОМАНДА ЗА ПРЕМАХВАНЕ НА main.py от staging area"
# git reset HEAD main.py

"""

# import os
# from random import randint
#
# for i in range(1, 365):
#     for j in range(0, randint(1, 10)):
#         d = str(i) + ' days ago'
#         with open('file.txt', 'a') as file:
#             file.write(d)
#         os.system('git add .')
#         os.system('git commit --date="' + d + '" -m "commit"')
# os.system('git push -u origin main')


"ПЪЛНЕНЕ НА GIT CONTRIBUTION CHART"
# терминала:
# [main = +2 ~0 -0 !]> python app.py

import os
from random import randint
from datetime import datetime, timedelta

start_date = datetime(2023, 5, 5)
end_date = datetime(2023, 5, 16)

current_date = start_date

while current_date <= end_date:
    # Проверете дали текущият ден не е събота или неделя (0 и 6 са съответно неделя и събота в Python).
    if current_date.weekday() not in [1, 3, 5, 6]:
        num_commits = randint(1, 3)
        for _ in range(num_commits):
            # Създайте и запишете комит.
            commit_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
            with open('file.txt', 'a') as file:
                file.write(commit_date)
            os.system('git add .')
            os.system('git commit --date="' + commit_date + '" -m "commit"')
    # Преминете към следващия ден.
    current_date += timedelta(days=1)

os.system('git push -u origin main')





