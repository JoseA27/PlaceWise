// Este codigo no es funcional, es solo un ejemplo de como se podria implementar utils para un proyecto de React
// helpers.js

/**
 * Utility function to format a date to a readable string.
 * @param {Date} date - The date object to format.
 * @returns {string} - Formatted date string.
 */
export function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString(undefined, options);
}

/**
 * Utility function to capitalize the first letter of a string.
 * @param {string} str - The string to capitalize.
 * @returns {string} - Capitalized string.
 */
export function capitalizeFirstLetter(str) {
    if (!str) return '';
    return str.charAt(0).toUpperCase() + str.slice(1);
}

/**
 * Utility function to generate a random integer between min and max.
 * @param {number} min - The minimum value.
 * @param {number} max - The maximum value.
 * @returns {number} - Random integer.
 */
export function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}