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
          console.log("Fetched articles:", data); // Log the fetched articles
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

  if (loading) {
    return <div>Loading...</div>;
  }

  if (articles.length === 0) {
    return <div>No articles available</div>;
  }

  return (
    <div>
      <ul>
        {articles.map((article, index) => ( 
          <li key={index} className="article-box">
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <p>{article.author}</p>
            <p>{article.date}</p>
            <a href={article.link} target="_blank" rel="noopener noreferrer">Read more</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ArticleList;
