# coding:utf-8
"""
经典排序算法 - 地精排序Gnome Sort

号称最简单的排序算法,只有一层循环,默认情况下前进冒泡,
一旦遇到冒泡的情况发生就往回冒,直到把这个数字放好为止

java代码：
static void gnome_sort(int[] unsorted)
        {
            int i = 0;
            while (i < unsorted.Length)
            {
                if (i == 0 || unsorted[i - 1] <= unsorted[i])
                {
                    i++;
                }
                else
                {
                    int tmp = unsorted[i];
                    unsorted[i] = unsorted[i - 1];
                    unsorted[i - 1] = tmp;
                    i--;
                }
            }
        }
"""


def gnome_sort(input_list):
    i = 0
    while i < len(input_list):
        if i == 0 or input_list[i-1] <= input_list[i]:
            i += 1
        else:
            input_list[i-1], input_list[i] = input_list[i], input_list[i-1]
            i -= 1
    return input_list

print(gnome_sort([6, 2, 4, 1, 5, 9]))
