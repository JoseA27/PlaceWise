// src/components/molecules/VideoUpload.jsx

import React, { useState } from 'react';
import { FaPlay } from 'react-icons/fa';

const VideoUpload = () => {
  const [videos, setVideos] = useState([]);

  // Maneja la carga de un nuevo video
  const handleVideoChange = (event) => {
    const files = Array.from(event.target.files);
    const newVideos = files.map((file) => URL.createObjectURL(file));
    setVideos((prevVideos) => [...prevVideos, ...newVideos]);
  };

  return (
    <div className="flex flex-col space-y-4 mt-4">
      <div className="flex flex-wrap space-x-4">
        {videos.map((video, index) => (
          <div key={index} className="relative w-24 h-24 border border-gray-300 mb-4">
            <video
              src={video}
              className="object-cover w-full h-full opacity-50"
              muted
              loop
              autoPlay
            />
            <div className="absolute inset-0 flex items-center justify-center">
              <FaPlay className="text-gray-700 text-3xl" />
            </div>
          </div>
        ))}
        <label className="w-24 h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer mb-4">
          <input
            type="file"
            onChange={handleVideoChange}
            className="hidden"
            accept="video/*"
          />
          <span className="text-xl text-gray-500">+</span>
        </label>
      </div>
    </div>
  );
};

export default VideoUpload;
