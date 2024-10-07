// src/components/atoms/Dropzone.jsx
import UploadInstructions from './UploadInstructions';

import React from 'react';

const Dropzone = ({ onChange }) => (
  <label
    htmlFor="dropzone-file"
    className="flex flex-col items-center justify-center w-full h-64 border-2 border-gray-300 border-dashed rounded-lg cursor-pointer bg-gray-50 dark:hover:bg-gray-800 dark:bg-gray-700 hover:bg-gray-100 dark:border-gray-600 dark:hover:border-gray-500 dark:hover:bg-gray-600"
  >
    <UploadInstructions />
    <input id="dropzone-file" type="file" className="hidden" onChange={onChange} />
  </label>
);

export default Dropzone;
