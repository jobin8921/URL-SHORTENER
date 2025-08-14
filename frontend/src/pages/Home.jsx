import { useState } from "react";
import axios from "axios";
import "./Home.css";

export default function Home() {
  const [url, setUrl] = useState("");
  const [shortUrl, setShortUrl] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const res = await axios.post("http://127.0.0.1:8000/shorten/", { url });
      setShortUrl(res.data.short_url);
    } catch (error) {
      alert("Something went wrong!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container">
      <header>
        <h1> URL Shortener Web App</h1>
        <p>Paste your long URL below and get a short link instantly!</p>
      </header>

      <main>
        <form onSubmit={handleSubmit} className="shortener-form">
          <input
            type="url"
            placeholder="Enter a long URL here..."
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            required
          />
          <button type="submit" disabled={loading}>
            {loading ? "Shortening..." : "Shorten URL"}
          </button>
        </form>

        {shortUrl && (
          <div className="result">
            <h3> Your Short Link</h3>
            <div className="short-link-box">
              <a href={shortUrl} target="_blank" rel="noreferrer">
                {shortUrl}
              </a>
              <button onClick={() => navigator.clipboard.writeText(shortUrl)}>
                Copy The Link 
              </button>
            </div>

            {/* QR Code */}
            {(() => {
              const shortCode = shortUrl.replace("http://127.0.0.1:8000/", "");
              return (
                <div style={{ marginTop: "20px" }}>
                  <img
                    src={`http://127.0.0.1:8000/qr/${shortCode}/`}
                    alt="QR Code"
                    width="150"
                  />
                </div>
              );
            })()}
          </div>
        )}
      </main>

      <footer>
        <p>Built with using Django & React</p>
      </footer>
    </div>
  );
}
