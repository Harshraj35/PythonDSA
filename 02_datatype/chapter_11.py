import arrow

brewing_time =arrow.utcnow()
brewing_time.to("Asia/Shanghai")

from collections import namedtuple
chaiProfile = namedtuple("ChaiProfile", ["name", "brewing_time"])