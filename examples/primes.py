#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ilinq.ilinq import Linq


def is_prime(n):
    if n < 2:
        return False

    for j in range(2, n):
        if n % j == 0:
            return False

    return True


if __name__ == '__main__':
    print(
        Linq(range(10**4))
        .last(is_prime))
    # => 9973
