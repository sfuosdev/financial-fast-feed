import React, { useState, useEffect } from 'react';
import axios from 'axios';

function ArticleList() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    fetchArticles();
  }, []);

  const fetchArticles = async () => {
    try {
      const response = await axios.get(`${process.env.REACT_APP_BACKEND_URL}/articles`);
      setArticles(response.data);
    } catch (error) {
      console.error("Error fetching articles:", error);
    }
  };

  return (
    <div>
      <ul>
        {articles.map(article => (
          <li key={article.id} className="article-box">
            <h3>{article.title}</h3>
            <p>{article.summary}</p>
            <p>{article.author}</p>
            <p>{article.date}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ArticleList;
