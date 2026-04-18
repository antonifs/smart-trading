def generate_signal(features):
    bullish = 0
    bearish = 0

    if features["ma5"] > features["ma20"]:
        bullish += 1
    else:
        bearish += 1

    if features["volume_ratio"] > 1.5:
        bullish += 1

    if bullish > bearish:
        return {
            "trend": "bullish",
            "confidence": bullish / (bullish + bearish)
        }
    else:
        return {
            "trend": "bearish",
            "confidence": bearish / (bullish + bearish)
        }