// src/components/atoms/SocialIcon.jsx

import React from 'react';

const SocialIcon = ({ href, svgPath }) => (
  <a
    href={href}
    className="p-2 rounded-lg flex items-center border border-gray-300 justify-center transition-all duration-500 hover:border-gray-100 hover:bg-gray-100"
  >
    <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 71 72" fill="none">
      <path d={svgPath} fill="#111827" />
    </svg>
  </a>
);

export default SocialIcon;