import React from 'react';
import ArticleList from './components/ArticleList';
import './App.css';

function App() {
  return (
    <div className="App">
      <header>
        Financial Fast Feed
        {/* You can add a filter button here later */}
      </header>
      <div className="articles-container">
        <ArticleList />
      </div>
    </div>
  );
}

export default App;
