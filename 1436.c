#include <stdio.h>

int main()
{
    int i, t, s, n, t1;
    int count = 0;
    scanf("%d", &n);
    i = 665;
    while (1)
    {
        t = i;
        s = i;
        while (s > 0)
        {
            t = s % 10;
            if (t == 6) // 6이 한 번
            {
                t = s / 10 % 10;
                if (t == 6) // 6이 두 번
                {
                    t = s / 100 % 10;
                    if (t == 6) // 6이 세 번
                    {
                        t1 = s / 1000 % 10; // 6이 네 번일경우 체크
                        count++;
                        if (n == count) // count와 n이 같으면 출력.
                        {
                            printf("%d", i);
                            return 0;
                        }
                    }
                }
            }
            if (t1 == 6) // 4번이면 i++하고 그냥 한 번 더 돌아가라고 내비둠
            i++;
            s = s / 10;
        }
        i++;
    }
}