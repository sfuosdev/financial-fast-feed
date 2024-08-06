import React, { useState, useEffect } from 'react';

function ArticleList({ selectedSources }) {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch('http://localhost:5001/articles');
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

  return (
    <div className="articles-container">
      {filteredArticles.slice(0, 32).map((article, index) => (
        <div key={index} className="article-box">
          <h3>{article.title}</h3>
          <p>{article.summary}</p>
          <p className="author">{article.author}</p>
          <p className="date">{new Date(article.date).toLocaleDateString()}</p>
          <a href={article.link} target="_blank" rel="noopener noreferrer">Read more</a>
        </div>
      ))}
    </div>
  );
}

export default ArticleList;
