# Conclusions

### 1.循环退出条件
### 2.mid 的取值
### 3.low 和 high 的更新

# Playground

二分查找针对的是一个有序的数据集合，查找思想有点类似分治思想。每次都通过跟区间的中间元素对比，将待查找的区间缩小为之前的一半，直到找到要查找的元素，或者区间被缩小为
0。
O(logn) 这种对数时间复杂度。

# Notice

## 循环退出条件

是 low <= high, 不是 low < high.

## 取值写法

mid = low+(high-low)/2 或者 low + ((high-low)>>1)

## low 和 high 的更新

low=mid+1，high=mid-1。注意这里的 +1 和 -1
如果直接写成 low=mid 或者 high=mid，就可能会发生死循环。比如，当 high=3，low=3 时，如果 a[3] 不等于 value，就会导致一直循环不退出。