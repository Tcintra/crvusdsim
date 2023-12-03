from crvusdsim.pool.crvusd import AggregateStablePrice
from curvesim.utils import override

class SimAggregateStablePrice(AggregateStablePrice):

    @override
    def prepare_for_run(self, prices, keep_price: bool = False):
        super().prepare_for_run(prices, keep_price=keep_price)
        if not keep_price:
            # Get/set initial prices
            initial_price = int(prices.iloc[0, :].tolist()[0] * 10**18)
            self.last_price = initial_price
        init_ts = int(prices.index[0].timestamp())
        self.last_timestamp = init_ts
