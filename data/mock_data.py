mock_trending_products = [
    {
        "product_name": f"Product {i}",
        "platform": "YouTube" if i % 3 == 0 else "TikTok" if i % 3 == 1 else "Twitter",
        "mention_count": 50 + i * 3,
        "avg_sentiment": round(0.5 + (i % 5) * 0.05 - (0.1 if i in [5, 12, 19] else 0), 2),
        "top_hashtags": [f"#hashtag{i}", f"#trend{i % 5}", f"#buzz{i % 3}"],
        "forecast": "Trending down" if i in [5, 12, 19] else ("Rising next few days" if i % 2 == 0 else "Stable"),
        "trend_score": round(0.7 + (i % 5) * 0.05 - (0.1 if i in [5, 12, 19] else 0), 2)
    } for i in range(1, 31)
]

mock_product_details = {
    f"Product {i}": {
        "sentiment_history": [round(0.6 - 0.02 * j, 2) for j in range(5)] if i in [5, 12, 19] else [round(0.5 + 0.02 * j, 2) for j in range(5)],
        "mention_history": [60 - j * 5 for j in range(5)] if i in [5, 12, 19] else [40 + j * 5 for j in range(5)],
        "forecast": "Trending down" if i in [5, 12, 19] else ("Still rising" if i % 2 == 0 else "May drop soon"),
        "top_hashtags": [f"#hashtag{i}", f"#buzz{i % 3}", f"#review{i % 4}"]
    } for i in range(1, 31)
}

mock_recommendations = [f"Product {i}" for i in [3, 6, 9, 12, 15, 18, 21, 24, 5, 19]]

mock_alerts = [
    {
        "product": f"Product {i}",
        "platform": "TikTok" if i % 2 == 0 else "YouTube",
        "type": "Spike in mentions" if i % 3 == 0 else "Sentiment Surge",
        "change": f"+{100 + i * 2}%",
        "sentiment": "Rising" if i % 2 == 0 else "Positive",
        "timestamp": f"2025-04-10 0{i % 10}:00 UTC"
    } for i in range(1, 21)
]
