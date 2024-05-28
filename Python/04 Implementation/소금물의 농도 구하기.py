# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

n, m = map(int, input().split())

answer = (7 * n) / (n + m)

print(format(math.floor(answer * 100) / 100, ".2f"))