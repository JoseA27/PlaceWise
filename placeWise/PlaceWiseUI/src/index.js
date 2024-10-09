// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './styles/tailwind.css'; // Importa Tailwind en tu archivo JS principal
import App from './App';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);
