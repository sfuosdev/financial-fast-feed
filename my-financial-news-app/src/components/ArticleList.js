import React, { useState, useEffect } from 'react';

function ArticleList() {
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch('http://localhost:5000/articles');
        if (response.ok) {
          const data = await response.json();
          // Format the date here and ensure author names are displayed correctly
          const formattedData = data.map(article => ({
            ...article,
            date: formatDate(article.date),
            author: article.author || "Unknown Author" // Fallback if no author name
          }));
          setArticles(formattedData);
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

  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };

  if (loading) {
    return <div>Loading...</div>;
  }

  if (articles.length === 0) {
    return <div>No articles available</div>;
  }

  return (
    <div className="articles-container">
      {articles.slice(0, 32).map((article, index) => (
        <div key={index} className="article-box">
          <h3>{article.title}</h3>
          <p className="summary">{article.summary}</p>
          <p className="author">{article.author}</p>
          <p className="date">{article.date}</p> {/* Formatted Date in bottom-right */}
          <a href={article.link} target="_blank" rel="noopener noreferrer">Read more</a>
        </div>
      ))}
    </div>
  );
}

export default ArticleList;
