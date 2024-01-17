import React from 'react';
import './FeedItem.css';

const FeedItem = ({ title, link, summary, date }) => {
  return (
    <a href={link} className="feed-item" target="_blank" rel="noopener noreferrer">
      <div className="feed-item-content">
        <h2 className="feed-title">{title}</h2>
        <div className="feed-meta">
          <span className="feed-date">{new Date(date).toLocaleDateString()}</span>
        </div>
        <p className="feed-summary">{summary}</p>
      </div>
    </a>
  );
};

export default FeedItem;
