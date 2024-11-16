import React, { useState, useEffect } from 'react';

function ArticleList({ selectedSources = [] }) {
  const [articles, setArticles] = useState([]); // State to store articles
  const [loading, setLoading] = useState(true); // State to manage loading status

  useEffect(() => {
    // Fetch articles when component mounts
    const fetchArticles = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/articles');
        if (response.ok) {
          const data = await response.json();
          setArticles(data);
        } else {
          throw new Error('Network response was not ok.');
        }
      } catch (error) {
        console.error('Error fetching articles:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchArticles();
  }, []);

    // Filter articles based on selected sources
  const filteredArticles = articles.filter(article => {
    if (selectedSources.length === 0) return true;
    return selectedSources.some(source => article.link.includes(source));
  });

  if (loading) {
    return <div>Loading...</div>;
  }

  if (filteredArticles.length === 0) {
    return <div className="no-articles">No articles available</div>;
  }

  // Function to decode HTML
  function decodeHTML(html){
    const txt = document.createElement("textarea");
    txt.innerHTML = html;
    return txt.value;
  }

  return (
    <div className="articles-container">
      {filteredArticles.slice(0, 32).map((article, index) => (
        <div key={index} className="article-box">
          <h3>{decodeHTML(article.title)}</h3>
          <p>{article.summary}</p>
          {article.author !== "No author available" &&
            <p className="author">{article.author}</p>
          }
          <p className="domain">{article.domain}</p>
          <p className="date">{new Date(article.date).toLocaleDateString()}</p>
          <a href={article.link} target="_blank" rel="noopener noreferrer">Read more</a>
        </div>
      ))}
    </div>
  );
}

export default ArticleList;
