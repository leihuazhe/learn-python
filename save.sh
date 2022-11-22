date +"%Y-%m-%d %T"
git add .
git commit -am "Reserved, time: $(date)"

sleep 1

git pull --rebase origin master  || true
git pull --rebase giteee master  || true

sleep 1

git push origin master || true
git push giteee master || true
