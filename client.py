class OpenRouterSpendingLimitClient:
    def evaluate(self, daily_spend_usd: float, hard_limit_usd: float) -> dict:
        return {"is_blocked": daily_spend_usd >= hard_limit_usd}