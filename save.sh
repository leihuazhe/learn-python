git pull --rebase origin master
git pull --rebase giteee master  || true
sleep 2
date +"%Y-%m-%d %T"
git add .
git commit -am "Reserved, time: $(date)"
git push origin master
git push giteee master || true
