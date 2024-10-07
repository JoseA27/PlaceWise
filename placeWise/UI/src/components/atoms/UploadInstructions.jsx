// src/components/atoms/UploadInstructions.jsx
import UploadIcon from './UploadIcon';

import React from 'react';

const UploadInstructions = () => (
  <div className="flex flex-col items-center justify-center pt-5 pb-6">
    <UploadIcon />
    <p className="mb-2 text-sm text-gray-500 dark:text-gray-400">
      <span className="font-semibold">Click to upload</span> or drag and drop
    </p>
    <p className="text-xs text-gray-500 dark:text-gray-400">STL (MAX. 100MB)</p>
  </div>
);

export default UploadInstructions;
