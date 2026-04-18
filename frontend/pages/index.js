import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [ticker, setTicker] = useState("BBCA");
  const [result, setResult] = useState(null);

  const fetchAnalysis = async () => {
    const res = await axios.get("http://localhost:8000/analysis", {
      params: {
        ticker,
        start: "2024-01-01",
        end: "2024-12-31"
      }
    });
    setResult(res.data);
  };

  return (
    <div style={{ padding: 20 }}>
      <h1>Smart Money Tracker</h1>

      <input
        value={ticker}
        onChange={(e) => setTicker(e.target.value)}
      />

      <button onClick={fetchAnalysis}>
        Analyze
      </button>

      {result && (
        <div>
          <h2>{result.ticker}</h2>
          <p>Trend: {result.signal.trend}</p>
          <p>Confidence: {result.signal.confidence}</p>
          <p>Price: {result.latest_price}</p>
        </div>
      )}
    </div>
  );
}