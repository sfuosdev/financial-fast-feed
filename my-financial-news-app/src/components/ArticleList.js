import React, { useState, useEffect } from 'react';
import axios from 'axios'; 

function ArticleList() {
  const [articles, setArticles] = useState([]);

  useEffect(() => {
    const fetchArticles = async () => {
      try {
        const response = await fetch('http://localhost:5000/articles'); 
        if (response.ok) {
          const data = await response.json();
          setArticles(data);
        } else {
          throw new Error('Network response was not ok.');
        }
      } catch (error) {
        console.error('Error fetching articles:', error);
      }
    };

    fetchArticles(); 
  }, []);

  return (
    <div>
      <ul>
        {articles.map((article, index) => ( 
          <li key={index} className="article-box">
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
