git pull origin master
git pull giteee  master || true
date +"%Y-%m-%d %T"
git add .
git commit -am "Reserved, time: $date"
git push origin master
git push giteee master || true
