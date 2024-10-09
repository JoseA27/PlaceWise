import React, { useState } from "react";

const MultipleFileUpload = () => {
  const [selectedFiles, setSelectedFiles] = useState([]);

  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
  };

  return (
  <div className="mb-5">
    <label className="block mb-2 text-sm font-medium text-gray-900 dark:text-white" for="large_size"></label>
    <input className="block w-full text-lg text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 focus:outline-none dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400" id="large_size" type="file"/>
  </div>
  );
};

export default MultipleFileUpload;