// src/components/molecules/VideoUpload.jsx

import React, { useState } from 'react';
import { FaChevronLeft, FaChevronRight } from 'react-icons/fa';
import { useSwipeable } from 'react-swipeable';

const VideoUpload = () => {
  const [videos, setVideos] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [animationClass, setAnimationClass] = useState('');

  const handleVideoChange = (event) => {
    const files = Array.from(event.target.files);
    const newVideos = files.map((file) => URL.createObjectURL(file));
    setVideos((prevVideos) => [...prevVideos, ...newVideos]);
    setCurrentIndex(videos.length);
  };

  const prevVideo = () => {
    setAnimationClass('animate-slideOutRight');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === 0 ? videos.length - 1 : prevIndex - 1));
      setAnimationClass('animate-slideInRight');
    }, 250);
  };

  const nextVideo = () => {
    setAnimationClass('animate-slideOutLeft');
    setTimeout(() => {
      setCurrentIndex((prevIndex) => (prevIndex === videos.length - 1 ? 0 : prevIndex + 1));
      setAnimationClass('animate-slideInLeft');
    }, 250);
  };

  const swipeHandlers = useSwipeable({
    onSwipedLeft: () => prevVideo(),
    onSwipedRight: () => nextVideo(),
    preventDefaultTouchmoveEvent: true,
    trackMouse: true,
  });

  return (
    <div className="flex flex-col items-center space-y-4 mt-4">
      {videos.length > 0 && (
        <div
          className="relative w-full h-64 flex justify-center items-center overflow-hidden"
          {...swipeHandlers}
        >
          <button onClick={prevVideo} className="absolute left-0 p-2 text-gray-600 hover:text-black">
            <FaChevronLeft />
          </button>

          <video
            src={videos[currentIndex]}
            className={`object-contain w-auto h-full ${animationClass}`}
            controls
            loop
          />

          <button onClick={nextVideo} className="absolute right-0 p-2 text-gray-600 hover:text-black">
            <FaChevronRight />
          </button>

          {/* Indicadores de posición (puntos) */}
          <div className="absolute bottom-4 flex space-x-1">
            {videos.map((_, index) => (
              <div
                key={index}
                className={`w-2 h-2 rounded-full ${
                  index === currentIndex ? 'bg-gray-300' : 'bg-gray-800'
                }`}
              ></div>
            ))}
          </div>
        </div>
      )}

      <label className="w-24 h-24 flex items-center justify-center border-2 border-gray-300 border-dashed cursor-pointer mt-4">
        <input
          type="file"
          onChange={handleVideoChange}
          className="hidden"
          accept="video/*"
          multiple
        />
        <span className="text-xl text-gray-500">+</span>
      </label>
    </div>
  );
};

export default VideoUpload;
